# -*- coding: utf-8 -*-
# Copyright (c) 2015, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class TransactionDetails(Document):
	def on_trash(self):
		frappe.throw(_("Cannot delete Transaction Documents..."))
