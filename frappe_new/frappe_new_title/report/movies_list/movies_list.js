// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.query_reports["Movies List"] = {
	"filters": [
           {
			"fieldname": "genre",
			"label": "Genre",
			"fieldtype": "Select",
			"options": "\nAction \nFight \nComedy",
			"default": "Action",
			"reqd": 0
		   }
	]
};
