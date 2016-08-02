// Copyright (c) 2016, Peter Mugenya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Account Types', {
	onload: function(frm){
         
	},
	refresh: function(frm) {
		frm.toggle_display('vat_amount', cint(frm.doc.vat_appl)==1);
		frm.toggle_display('whtx_amount', cint(frm.doc.whtx_applicable)==1);
	},
	vat_appl: function(frm){
		frm.toggle_display('vat_amount', cint(frm.doc.vat_appl)==1);
	},
	whtx_applicable: function(frm){
        frm.toggle_display('whtx_amount', cint(frm.doc.whtx_applicable)==1);
	}
});
