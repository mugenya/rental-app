# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class UnitRates(Document):
	def autoname(self):
		keys = filter(None,(self.rate_type,self.unit_type))
		self.name = " For ".join(keys)
