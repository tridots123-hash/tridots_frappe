frappe.ui.form.on('Transfer Product Detail', {
    from_location: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'to_location', '');
        frm.fields_dict.transfer_product_details.grid.get_field('to_location').get_query = function(doc, cdt, cdn) {
            let child = locals[cdt][cdn];
            return {
                filters: [
                    ['Location', 'name', '!=', child.from_location]
                ]
            };
        }
    },
    transfer_product_details_add: function(frm, cdt, cdn) {
        frm.fields_dict.transfer_product_details.grid.get_field('to_location').get_query = function(doc, cdt, cdn) {
            let child = locals[cdt][cdn];
            return {
                filters: [
                    ['Location', 'name', '!=', child.from_location]
                ]
            };
        };
    }
});
