# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class RentalStructures(Document):
	def validate(self):
		count = 0
		for d in self.units_def:
			count+=1
		if(count!=self.no_of_units):
			frappe.throw(_("Units defined does not match the number of units that have been setup"))
		duplicate_houses = []
		for house in self.units_def:
			if(duplicate_houses.__contains__(house.house_name)):
				frappe.throw(_("Duplicate Units Exists {0}").format(house.house_name))
			else:
				duplicate_houses.append(house.house_name)

		if self.no_of_floors > self.no_of_units:
			frappe.throw(_("No of Floors cannot be greater than no of Units"))

