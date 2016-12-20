# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "access_control"
app_title = "Access Control"
app_publisher = "Hemant and Karan"
app_description = "IoT Access Control for Complexes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hemant@pema.co.za"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/access_control/css/access_control.css"
# app_include_js = "/assets/access_control/js/access_control.js"

# include js, css files in header of web template
# web_include_css = "/assets/access_control/css/access_control.css"
# web_include_js = "/assets/access_control/js/access_control.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "access_control.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "access_control.install.before_install"
# after_install = "access_control.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "access_control.notifications.get_notification_config"

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
# 		"access_control.tasks.all"
# 	],
# 	"daily": [
# 		"access_control.tasks.daily"
# 	],
# 	"hourly": [
# 		"access_control.tasks.hourly"
# 	],
# 	"weekly": [
# 		"access_control.tasks.weekly"
# 	]
# 	"monthly": [
# 		"access_control.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "access_control.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "access_control.event.get_events"
# }

