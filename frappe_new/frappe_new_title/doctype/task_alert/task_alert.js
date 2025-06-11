frappe.ui.form.on("Task Alert", {
    refresh: function (frm) {
        frappe.realtime.on('new_task_alert_created', function (data) {
            console.log("Realtime data received:", data);
            frappe.msgprint(`🆕 New Task: ${data.title}`);
        });
    }
});
