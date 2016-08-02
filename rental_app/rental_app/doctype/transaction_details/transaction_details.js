// Copyright (c) 2016, Peter Mugenya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transaction Details', {
	refresh: function(frm) {

		cur_frm.add_custom_button('Print Invoice').on('click', function(event) {

        cur_frm.print_doc();
    });

	}
});
