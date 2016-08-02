from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Rental Company Setups"),
			"items": [
				{
					"type": "doctype",
					"name": "Company Details",
					"description": _("Company Details"),
				},
				{
					"type": "doctype",
					"name": "Regions",
					"description": _("Regions"),
				},
				{
					"type": "doctype",
					"name": "Branches",
					"description": _("Branches"),
				},
				{
					"type": "doctype",
					"name": "Landlord Details",
					"description": _("Landlord Details"),
				},
				{
					"type": "doctype",
					"name": "Rental Structures",
					"description": _("Rental Structures"),
				},
				{
					"type": "doctype",
					"name": "Payment Mode",
					"description": _("Payment Mode"),
				},
			]
		},
		{
			"label": _("Units Setups"),
			"items": [
				{
					"type": "doctype",
					"name": "Unit Type Details",
					"description": _("Unit Type Details"),
				},
				{
					"type": "doctype",
					"name": "Rate Types",
					"description": _("Rate Types")
				},
				{
					"type": "doctype",
					"name": "Unit Rates",
					"description": _("Unit Rates")
				},

			]
		},
		{
			"label": _("Accounts and Tenant Setups"),
			"items": [
				{
					"type": "doctype",
					"name": "Account Types",
					"description": _("Account Types"),
				},
				{
					"type": "doctype",
					"name": "Accounts",
					"description": _("Accounts"),
				},
				{
					"type": "doctype",
					"name": "Tenant Details",
					"description": _("Tenant Details")
				},
				{
					"type": "doctype",
					"name": "Deallocate Tenant Unit",
					"description": _("Deallocate Tenant Unit")
				},

			]
		},
		{
			"label": _("Setups Reports"),
			"items": [
				{
					"type": "report",
					"name": "Tenants Report",
					"doctype": "Tenant Details"
				},

			]
		},
		{
			"label": _("Tenants Transactions"),
			"items": [
				{
					"type": "doctype",
					"name": "Tenant Invoice Details",
					"description": _("Tenant Invoice Details"),
				},
				{
					"type": "doctype",
					"name": "Transaction Details",
					"description": _("Invoice Details"),
					"label":_("Invoice Reports")
				},
				{
					"type": "doctype",
					"name": "Invoice Renewals",
					"description": _("Invoice Renewals"),
					"label":_("Invoice Renewals")
				},
				{
					"type": "doctype",
					"name": "Renewal Invoices",
					"description": _("Renewal Invoices"),
					"label":_("Authorize Renewals")
				},

			]
		},
	]
