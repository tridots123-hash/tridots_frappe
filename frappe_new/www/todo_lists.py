import frappe

def get_context(context):
    context.todo_items = frappe.get_all(
        'Todo Item',
        fields=['title', 'description', 'status'],
        order_by='creation desc'
    )

@frappe.whitelist(allow_guest=True)
def create_task(title, description, status):
    doc = frappe.new_doc("Todo Item")
    doc.title = title
    doc.description = description
    doc.status = status
    doc.insert()
    return {"message": "Your Todo Item has been Successfully created", "name": doc.name}    