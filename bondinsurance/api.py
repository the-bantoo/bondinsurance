# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bantoo and contributors
# For license information, please see license.txt
"""
    This script gets mixed format data from https://ratingqa.itcdataservices.com/Webservices/ITCRateEngineAPI/api/objectsamples/ITCRateEngineRequest?useacord=true
    And converts it to a JSON formatted string before saving it to the insurancePolicyTemplate

    make_policy_entry is pulicly accessible for creating new records

    See https://frappeframework.com/docs/user/en/api/rest for setting up the Frappe API
    
    Requires xmltodict. Go to bench folder and install with this command:
    
        /usr/local/bin/pip3 install xmltodict

"""


import frappe, xmltodict, json
from frappe import msgprint, _
from frappe.integrations.utils import make_get_request


"""
    Called by "Get Data" button found in insurancePolicyTemplate List > Menu [...] > Get Data
"""
@frappe.whitelist()
def get_data():
    
    data = fetch()
    sub_xml = data.pop("PolicyData")
    cleaned_data = convert(sub_xml, data)
    make_policy_entry(cleaned_data)
    

def fetch():
    try:
        return make_get_request(url="https://ratingqa.itcdataservices.com/Webservices/ITCRateEngineAPI/api/objectsamples/ITCRateEngineRequest?useacord=true")
    except Exception as e:
        frappe.errprint(_("Something seems is wrong !!! \n \n" + e))
        
        
def convert(xmldata, main):
    sub = xmltodict.parse(xmldata)['ACORD']
    main['PolicyData'] = sub
    
    return json.dumps(main, indent=4)
    
    
"""
    Callable through the API with a string parameter. For example:
    
        POST https://marketplace.thebantoo.com/api/method/bondinsurance.api.make_policy_entry HTTP/1.1
        
        Content-Type: application/json
        Authorization: token keyapi_key:api_secret
        
        { 
            "data": "'first_name': 'adam'"
        }

"""
@frappe.whitelist()
def make_policy_entry(payload):
    
    todo = frappe.get_doc({
        "doctype":"insurancePolicyTemplate", 
        "data": payload
    })
    todo.insert()