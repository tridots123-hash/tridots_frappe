frappe.ui.form.on('Product Transfer', {
    onload: function(frm) {
        frm.fields_dict['transfer_product_details'].grid.get_field('to_location').get_query = function(doc, cdt, cdn) {
            let row = locals[cdt][cdn];
            return {
                filters: [
                    ['Location', 'name', '!=', row.from_location]
                ]
            };
        };
    },
    onload_post_render: function(frm) {
        hide_child_table_if_empty(frm);
    },
    refresh: function(frm) {
        hide_child_table_if_empty(frm);
    },
    transfer_product_details_add: function(frm) {
        hide_child_table_if_empty(frm);
    },
    transfer_product_details_remove: function(frm) {
        hide_child_table_if_empty(frm);
    }
});

frappe.ui.form.on('Transfer Product Detail', {
    from_location: function(frm, cdt, cdn) {
        frappe.model.set_value(cdt, cdn, 'to_location', '');
        frm.fields_dict['transfer_product_details'].grid.get_field('to_location').get_query = function(doc, cdt, cdn) {
            let row = locals[cdt][cdn];
            return {
                filters: [
                    ['Location', 'name', '!=', row.from_location]
                ]
            };
        };
    }
});

function hide_child_table_if_empty(frm) {
    let child_data = frm.doc.transfer_product_details || [];
    
    if (child_data.length === 0) {
        frm.fields_dict['transfer_product_details'].wrapper.hide();
    } else {
        frm.fields_dict['transfer_product_details'].wrapper.show();
    }
}
