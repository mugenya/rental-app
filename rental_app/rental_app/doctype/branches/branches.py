# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Branches(Document):
	def validate(self):
		duplicate_houses = []
		for d in self.houses:
			if duplicate_houses.__contains__(d.rental_house):
				frappe.throw(_("Duplicate Rental Houses Exist..."))
			else:
				duplicate_houses.append(d.rental_house)

		for d in self.houses:
			house = frappe.db.sql("""select name from `tabBranch Rental Structure` where parent!=%s and rental_house=%s """,
				(self.branch_name,d.rental_house))
			if house:
				frappe.throw(_("Rental house {0} has already been attached to another branch").format(d.rental_house))

