import frappe
from frappe.model.document import Document


class NewsPaperArticle(Document):
	def validate(self):
       frappe.msgprint("this is override")