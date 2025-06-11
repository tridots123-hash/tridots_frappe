# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words


class StdFeeRegistration(Document):
	pass

@frappe.whitelist()
def pay_registor(student_id, student_name, month, class_section, phone_no, email, fee_amount, status):
	frappe.get_doc({
		"doctype": "Std Fee Registration",
		"student_id": student_id,
		"student_name": student_name,
		"class": class_section,
		"phone_no": phone_no,
		"email": email,
		"fee_month": month,
		"fee_amount": fee_amount,
		"status": status
	}).insert(ignore_permissions=True)

	frappe.db.commit()
    
	return {
		"message": "Your Registration has been successful"
	}

@frappe.whitelist()
def get_pay_data(query=None):
    get_payment_data = frappe.get_all(
        "Std Fee Registration",
        fields=["name", "student_id", "student_name", "class", "phone_no", "email", "fee_month", "fee_amount", "status", "payment_id"],
        order_by="creation desc"
    )
    for record in get_payment_data:
        if record.get("payment_id"):
            record["invoice_url"] = f"/api/method/frappe.utils.print_format.download_pdf?doctype=Std Fee Registration&name={record['name']}&format=Student pay invoice&no_letterhead=0"
        else:
            record["invoice_url"] = None
            
        record["fee_amount_formatted"] = f"₹{record['fee_amount']:,.2f}"

    return get_payment_data

