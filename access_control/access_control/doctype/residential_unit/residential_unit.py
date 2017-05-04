# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hemant and Karan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import uuid
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

class ResidentialUnit(Document):
	pass

@frappe.whitelist(allow_guest=True)
def unit(pin, unit_number):
	pin_stored = frappe.get_doc("Pin")

	if pin_stored.pin == pin:
		unit = {}
		exists = frappe.db.exists('Residential Unit',{'unit_number':unit_number})
		if exists:
			unit = frappe.get_doc('Residential Unit', exists)

		return unit.residents
	else:
		return None

@frappe.whitelist(allow_guest=True)
def call_unit(CLID,From,To, CallStatus):
	frappe.log(CLID)
	frappe.log(From)
	frappe.log(To)
	frappe.log(CallStatus)

	pin_stored = frappe.get_doc("Pin")

	if pin_stored.pin == To.split('|')[0].split(':')[1]:
		if CallStatus == 'ringing':
			from werkzeug.wrappers import Response
			response = Response()
			response.mimetype = 'text/xml'
			response.charset = 'utf-8'
			data= Element("Response")
			dial = SubElement(data, "Dial")
			dial.set('callerId', CLID)
			dial.set('callerName', "kyalom170124081248")
			dial.set('digitsmatch', '9')
			SubElement(dial, "User").text = 'sip:' + To.split('|')[1]
			response.data = tostring(data)
			#tree = ElementTree(response)
			return response
		else:
			return To
		#params = {}
		#params['to'] = 'sip:' + To.split('|')[1]
		#params['clid'] = CLID
		#params['frm']= From
		#return params
	else:
		return CLID + ' - ' + To.split('|')[0].split(':')[1]

@frappe.whitelist(allow_guest=True)
def bb28741238af481dacf6187153fdc3cf():
	#import random

	#pin = random.randint(9999, 99999)
	pin=str(uuid.uuid4())

	frappe.db.set_value("Pin",None,'pin',pin)
	frappe.db.commit()
	return pin