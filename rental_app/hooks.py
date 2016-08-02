# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rental_app"
app_title = "Rental App"
app_publisher = "Peter Mugenya"
app_description = "Rental Application to manage Rental Operations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pmugenya@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rental_app/css/rental_app.css"
# app_include_js = "/assets/rental_app/js/rental_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/rental_app/css/rental_app.css"
# web_include_js = "/assets/rental_app/js/rental_app.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rental_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rental_app.install.before_install"
# after_install = "rental_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rental_app.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rental_app.tasks.all"
# 	],
# 	"daily": [
# 		"rental_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"rental_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rental_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rental_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rental_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rental_app.event.get_events"
# }

