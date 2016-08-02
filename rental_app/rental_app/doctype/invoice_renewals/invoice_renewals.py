# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate,cstr,flt,nowdate,add_months,add_days
from frappe.model.document import Document

class InvoiceRenewals(Document):

	def validate(self):
		frappe.throw(_("Cannot save a Search document"))

	def searchRenewals(self):
		self.set('results', [])
		if(getdate(self.s_date_from) > getdate(self.s_date_to)):
			frappe.throw(_("Date From cannot be greater than Date To..."))
		invoices = frappe.db.sql("""select a.name,eff_from,eff_to,inv_amount,concat(f_name,' ',other_names),
			       inv_date,unit_invoiced FROM `tabTenant Invoice Details` a,`tabTenant Details` b
			       where a.tenant = b.name and ren_date between %s and %s and
			         branch=ifnull(%s,branch) and house_allocated=ifnull(%s,house_allocated)
			          and a.name not in (select inv_no from `tabRenewal Invoices`)""",(self.s_date_from,self.s_date_to,self.s_branch,self.s_rental))
		#if not invoices:
		#	frappe.throw(_("There are no invoices due for renewal for the selected period"))
		for ren in invoices:
			child = self.append("results", {})
			child.invoice = cstr(ren[0])
			child.inv_from = getdate(ren[1])
			child.inv_to = getdate(ren[2])
			child.amount = flt(ren[3])
			child.tenant = cstr(ren[4])
			child.inv_date = getdate(ren[5])
			child.unit = cstr(ren[6])
			child.ucheck = True

	def processRenewals(self):
		count = 0
		for d in self.results:
			if d.ucheck == True:
				count+=1
		if(count==0):
			frappe.throw(_("No Records to process"))

		for d in self.results:
			if d.ucheck == True:
				trans = frappe.new_doc("Renewal Invoices")
				invoice = frappe.get_doc("Tenant Invoice Details",cstr(d.invoice))
				if not invoice:
					frappe.throw(_("The invoice does not exist..."))
				else:
					trans.inv_no = cstr(d.invoice)
					trans.tenant = invoice.tenant
					trans.trans_date = nowdate
					trans.eff_from = invoice.ren_date
					rendate = invoice.ren_date
					if(invoice.pay_frequency == "MONTHLY"):
						trans.eff_to = add_months(invoice.ren_date,1)
						rendate = add_months(invoice.ren_date,1)
					elif(invoice.pay_frequency == "QUARTELY"):
						trans.eff_to = add_months(invoice.ren_date,3)
						rendate = add_months(invoice.ren_date,3)
					elif(invoice.pay_frequency == "SEMI-ANNUALLY"):
						trans.eff_to = add_months(invoice.ren_date,6)
						rendate = add_months(invoice.ren_date,6)
					elif(invoice.pay_frequency == "ANNUALLY"):
						trans.eff_to = add_months(invoice.ren_date,12)
						rendate = add_months(invoice.ren_date,12)
					trans.ren_date = add_days(rendate,1)
					trans.pay_freq = invoice.pay_frequency
					trans.pay_mode = invoice.pay_mode
					trans.currency = invoice.currency
					tenant = frappe.get_doc("Tenant Details", invoice.tenant)
					if not tenant:
						frappe.throw(_("The tenant for invoice {0} does not exist in the system").format(cstr(d.invoice)))
					else:
						trans.ten_name = "{0} {1}".format(tenant.f_name,tenant.other_names)
						trans.address = tenant.address
					trans.house_alloc = invoice.house_alloc
					trans.unit_inv = invoice.unit_invoiced
					trans.branch_inv = invoice.inv_branch
					trans.inv_items = invoice.inv_items
					trans.amount = invoice.inv_amount
					trans.taxes = invoice.total_taxes
					trans.net_amount = invoice.net_amount
				trans.insert()
		self.set('results',[])
		frappe.msgprint(_("Renewals processed successfully {0}").format(count))





