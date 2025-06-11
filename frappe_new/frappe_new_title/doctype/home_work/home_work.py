import frappe
from frappe.model.document import Document
from frappe import _   # for translatable messages
from frappe.utils.pdf import get_pdf
from frappe.utils import escape_html
from datetime import datetime
from frappe.search.full_text_search import FullTextSearch


class HomeWork(Document):
    pass
#     def validate(self):
#         if not self.title:
#             frappe.throw(_("Title is required"))

def get_context(context):
    context.home_works = frappe.get_all(
        "Home Work",
        fields=["teacher_name", "subject", "class", "topics", "description", "status", "created_at"],
        order_by="creation desc",
        limit_page_length=50,
    )

# @frappe.whitelist()
# def create_task(title, description, status):
#     doc = frappe.get_doc({
#         "doctype": "Todo Item",
#         "title": title,
#         "description": description,
#         "status": status,
#     }).insert(ignore_permissions=True)
    
#     frappe.db.commit()

#     return {
#         "message": "Todo item creation has been successfull",
#         "doc": doc.as_dict(),
#     }

@frappe.whitelist()
def create_task(TeacherName, Subject, Class, Topic, Description, Status, Created):
    doc = frappe.get_doc({
        "doctype": "Home Work",
        "teacher_name": TeacherName,
        "subject": Subject,
        "class": Class,
        "topics": Topic,
        "description": Description,
        "status": Status,
        "created_at": Created
    }).insert(ignore_permissions=True)
    
    frappe.db.commit()

    return {
        "message": "Home work Registor has been successfully Added",
    }

@frappe.whitelist()
def get_task(query=None):
#     # if query:
#     #     results = frappe.get_all(
#     #         "Todo Item",
#     #         filters={
#     #             "title": ["like", f"%{query}%"],
#     #         },
#     #         fields=["title", "description", "status"],
#     #         order_by="creation desc"
#     #     )
#     #     return results
    if query:
        results = frappe.db.sql("""
             SELECT teacher_name, subject, class, topics, description, status, created_at
             FROM `tabHome Work`
             WHERE teacher_name LIKE %(q)s
                OR subject LIKE %(q)s
                OR class LIKE %(q)s
             ORDER BY created_at DESC
        """, {"q": f"%{query}%"}, as_dict=True)
        return results
    if not query:
        todo_get_items = frappe.get_all(
            "Home Work",
            fields=["teacher_name", "subject", "class", "topics", "description", "status", "created_at"],
            order_by="created_at desc"
        )

        return todo_get_items

    

@frappe.whitelist()
def doc_generate():
    home_works = frappe.get_all(
        "Home Work",
        fields=["teacher_name", "subject", "class", "topics", "description", "status", "created_at"],
        order_by="creation desc"
    )
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body { font-family: Inter, sans-serif; font-size: 10pt; }
            h1 { text-align: center; margin-bottom: 20px; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #333; padding: 8px; text-align: left; }
            th { background-color: #f5f5f5; }
        </style>
    </head>
    <body>
        <h1>Student — Today Home Work</h1>
        <table>
            <thead>
                <tr>
                  <th>S.No</th>
                  <th>Teacher Name</th>
                  <th>Subject</th>
                  <th>Topics</th>
                  <th>Description</th>
                  <th>Status</th>
                  <th>Created At</th>
                </tr>
            </thead>
            <tbody>
    """
    for i, item in enumerate(home_works, start=1):
        html += f"""
            <tr>
                <td>{i}</td>
                <td>{escape_html(item.teacher_name)}</td>
                <td>{escape_html(item.subject)}</td>
                <td>{escape_html(item.topics)}</td>
                <td>{escape_html(item.description or "")}</td>
                <td>{escape_html(item.status)}</td>
                <td>{escape_html(item.created_at)}</td>
            </tr>
        """
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    pdf = get_pdf(html)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": f"home_work_{timestamp}.pdf",
        "content": pdf,
        "is_private": 0
    }).insert(ignore_permissions=True)
    return file_doc.file_url

# @frappe.whitelist()
# def search_items(query):
#     if not query:
#         return []

#     fts = FullTextSearch(index_name="web")
#     results = fts.search(query)

#     filtered_results = [r for r in results if r.doctype == "Todo Item"]
#     return filtered_results

# @frappe.whitelist()
# def search_items(query):
#     if not query:
#         return []
#     results = frappe.get_all(
#         "Todo Item",
#         filters={
#             "title": ["like", f"%{query}%"]
#         },
#         fields=["name", "title", "description", "status"]
#     )
#     return results
# @frappe.whitelist(allow_guest=True)
# def create_task(title, description, status):
#     doc = frappe.new_doc("Todo Item")
#     doc.title = title
#     doc.description = description
#     doc.status = status
#     doc.insert()
#     return {"message": "Created", "name": doc.name, "title": doc.title, "description": doc.description, "status":doc.status}
