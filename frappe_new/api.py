import frappe

@frappe.whitelist()
def get_actual_qty(product: str, location: str) -> float:
    """
    Return the current stock of *product* at *location* from Stock Balance.

    Called from Stock Movement Item (child table) when a product is picked.
    """
    qty = frappe.db.get_value("Stock Balance",{
        "product": product,
        "location": location},
        "actual_qty"                  
    )
    print(qty)

def handle_alert(doc, method=None):
    frappe.msgprint("This is a doc events alert")
   