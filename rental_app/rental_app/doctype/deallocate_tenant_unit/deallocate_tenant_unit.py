# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class DeallocateTenantUnit(Document):
	def validate(self):
		units = frappe.db.sql("""select name from `tabStructure Units` where allocated=%s""",self.tenant)
		if not units:
			frappe.throw(_("No Unit to Deallocate from tenant"))

	

@frappe.whitelist()
def getTenantDetails(tenant):
	branch,house,unitalloc,firstname,othernames,address = frappe.db.get_value("Tenant Details",tenant,["branch","house_allocated","unit_alloc","f_name","other_names","address"])
	return branch,house,unitalloc,firstname,othernames,address

@frappe.whitelist()
def cancelDeallocation(docname):
	deallocate = frappe.get_doc("Deallocate Tenant Unit",docname)
	deallocate.deallocate = "No"
	deallocate.save()

@frappe.whitelist()
def deallocateTenant(tenant,unitalloc):
    frappe.db.sql("""update `tabStructure Units` set allocated = null where allocated=%s and name=%s""",(tenant,unitalloc))
    frappe.db.sql(""" update `tabTenant Details` set unit_alloc = null where name=%s""",tenant)

@frappe.whitelist()
def getallocationstatus(docname):
	alloc_status = frappe.db.get_value("Deallocate Tenant Unit",docname,["deallocate"])
	return alloc_status

