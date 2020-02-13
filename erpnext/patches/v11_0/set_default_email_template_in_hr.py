# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe import _

def execute():
	#PFG bug con el idioma
	hr_settings = frappe.get_single("HR Settings")
	hr_settings.leave_approval_notification_template = "Notificación de Autorización de Vacaciones"#_("Leave Approval Notification")
	hr_settings.leave_status_notification_template = "Estado de Notificación de Vacaciones"#_('Leave Status Notification')
	hr_settings.save()