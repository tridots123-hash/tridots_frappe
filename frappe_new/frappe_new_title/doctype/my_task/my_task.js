// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("My Task", {
	refresh(frm) {
        if(frm.doc.reference_type && frm.doc.reference_name) {
            frm.add_custom_button(frm.doc.reference_name, function () {
                frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name)
            })
        }
	},
});
