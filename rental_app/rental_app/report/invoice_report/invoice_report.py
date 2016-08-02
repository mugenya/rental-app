# Copyright (c) 2013, Peter Mugenya and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = [
		{
			'fieldname': 'trans_amount',
			'label': 'Amount',
			'fieldtype': 'Currency'
		},
		{
			'fieldname': 'trans_balance',
			'fieldtype': 'Currency',
			'label': 'Balance'
		},
		{
			'fieldname': 'trans_reference',
			'fieldtype': 'Data',
			'label': 'Invoice'
		},
		{
			'fieldname': 'tenant',
			'fieldtype': 'Data',
			'label': 'Tenant ID'
		},
	]
	data = frappe.db.sql("""select trans_amount, trans_balance,trans_reference,tenant FROM `tabTransaction Details`""")
	return columns, data
