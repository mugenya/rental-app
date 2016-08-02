// Copyright (c) 2016, Peter Mugenya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Invoice Renewals', {

	setup: function(frm) {
		frm.get_field('results').grid.editable_fields = [
			{fieldname: 'invoice', columns: 2},
			{fieldname: 'inv_from', columns: 1},
			{fieldname: 'inv_to', columns: 1},
			{fieldname: 'amount', columns: 1},
			{fieldname: 'tenant', columns: 3},
			{fieldname: 'ucheck', columns: 1},
		];
	},
	refresh: function(frm) {
		 frm.disable_save();
        frm.set_df_property("results", "read_only", 1);
        frm.toggle_enable(['select_all_btn'], false);
       

	},
	search_btn: function(frm){
		if(!frm.doc.s_date_from && !frm.doc.s_date_to){
            msgprint(__("Provide Date from and Date To "));
		   throw "cannot continue";
		}

		$c_obj(frm.doc,'searchRenewals','', function(r, rt) { 
            refresh_many(['results']);
		});
	},
	s_date_from: function(frm){
		frm.set_value("s_date_to",frappe.datetime.add_months(frm.doc.s_date_from,1));
	},
	process_btn: function(frm){
		if(!frm.doc.results){
            msgprint(__("Cannot Continue to Process. Search Records to Renew first"));
		   throw "cannot continue";
		}
		$c_obj(frm.doc,'processRenewals','', function(r, rt) { 
            refresh_many(['results']);
		});
	},
	select_all_btn: function(frm){
		var accounts = frm.doc.results;
		var count=0;
		for(var i in accounts) {
           count++;
		}
		if(count==0){
			msgprint(__("No records to select all"));
			throw "Cannot Continue"
		}

	}
});
