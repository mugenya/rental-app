// Copyright (c) 2016, Peter Mugenya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenant Details', {
	refresh: function(frm) {
		var now = frappe.datetime.get_today();
		frm.set_value("wef", now);

	},
	branch: function(frm){
		cur_frm.set_query("house_allocated", function(){
			return{
				"filters":{
					"parent":frm.doc.branch
				}
			}

		});
	},
	house_allocated: function(frm){
		cur_frm.set_query("house_allocated", function(){
			return{
				"filters":{
					"parent":frm.doc.branch
				}
			}

		});

		cur_frm.set_query("unit_alloc", function(){
			return {
					query: "rental_app.rental_app.doctype.tenant_details.tenant_details.tenant_query",
					filters: {
						"allocated": frm.doc.name,
						"parent":frm.doc.house_allocated
					}
				}
		});
	},
	unit_alloc: function(frm){

		cur_frm.set_query("unit_alloc", function(){
			return {
					query: "rental_app.rental_app.doctype.tenant_details.tenant_details.tenant_query",
					filters: {
						"allocated": frm.doc.name,
						"parent":frm.doc.house_allocated
					}
				}
		});

	}
});
