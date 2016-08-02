# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate,today
from frappe.model.document import Document

class TenantDetails(Document):
	def validate(self):
		self.validateDates()

	def validateDates(self):
		years = int((getdate(today()) - getdate(self.dob)).days / 365.25)
		if(years < 18):
			frappe.throw(_("Date of Birth is invalid..Tenant age must be over 18 years"))
		if getdate(self.dob) >= getdate(today()):
			frappe.throw(_("Date of Birth cannot be greater than or equal to Today"))
		if self.status =="Terminated":
			if not self.wet:
				frappe.throw(_("Date of Termination is Mandatory when the tenant is terminated"))

	def on_trash(self):
		frappe.throw(_("Cannot delete a tenant....A tenant can only be updated"))

	def on_update(self):
		for units in frappe.db.sql("""select name from `tabStructure Units` where allocated=%s""",self.name):
			unit = frappe.get_doc("Structure Units",units[0])
			unit.allocated = None
			unit.save()

		unit_allocated = frappe.get_doc("Structure Units",self.unit_alloc)
		unit_allocated.allocated = self.name
		unit_allocated.save()


def tenant_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name	from `tabStructure Units`
			where allocated = %s or allocated is null
				and parent = %s and `%s` LIKE %s limit %s, %s"""
			% ("%s","%s", searchfield, "%s", "%s", "%s"),
			(filters.get("allocated"),filters.get("parent"), "%%%s%%" % txt, start, page_len))