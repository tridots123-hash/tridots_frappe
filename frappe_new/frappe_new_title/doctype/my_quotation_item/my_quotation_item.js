frappe.ui.form.on('My Quotation Item', {
    item_code(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);

        if (row.item_code) {
            frappe.db.get_doc('Item', row.item_code).then(item => {
                frappe.model.set_value(cdt, cdn, 'item_name', item.item_name || '');
                frappe.model.set_value(cdt, cdn, 'rate', item.standard_rate || 0);
                
                frm.fields_dict.items.grid.refresh();
            });
        }
    }
});
