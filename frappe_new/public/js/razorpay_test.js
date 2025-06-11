frappe.ui.form.on('Razorpay test', {
    refresh: function (frm) {
        frm.add_custom_button('Open Razorpay', () => {
            let amount_in_paise = frm.doc.currency * 100 || 10000;
            let options = {
                key: "rzp_test_1DP5mmOlF5G5ag",
                amount: amount_in_paise,
                currency: "INR",
                name: frm.doc.customer_name || "Demo User",
                description: "This is Demo Payment No real",
                handler: function(response) {
                    frappe.msgprint("Payment ID:" + response.razorpay_payment_id)
                },
                prefill: {
                    name: frm.doc.customer_name || "Test User",
                    email: frm.doc.email || "imranameen@gmail.com",
                    contact: frm.doc.mobile || "6387906534"
                },
                theme: {
                    color: "#3399cc"
                },
                modal: {
                    ondismiss: function () {
                        frappe.msgprint("You closed the Razorpay popup.")
                    }
                },
                handler: function (response) {
                    frappe.call({
                        method: "frappe.client.set_value",
                        args: {
                            doctype: "Razorpay test",
                            name: frm.doc.name,
                            fieldname: {
                                payment_id: response.razorpay_payment_id
                            }
                        },
                        callback:  function () {
                            frappe.msgprint("Payment successful! Payment ID saved.");
                            frm.reload_doc();
                        }
                    })
                } 
            };
            let rzp = new Razorpay(options);
            rzp.open();
        });
        if (frm.doc.payment_id) {
            frm.add_custom_button('Download Invoice', () => {
                const url = `/api/method/frappe.utils.print_format.download_pdf?doctype=Razorpay test&name=${frm.doc.name}&format=Razorpay Invoice Format&no_letterhead=0`;
                window.open(url);
            })
        }
    }
})