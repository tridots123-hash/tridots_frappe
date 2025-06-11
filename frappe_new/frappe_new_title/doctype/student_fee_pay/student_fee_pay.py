# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class StudentFeePay(Document):
    pass

@frappe.whitelist()
def pre_pay_registor_student(student_id, student_name, month):
    exists = frappe.db.exists("Std Fee Registration", {
        "student_id": student_id,
        "student_name": student_name,
        "fee_month": month
    })
    if exists:
        data = frappe.db.sql("""
            SELECT phone_no, email, class, fee_amount
            FROM `tabStd Fee Registration`
            WHERE student_id = %s AND student_name = %s AND fee_month = %s                
        """,(student_id, student_name, month), as_dict=True)

        return data

@frappe.whitelist()
def handle_payment(payment_id, student_id, student_name, month, class_section, phone_no, email, fee_amount):
    doc = frappe.get_doc({
        "doctype": "Student Fee Pay",
        "student_id": student_id,
        "student_name": student_name,
        "class": class_section,
        "phone_no": phone_no,
        "email": email,
        "fee_month": month,
        "fee_amount": fee_amount,
        "payment_id": payment_id
	}).insert(ignore_permissions=True)
    
    existing_reg = frappe.db.exists("Std Fee Registration", {
        "student_id": student_id,
        "student_name": student_name,
        "fee_month": month,
        "class": class_section,
        "phone_no": phone_no,
        "email": email,
        "fee_month": month,
        "fee_amount": fee_amount
    })
    if existing_reg:
        reg_doc = frappe.get_doc("Std Fee Registration", existing_reg)
        reg_doc.status ="Paid",
        reg_doc.payment_id = payment_id,
        reg_doc.save(ignore_permissions=True)
        
    frappe.db.commit()
    if doc.payment_id:
       return {
        "status": "success",
        "message": "Your payment is successful",
       }
    else:
       return {
           "status": "failed",
           "message": "Payment failed. Try again."
       }

  

#   @frappe.whitelist()
# def pre_validate_student(student_id, student_name, month):
#     exists = frappe.db.exists("Student Fee Pay", {
#         "student_id": student_id,
#         "fee_month": month
#     })
#     if exists:
#         return f"{student_name} already paid for {month}"
#     return "Valid to proceed"
