app_name = "frappe_new"
app_title = "frappe-new-title"
app_publisher = "imran"
app_description = "test app"
app_email = "imranexpo123@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "frappe_new",
# 		"logo": "/assets/frappe_new/logo.png",
# 		"title": "frappe-new-title",
# 		"route": "/frappe_new",
# 		"has_permission": "frappe_new.api.permission.has_app_permission"
# 	}
# ]
# test_string = "value"
# test_list = ["value"]
# test_dict = {
#     "key": "value"
# }

# student_app/hooks.py
# website_route_rules = [
#     {"from_route": "/student-records", "to_route": "frappe_new/www/student-records"}
# ]

doctype_js = {
    "Product Transfer": "public/js/product_transfer.js"
}

doctype_js = {
    "Move": "public/js/movie.js"
}

doctype_js = {
    "Razorpay test": "public/js/razorpay_test.js"
}

fixtures = [
    {
        "dt": "News Alert",
        "filters": {
            "is_active": 1
        }
    }
]
# app_include_js = "/assets/frappe_new/js/razorpay_test.js"

# my_custom_app/hooks.py

sounds = [
    {
        "name": "success",
        "src": "/assets/frappe_new/sounds/glass-break-316720.mp3"
    }
]

website_route_rules = [
    {"from_route": "/home_work", "to_route": "home_work"}
]

website_route_rules = [
    {"from_route": "/expense-entry", "to_route": "expense_entry"}
]

website_route_rules = [
    {"from_route": "/student_payment", "to_route": "student_payment"}
]

website_route_rules = [
    {"from_route": "/Payment_register", "to_route": "Payment_register"}
]

app_include_js = [
    "https://checkout.razorpay.com/v1/checkout.js"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_new/css/frappe_new.css"
# app_include_js = "/assets/frappe_new/js/frappe_new.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_new/css/frappe_new.css"
# web_include_js = "/assets/frappe_new/js/frappe_new.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappe_new/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "frappe_new/public/broadcast.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "frappe_new.utils.jinja_methods",
# 	"filters": "frappe_new.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_new.install.before_install"
# after_install = "frappe_new.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_new.uninstall.before_uninstall"
# after_uninstall = "frappe_new.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "frappe_new.utils.before_app_install"
# after_app_install = "frappe_new.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "frappe_new.utils.before_app_uninstall"
# after_app_uninstall = "frappe_new.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_new.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"News Paper Article": "frappe_new.frappe_new_title.overrides.news_paper_articles.NewsPaperArticle"
}

before_migrate = "frappe_new.frappe_new_title.migrate.before_migrate"
after_migrate = "frappe_new.frappe_new_title.migrate.after_migrate"

portal_menu_items = [
    {"title": "Dashboard", "route": "/dashboard", "role": "Administrator"},
    {"title": "Orders", "route": "/orders", "role": "Administrator"},
]

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"News Alert": {
		"before_insert": "frappe_new.api.handle_alert"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_new.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_new.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_new.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_new.tasks.weekly"
# 	],
# 	"monthly": [
# 		"frappe_new.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "frappe_new.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_new.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_new.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["frappe_new.utils.before_request"]
# after_request = ["frappe_new.utils.after_request"]

# Job Events
# ----------
# before_job = ["frappe_new.utils.before_job"]
# after_job = ["frappe_new.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"frappe_new.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

