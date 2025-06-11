// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt


frappe.ui.form.on('Book', {
    author: function(frm) {
        if (frm.doc.author) {
            frappe.db.get_doc('Author', frm.doc.author).then(doc => {
                frm.set_value('author_email', doc.email);
            });
        }
    }
});
frappe.form.link_formatters['Author'] = function(value, doc) {
    if (doc && doc.author_email) {
        return value + ' (' + doc.author_email + ')';
    }
    return value;
};
