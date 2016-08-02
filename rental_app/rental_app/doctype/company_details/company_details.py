# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class CompanyDetails(Document):
	def autoname(self):
		self.name = self.company_name

	def validate(self):
		duplicate_regions = []
		for d in self.company_regions:
			if duplicate_regions.__contains__(d.region):
				frappe.throw(_("Duplicate Regions Exist..Remove Duplicates to continue"))
			else:
				duplicate_regions.append(d.region)


