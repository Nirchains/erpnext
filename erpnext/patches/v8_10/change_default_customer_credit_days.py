from __future__ import unicode_literals
import frappe


def execute():
	pass

def make_template(payment_term):
	doc = frappe.new_doc('Payment Terms Template Detail')
	doc.payment_term = payment_term.payment_term_name
	doc.due_date_based_on = payment_term.due_date_based_on
	doc.invoice_portion = payment_term.invoice_portion
	doc.description = payment_term.description
	doc.credit_days = payment_term.credit_days
	doc.credit_months = payment_term.credit_months

	template = frappe.new_doc('Payment Terms Template')
	template.template_name = 'Default Payment Term - {0}'.format(payment_term.payment_term_name)
	template.append('terms', doc)
	template.save()

	return template


def make_payment_term(days, based_on):
	based_on_map = {
		'Fixed Days': 'Day(s) after invoice date',
		'Last Day of the Next Month': 'Month(s) after the end of the invoice month'
	}

	doc = frappe.new_doc('Payment Term')
	doc.due_date_based_on = based_on_map.get(based_on)
	doc.invoice_portion = 100

	if based_on == 'Fixed Days':
		doc.credit_days = days
		doc.description = 'Net payable within {0} days'.format(days)
		doc.payment_term_name = 'N{0}'.format(days)
	else:
		doc.credit_months = 1
		doc.description = 'Net payable by the end of next month'
		doc.payment_term_name = 'EO2M'

	doc.save()
	return doc
