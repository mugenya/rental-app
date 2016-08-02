# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate
from frappe import _
from frappe import utils
from frappe.model.document import Document

class Accounts(Document):
	def validate(self):
		self.validateDates()
		

	def validateDates(self):
		if(getdate(utils.today()) < getdate(self.wef)):
			frappe.throw(_("WEF Date cannot be greater than today"))
		if(self.wet):
			if(getdate(self.wef) > getdate(self.wet)):
				frappe.throw(_("WEF Date cannot be greater than WET Date"))


  
