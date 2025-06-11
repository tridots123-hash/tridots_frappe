# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
        {"label": "Movie Name", "fieldname": "movie_name", "fieldtype": "Data", "width": 200},
		{"label": "Genre", "fieldname": "genre", "fieldtype": "Select", "width": 200},
		{"label": "Release Date", "fieldname": "release_date", "fieldtype": "Date", "width": 200},
		{"label": "Rating", "fieldname": "rating", "fieldtype": "Float", "width": 200},
 	]


def get_data(filters):
	condition = ""
	if filters.get("genre"):
		condition += "AND genre = %(genre)s"
	return frappe.db.sql("""
       SELECT 
		  movie_name, genre, release_date, rating
	   FROM
		  `tabMove`
	   WHERE
		  1=1 {condition}
	   ORDER BY
		  release_date DESC
    """.format(condition=condition), filters, as_dict=1)