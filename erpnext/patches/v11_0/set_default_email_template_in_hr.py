from __future__ import unicode_literals
import frappe

def execute():
	#PFG bug con el idioma
	hr_settings = frappe.get_single("HR Settings")
	hr_settings.leave_approval_notification_template = _("Leave Approval Notification")
	hr_settings.leave_status_notification_template = _('Leave Status Notification')
	hr_settings.save()