# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{"label": "Teacher Name", "fieldname": "teacher_name", "fieldtype": "Data", "width": 200},
		{"label": "Subject", "fieldname": "subject", "fieldtype": "Data", "width": 200},
		{"label": "Class", "fieldname": "class", "fieldtype": "Data", "width": 200},
		{"label": "Topics", "fieldname": "topics", "fieldtype": "Data", "width": 200},
		{"label": "Description", "fieldname": "description", "fieldtype": "Small Text", "width": 200},
		{"label": "Status", "fieldname": "status", "fieldtype": "Select", "width": 200},
		{"label": "Created At", "fieldname": "created_at", "fieldtype": "Date", "width": 200},
	]

	data = frappe.db.sql("""
		SELECT teacher_name, subject, class, topics, description, status, created_at
		FROM `tabHome Work`
		ORDER BY created_at DESC
	""", as_dict=1)

	status_data = frappe.db.sql("""
		SELECT status, subject, COUNT(*) AS count
		FROM `tabHome Work`
		GROUP BY status
	""", as_dict=1)

	chart = {
		"data": {
			"labels": [row["status"] for row in status_data],
			"datasets": [
				{
					"name": "Status Count",
					"values": [row["count"] for row in status_data]
				}
			]
		},
		"type": "bar",
		"colors": ["#E14718"]
	}

	return columns, data, None, chart
