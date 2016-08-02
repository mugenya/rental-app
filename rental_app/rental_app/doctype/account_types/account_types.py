# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe.model.document import Document

class AccountTypes(Document):
	def validate(self):
		if(self.vat_appl):
			if(flt(self.vat_amount)==0):
				frappe.throw(_("VAT Amount cannot be zero"))
		if(self.whtx_applicable):
			if(flt(self.whtx_amount)==0):
				frappe.throw(_("WHTX Amount cannot be zero"))
		det = frappe.db.sql("""select name from `tabAccount Types` where acct_type=%s""",(self.acct_type))
		if det:
			frappe.throw(_("Rates for the account type already exists"))
