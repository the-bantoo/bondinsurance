# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bantoo and contributors
# For license information, please see license.txt
import xmltodict, json
from frappe import msgprint, _
from frappe.integrations.utils import make_get_request
import frappe

@frappe.whitelist()
def get_data():
    #frappe.msgprint("working!")
    data = fetch()
    
    
def fetch():
    try:
        data = make_get_request(url="https://ratingqa.itcdataservices.com/Webservices/ITCRateEngineAPI/api/objectsamples/ITCRateEngineRequest?useacord=true")
        sub_xml = data.pop("PolicyData").replace('<?xml version="1.0" encoding="utf-8"?>', "") #remove replace
        cleaned_data = convert(sub_xml, data)
        make_policy_entry(cleaned_data)

    except Exception as e:
        frappe.errprint(_("Something seems is wrong !!! \n \n" + e.))
        
def convert(xmldata, main):
    sub = xmltodict.parse(xmldata)['ACORD']
    main['PolicyData'] = { sub }
    converted = json.dumps(main)
    frappe.errprint(main)
    
    return 
    

def make_policy_entry(data):
    
    todo = frappe.get_doc({
        "doctype":"insurancePolicyTemplate", 
        "data": data
    })
    
    todo.insert()
    
    