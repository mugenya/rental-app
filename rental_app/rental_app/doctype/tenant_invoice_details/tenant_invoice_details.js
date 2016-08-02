// Copyright (c) 2016, Peter Mugenya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenant Invoice Details', {
	refresh: function(frm) {

		if(!frm.doc.__islocal) {
			//frm.set_df_property("inv_items", "read_only", 1);
			frm.set_df_property("pay_frequency", "read_only", 1);
			frm.set_df_property("inv_amount", "read_only", 1);
		     frm.set_df_property("total_taxes", "read_only", 1);
		     frm.set_df_property("net_amount", "read_only", 1);

		}


	},
	setup: function(frm) {
		frm.get_field('inv_items').grid.editable_fields = [
			{fieldname: 'rate_type', columns: 3},
			{fieldname: 'amount', columns: 2},
			{fieldname: 'tax', columns: 2},
			{fieldname: 'net_amount', columns: 2}
		];
	},
	tenant: function(frm){
		if(frm.doc.tenant){
			frappe.call({
				method: "rental_app.rental_app.doctype.deallocate_tenant_unit.deallocate_tenant_unit.getTenantDetails",
				args: {
					"tenant": frm.doc.tenant
				},
				callback: function(r, rt) {
					frm.set_value("inv_branch", r.message[0]);
					frm.set_value("house_alloc", r.message[1]);
					frm.set_value("unit_invoiced", r.message[2]);
					frm.set_value("tenant_name",r.message[3]+" "+r.message[4]);
					frm.set_value("address",r.message[5]);
					console.log("Address "+r.message[5]);
				}
			});

			var invoiceItems = frm.doc.inv_items || [];
			//if (invoiceItems.length == 0)
		     $c_obj(frm.doc,'make_invoice_table','', function(r, rt) { 
		     	refresh_many(['inv_items','inv_amount','total_taxes','net_amount']);
		     });

		     //frm.set_df_property("inv_items", "read_only", 1);
		     frm.set_df_property("inv_amount", "read_only", 1);
		     frm.set_df_property("total_taxes", "read_only", 1);
		     frm.set_df_property("net_amount", "read_only", 1);
		     cur_frm.reload_doc();
		}


	},
	eff_from: function(frm){
		if(frm.doc.pay_frequency =="MONTHLY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,1));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,1);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		else if(frm.doc.pay_frequency =="QUARTELY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,3));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,3);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		else if(frm.doc.pay_frequency =="SEMI-ANNUALLY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,6));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,6);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		else if(frm.doc.pay_frequency =="ANNUALLY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,12));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,12);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		
	},
	pay_frequency: function(frm){
		if(frm.doc.pay_frequency =="MONTHLY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,1));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,1);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		else if(frm.doc.pay_frequency =="QUARTELY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,3));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,3);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		else if(frm.doc.pay_frequency =="SEMI-ANNUALLY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,6));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,6);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		else if(frm.doc.pay_frequency =="ANNUALLY"){
			if(frm.doc.eff_from){
				frm.set_value("eff_to",frappe.datetime.add_months(frm.doc.eff_from,12));
				var effto = frappe.datetime.add_months(frm.doc.eff_from,12);
				frm.set_value("ren_date",frappe.datetime.add_days(effto,1));
			}
		}
		if(frm.doc.tenant){
			frappe.call({
				method: "rental_app.rental_app.doctype.deallocate_tenant_unit.deallocate_tenant_unit.getTenantDetails",
				args: {
					"tenant": frm.doc.tenant
				},
				callback: function(r, rt) {
					frm.set_value("inv_branch", r.message[0]);
					frm.set_value("house_alloc", r.message[1]);
					frm.set_value("unit_invoiced", r.message[2]);
					frm.set_value("tenant_name",r.message[3]+" "+r.message[4]);
					frm.set_value("address",r.message[5]);
				}
			});

			var invoiceItems = frm.doc.inv_items || [];
			//if (invoiceItems.length == 0)
		     $c_obj(frm.doc,'make_invoice_table','', function(r, rt) { 
		     	refresh_many(['inv_items','inv_amount','total_taxes','net_amount']);
		     });

		    // frm.set_df_property("inv_items", "read_only", 1);
		     frm.set_df_property("inv_amount", "read_only", 1);
		     frm.set_df_property("total_taxes", "read_only", 1);
		     frm.set_df_property("net_amount", "read_only", 1);
		}
	}
});
