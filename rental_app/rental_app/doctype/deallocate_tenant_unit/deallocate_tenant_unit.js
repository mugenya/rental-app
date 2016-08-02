// Copyright (c) 2016, Peter Mugenya and contributors
// For license information, please see license.txt

frappe.ui.form.on('Deallocate Tenant Unit', {
	refresh: function(frm) {
           if(frm.doc.deallocate == "Yes"){
          	frm.set_df_property("deallocate", "read_only", 1);
          	frm.set_df_property("tenant", "read_only", 1);
          }
          
	},
	deallocate: function(frm){
       if(frm.doc.deallocate == "Yes"){
       	  frm.set_df_property("reason_dealloc", "read_only", 0); 
       }
       else{
       	 frm.set_df_property("reason_dealloc", "read_only", 1); 
       }
	},
	tenant: function(frm){
		if(frm.doc.tenant){
			frappe.call({
				method: "rental_app.rental_app.doctype.deallocate_tenant_unit.deallocate_tenant_unit.getTenantDetails",
				args: {
					"tenant": frm.doc.tenant
				},
				callback: function(r, rt) {
					frm.set_value("branch", r.message[0]);
					frm.set_value("house_alloc", r.message[1]);
					frm.set_value("unit_alloc", r.message[2]);
				}
			})
		}
	},
	validate: function(frm){
         var df = frappe.meta.get_docfield("Deallocate Tenant Unit","deallocate", cur_frm.doc.name);
         if(cint(df.read_only)==1){
         	frappe.msgprint(__("Deallocation on this unit has already been done"));
         	return;
         }
		if(frm.doc.deallocate == "Yes")
		frappe.confirm(
			    'Are you sure you want to Deallocate the Room from tenant ?',
			    function(){
			      frappe.call({
						method: "rental_app.rental_app.doctype.deallocate_tenant_unit.deallocate_tenant_unit.deallocateTenant",
						args: {
							"tenant": frm.doc.tenant,
							"unitalloc": frm.doc.unit_alloc
						},
						callback: function(r, rt) {
							cur_frm.reload_doc();
						}
					})
			    },
			    function(){
			          frappe.call({
						method: "rental_app.rental_app.doctype.deallocate_tenant_unit.deallocate_tenant_unit.cancelDeallocation",
						args: {
							"docname": frm.doc.name
						},
						callback: function(r, rt) {
							cur_frm.reload_doc();
						}
					})
			    }
			)
       //}
	}
});
