// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee", {
// 	refresh(frm) {

// 	},
// });

frappe.listview_settings['Employee'] = {
  add_fields: ["status"],
  get_indicator: function(doc) {
    if (doc.status === "Active"){
      return [__("Active"), "yellow", "status,=,Active"];
    } else {
      return [__("Inactive"), "orange", "status,=,Inactive"];
    }
  },
  onload: function(listview) {
    listview.page.set_title("Active Employees");
  }
}