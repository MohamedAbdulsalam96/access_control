# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hemant and Karan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import uuid
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from random import randint
import datetime

class ResidentialUnit(Document):
	def generate_pin(self):
		#frappe.errprint(self.exit_pin)
		self.entry_pin = randint(10000, 99999)
		self.start_from = frappe.utils.now()
		source_datetime = frappe.utils.get_datetime(self.start_from)
		eod = datetime.datetime(
			year=source_datetime.year,
			month=source_datetime.month,
			day=source_datetime.day
		) + datetime.timedelta(days=1, microseconds=-1)
		self.expires_on=eod
		self.expired = 0
		#frappe.errprint(self.entry_pin)
		#frappe.errprint(self.expires_on)
		self.save()
		#return 1

	def on_update(self):
		source_datetime = frappe.utils.get_datetime(self.start_from)
		eod = datetime.datetime(
			year=source_datetime.year,
			month=source_datetime.month,
			day=source_datetime.day
		) + datetime.timedelta(days=1, microseconds=-1)
		self.expires_on = eod
		#return 1


def check_expired():
	#frappe.logger().debug('Checking Expired pins...')
	for d in frappe.db.sql("""select name, start_from, expires_on, expired
			from `tabResidential Unit`
			where expired = 0 and (start_from is not null or expires_on is not null) """, as_dict=1):

		today = frappe.utils.now_datetime()
		#frappe.logger().debug(str(today) + "|" + str(d.start_from) + "|" + str(d.expires_on))
		if today> d.expires_on:
			frappe.set_value("Residential Unit",d.name,"expired",1)
			frappe.db.commit()
			#frappe.logger().debug('Pin flagged as expired on ' + d.name)

@frappe.whitelist(allow_guest=True)
def verify_enty_pin(pin, entry_pin):
	pin_stored = frappe.get_doc("Pin")

	if pin_stored.pin == pin:
		residents = frappe.db.sql("""select name, entry_pin, start_from, expires_on, expired
							from `tabResidential Unit`
	    					where entry_pin=%(pin)s and expired=0""", {"pin": entry_pin}, as_dict=True)
		if residents !=None:
			return 1
		else:
			return 0


@frappe.whitelist(allow_guest=True)
def unit(pin, unit_number):
	pin_stored = frappe.get_doc("Pin")

	if pin_stored.pin == pin:
		unit = {}
		exists = frappe.db.exists('Residential Unit',{'unit_number':unit_number})
		if exists:
			residents = frappe.db.sql("""select name, contact_type, contact, show_as, sufix from `tabResident`
					where parent=%(name)s and hidden=0
					order by idx""", {"name": exists}, as_dict=True)
			#unit = frappe.get_doc('Residential Unit', exists)

			return residents#residents #unit.residents
		else:
			return None
	else:
		return None

@frappe.whitelist(allow_guest=True)
def call_unit(CLID,From,To, CallStatus):
	pin_stored = frappe.get_doc("Pin")
	pin = To.split('|')[0].split(':')[1]
	if pin_stored.pin == pin:
		if CallStatus == 'ringing':
			from werkzeug.wrappers import Response
			response = Response()
			response.mimetype = 'text/xml'
			response.charset = 'utf-8'
			data= Element("Response")
			dial = SubElement(data, "Dial")
			dial.set('callerId', CLID)
			dial.set('callerName', "kyalom170124081248")
			dial.set('digitsMatchBLeg', '9')
			dial.set('callbackUrl', 'http://gate.pema.co.za:5000/open')
			SubElement(dial, "User").text ='sip:' + To.split('|')[1]
			response.data = tostring(data)
			#tree = ElementTree(response)
			return response
		else:
			return None
		#params = {}
		#params['to'] = 'sip:' + To.split('|')[1]
		#params['clid'] = CLID
		#params['frm']= From
		#return params
	else:
		return None

@frappe.whitelist(allow_guest=True)
def bb28741238af481dacf6187153fdc3cf():
	#import random

	#pin = random.randint(9999, 99999)
	pin=str(uuid.uuid4())

	frappe.db.set_value("Pin",None,'pin',pin)
	frappe.db.commit()
	return pin

@frappe.whitelist(allow_guest=True)
def verify(pin):
	pin_stored = frappe.get_doc("Pin")
	if pin_stored.pin.replace('-','') == pin:
		return True
	else:
		return False


@frappe.whitelist(allow_guest=True)
def verify_number(number):
	exists = frappe.db.exists('Resident', {'contact': number})
	#return exists
	if exists:
		resident = frappe.get_doc('Resident', exists)
		unit = frappe.get_doc('Residential Unit', resident.parent)
		return unit.unit_number
	else:
		return None

@frappe.whitelist(allow_guest=True)
def unit_list(pin):
	pin_stored = frappe.get_doc("Pin")
	if pin_stored.pin == pin:
		_list = frappe.get_all('Residential Unit', fields=['unit_number', 'exit_pin'])
		return _list
	else:
		return None

