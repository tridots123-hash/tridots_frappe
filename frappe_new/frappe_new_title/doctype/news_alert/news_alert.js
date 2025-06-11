// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("News Alert", {
	onload(frm) {
        if (!frm.doc.date) {
            frm.set_value('date', frappe.datetime.get_today());
        }
    },

    validate(frm) {
        if (!frm.doc.title || !frm.doc.description) {
            frappe.throw('Title and description are required');
        }
    },

    is_active(frm) {
        if (frm.doc.is_active) {
            frappe.msgprint('This news alert is active');
        }
    }
});
