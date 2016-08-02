from __future__ import unicode_literals
import frappe
from frappe.desk.reportview import get_match_cond
from frappe.utils import nowdate


def tenant_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name	from `tabStructure Units`
			where allocated = (%s) or allocated is null
				and parent = %s and `%s` LIKE %s limit %s, %s"""
			% ("%s", searchfield, "%s", "%s", "%s"),
			(filters.get("parent"), "%%%s%%" % txt, start, page_len))