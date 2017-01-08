# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hemant and Karan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ResidentialUnit(Document):
	pass


@frappe.whitelist(allow_guest=True)
def unit(pin, unit_number):
	pin_stored = frappe.db.get_doc("Pin")
	if pin_stored.pin == pin:
		unit = {}
		exists = frappe.db.exists('Residential Unit',{'unit_number':unit_number})
		if exists:
			unit = frappe.get_doc('Residential Unit', exists)

		return unit.residents
	else:
		return None

@frappe.whitelist(allow_guest=True)
def bb28741238af481dacf6187153fdc3cf():
	import random

	pin = random.randint(9999, 99999)
	frappe.db.set_value("Pin",None,'pin',pin)
	return pin