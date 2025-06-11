// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Project Task", {
	refresh(frm) {
        console.log(frm)
       if (frm.doc.docstatus === 0 && !frm.custom_due_date_ctrl) {
        let $wrap = $('<div class="my-control mb-3"></div>').appendTo(frm.fields_dict.title.$wrapper);
        frm.custom_due_date_ctrl = frappe.ui.form.make_control({
            parent: $wrap,
            df: {
                label: 'Temp Due Date',
                fieldname: 'temp_due_date',
                fieldtype: 'Date'
            },
            render_input: true
        });
        frm.custom_due_date_ctrl.$input.on('change', () => {
            console.log('picked', frm.custom_due_date_ctrl.get_value());
        });
       }
	}
});
