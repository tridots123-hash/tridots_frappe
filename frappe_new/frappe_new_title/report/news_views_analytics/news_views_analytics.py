# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label":"News Title", "fieldname": "news_title", "fieldtype": "Data", "width": 200},
        {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 200},
        {"label": "Total Views", "fieldname": "total_views", "fieldtype": "Int", "width": 150},
        {"label": "Viewed On", "fieldname": "viewed_on", "fieldtype": "Date", "width": 200}
    ]
    data = get_data(filters)

    chart = {
         "data": {
             "labels": [row["category"] for row in data],
             "datasets": [
                 {
                     "name": "Views",
                     "values": [row["total_views"] for row in data]
                 }
             ]
         },
         "type": "bar", 
         "colors": ["#E14718"]
     }
    return columns, data, None, chart
    

def get_data(filters):
    condition = ""
    if filters.get("viewed_on"):
        condition += " AND viewed_on = %(viewed_on)s"

    return frappe.db.sql("""
        SELECT category, SUM(views) AS total_views, news_title, viewed_on
        FROM `tabNews View Tracker`
        WHERE 1=1 {condition}
        GROUP BY category
        ORDER BY total_views DESC
    """.format(condition=condition), filters, as_dict=1)

    # data = frappe.db.sql("""
    #     SELECT category, SUM(views) as total_views, news_title, viewed_on
    #     FROM `tabNews View Tracker`
    #     GROUP BY category
    #     ORDER BY total_views DESC
    # """, as_dict=1)

