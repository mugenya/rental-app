# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cstr, flt,now_datetime,nowdate
from frappe.model.document import Document

class TenantInvoiceDetails(Document):
	def validate(self):
		if not self.net_amount:
			frappe.throw(_("Net Amount for Invoice cannot be zero"))
		if self.net_amount:
			if flt(self.net_amount) == 0:
				frappe.throw(_("Net Amount for Invoice cannot be zero"))


	def on_submit(self):
		self.createTransaction()

	def on_cancel(self):
		self.cancelTransaction()

	def on_trash(self):
		if self.docstatus == 2:
			frappe.throw(_("Cannot delete Invoice Transactions for Audit..."))
		

	def before_save(self):
		check_invoice = frappe.db.sql("""select name 
					from `tabTenant Invoice Details` 
			    	where ((%s between eff_from and eff_to) or (%s between eff_from and eff_to)) and tenant=%s
			    	""",(self.eff_from,self.eff_from,self.tenant))
		if check_invoice:
			frappe.throw(_("Another invoice overlaps with the invoice to be created. Check dates..."))
		branch,house,unit,fname,othernames,address= self.getTenantDetails()
		self.inv_branch = branch
		self.house_alloc = house
		self.unit_invoiced = unit
		self.tenant_name = "{0} {1}".format(fname,othernames)
		self.address = address

	def getTenantDetails(self):
		branch,house,unitalloc,firstname,othernames,address = frappe.db.get_value("Tenant Details",self.tenant,["branch","house_allocated","unit_alloc","f_name","other_names","address"])
		return branch,house,unitalloc,firstname,othernames,address

	def cancelTransaction(self):
		transaction = frappe.db.sql("""select name from `tabTransaction Details` where trans_reference=%s and trans_type='Debit'""",(self.name),as_dict=1)
		if not transaction:
			frappe.throw(_("Cannot Cancel..Transaction does not exist...."))
		for trans in transaction:
			det = frappe.get_doc("Transaction Details",trans.name)
			det.trans_status = "Cancelled"
			det.save()

	def createTransaction(self):
		trans = frappe.new_doc("Transaction Details")
		trans.trans_date = nowdate()
		trans.trans_reference = self.name
		trans.tenant = self.tenant
		trans.trans_amount = flt(self.inv_amount)
		trans.trans_balance = flt(self.inv_amount)
		trans.settle_amount = flt(0)
		trans.trans_type = "Debit"
		trans.tax_amount = flt(self.total_taxes)
		trans.net_amount = flt(self.net_amount)
		trans.trans_status = "Authorised"
		#trans.trans_agent = self.agent
		trans.commission = 0
		trans.tenant_name = self.tenant_name
		trans.tenant_branch = self.inv_branch
		trans.tenant_house = self.house_alloc
		trans.alloc_house = self.unit_invoiced
		trans.tenant_address = self.address
		trans.period_from = self.eff_from
		trans.period_to = self.eff_to
		trans.insert()



			
	def make_invoice_table(self):
		branch,house,unitalloc = frappe.db.get_value("Tenant Details",self.tenant,["branch","house_allocated","unit_alloc"])
		self.set('inv_items', [])
		if unitalloc:
			deposit_cnt = frappe.db.sql("""select name from `tabTenant Invoice Details` where tenant=%s and docstatus=1""",self.tenant)
			if not deposit_cnt:
				units = frappe.get_doc("Structure Units",unitalloc)
				one_off_invoice = frappe.db.sql("""select rate_type,amount,ifnull(tax_value,0) 
					from `tabUnit Rates` 
			    	where %s between wef and ifnull(wet,curdate()) and frequency='ONE-OFF' and unit_type=%s""",(self.inv_date,units.house_type))
				total_invoice = 0
				total_tax = 0

				for inv in one_off_invoice:
					child = self.append("inv_items", {})
					child.rate_type = cstr(inv[0])
					child.amount = flt(inv[1]) 
					child.tax = flt(inv[2]) 
					child.net_amount = (flt(inv[1]) - flt(inv[2]))
					if(inv[1]):
						total_invoice+=flt(inv[1]) 
					if(inv[2]):
						total_tax+=flt(inv[2]) 

				check_invoice = frappe.db.sql("""select name 
					from `tabTenant Invoice Details` 
			    	where ((%s between eff_from and eff_to) or (%s between eff_from and eff_to)) and tenant=%s
			    	""",(self.eff_from,self.eff_from,self.tenant))
				self.inv_amount = total_invoice
				if total_tax:
					self.total_taxes = total_tax
				else:
					self.total_taxes = 0
				self.net_amount = flt(total_invoice) - flt(total_tax)
				if check_invoice:
				    return;
				


				
				invoice = frappe.db.sql("""select rate_type,amount,ifnull(tax_value,0) 
					from `tabUnit Rates` 
			    	where %s between wef and ifnull(wet,curdate()) and frequency='MONTHLY' and unit_type=%s""",(self.inv_date,units.house_type))
				
				count = 1
				if self.pay_frequency:
					if(self.pay_frequency =="MONTHLY"):
						count = 1
					elif (self.pay_frequency == "QUARTELY"):
						count = 3
					elif (self.pay_frequency == "SEMI-ANNUALLY"):
						count = 6
					elif(self.pay_frequency == "ANNUALLY"):
						count = 12

				for inv in invoice:
					child = self.append("inv_items", {})
					child.rate_type = cstr(inv[0])
					child.amount = flt(inv[1]) * count
					child.tax = flt(inv[2])/100 * flt(inv[1]) * count
					child.net_amount = (flt(inv[1]) - flt(inv[2])/100 * flt(inv[1]))* count
					if(inv[1]):
						total_invoice+=flt(inv[1]) * count
					if(inv[2]):
						total_tax+=flt(inv[2])/100 * flt(inv[1]) * count


				self.inv_amount = total_invoice
				if total_tax:
					self.total_taxes = total_tax
				else:
					self.total_taxes = 0

				self.net_amount = flt(total_invoice) - flt(total_tax)

