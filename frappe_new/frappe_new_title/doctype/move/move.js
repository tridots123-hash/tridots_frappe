// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt


// frappe.ui.form.on('Move', {
//     refresh: function(frm){
//         frm.add_custom_button('Dialog click', function() {
//             frappe.ui.form.custom_move();
//         })
//     }
// });

// frappe.ui.form.custom_move =  function() {
//     let d = new frappe.ui.Dialog({
//         title: 'Enter details',
//         fields: [
//             {
//                 label: 'First Name',
//                 fieldname: 'first_name',
//                 fieldtype: 'Data'
//             },
//             {
//                 label: 'Last Name',
//                 fieldname: 'last_name',
//                 fieldtype: 'Data'
//             },
//             {
//                 label: 'Age',
//                 fieldname:'age',
//                 fieldtype: 'Int'
//             }
//         ],
//         size: 'small',
//         primary_action_label:'Submit',
//         primary_action: function(values) {
//             console.log(values)
//             d.hide();
//             frappe.msgprint({
//                 title:__('Notification'),
//                 indicator: 'green',
//                 message:__('Document Updated successfully')
//             })
//         }
//     });
//     d.show();
// };

// frappe.ui.form.on('Movie', {
//     refresh:function(frm) {
//         frm.add_custom_button('Load Movies', () => {
//             frappe.call({
//                 method: "frappe_new_title.doctype.movie.get_movies",
//                 callback: function(r) {
//                     console.log(r.message)
//                 }
//             })
//         })
//     }
// })

    frappe.ui.form.on('Move', {
    refresh: function(frm) {
        frm.add_custom_button('Load Movies', () => {
            frappe.call({
                method: "frappe_new.frappe_new_title.doctype.move.move.get_movies",
                callback: function(r) {
                    if (r.message) {
                        // let movie_list = r.message.map(m => `${m.movie_name} (${m.rating})`).join('<br>');
                        // frappe.msgprint({
                        //     title: "Movie List",
                        //     message: movie_list,
                        //     indicator: 'blue'
                        // });
                        // frappe.msgprint(JSON.stringify(r.message));

                        console.log(r.message)
                    }
                }
            });
        });
    }
});