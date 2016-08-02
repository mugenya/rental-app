# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Regions(Document):
	def autoname(self):
		self.name = self.region_name

	def validate(self):
		duplicate_branches = []
		for d in self.branches:
			if duplicate_branches.__contains__(d.branch):
				frappe.throw(_("Duplicate Branches Exist"))
			else:
				duplicate_branches.append(d.branch)
        
		for d in self.branches:
			brn = frappe.db.sql("""select name from `tabRegion Branches` where parent!=%s and branch=%s""",
				(self.region_name,d.branch))
			if brn:
				frappe.throw(_("Branch {0} has already been added to another region").format(d.branch))



