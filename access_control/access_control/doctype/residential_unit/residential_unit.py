# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hemant and Karan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ResidentialUnit(Document):
	pass


@frappe.whitelist(allow_guest=False)
def Unit(unit_number):
	unit = {}
	exists = frappe.db.exists('Residential Unit',{'unit_number':unit_number})
	if exists:
		unit = frappe.db.get_doc('Residential Unit', exists)

	return unit