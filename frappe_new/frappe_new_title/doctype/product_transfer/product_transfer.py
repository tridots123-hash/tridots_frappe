# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ProductTransfer(Document):
    def validate(self):
        settings = frappe.get_single("Settings")
        max_total = settings.max_total_qty_per_transaction
        max_per_product = settings.max_qty_per_product

        frappe.msgprint(f"Max total: {max_total}, Max per product: {max_per_product}")
