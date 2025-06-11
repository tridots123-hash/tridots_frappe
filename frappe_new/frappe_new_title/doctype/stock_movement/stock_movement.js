// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Stock Movement", {
	refresh: function(frm) {
        frm.toggle_display("products_transferred", frm.doc.products_transferred.length > 0)
	},
});

frappe.ui.form.on("Stock Movement Item", {
    product: function(frm, cdt, cdn) {
        console.log(frm)
        const row = locals[cdt][cdn];
        if (!frm.doc.form_location || !row.product) {
            frappe.msgprint("Please select both From Location and Product.")
        }
        frappe.call({
            method: "frappe_new_title.api.get_actual_qty",
            args: {
                product: row.product,
                location: frm.doc.form_location
            },
            callback: function(r) {
                if (r.message !== undefined) {
                    frappe.model.set_value(cdt, cdn, "qty", r.message)
                }
            }
        })
    }
})
