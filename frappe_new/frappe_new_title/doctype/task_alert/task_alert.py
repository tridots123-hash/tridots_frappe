# import frappe
from frappe.model.document import Document


class TaskAlert(Document):
    pass
    # def valdate(self):
    #     # doc = frappe.get_doc("Task Alert", "TASK-0001")
    #     #  task = frappe.get_last_doc('Task Alert')
    # def after_submit(self):
    #     task = frappe.get_last_doc('Task Alert"', filters={"status": "Cancelled"})
    #     print(task)
    # create a new document
    #   def after_submit(self): 
    #       doc = frappe.new_doc('Task Alert')
    #       doc.title = 'New Task 2'
    #       doc.insert()
    #   def validate(self):
    #         frappe.delete_doc('Task Alert', 'TASK-0001')
        # def vaidate(self):
        #     frappe.rename_doc('Task Alert', 'TASK-0007', 'TASK-0010')
        # def validate(self):
        #     meta = frappe.get_meta('Task Alert')
        #     meta.has_field('status') # True
        #     meta.get_custom_fields() # [field1, field2, ..]
        #     print(meta)
