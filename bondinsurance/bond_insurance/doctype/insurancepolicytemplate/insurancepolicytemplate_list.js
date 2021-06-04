// Copyright (c) 2021, Bantoo and contributors
// For license information, please see license.txt

frappe.listview_settings['insurancePolicyTemplate'] = {

	onload: function(listview) {
		listview.page.add_menu_item(__("Get Data"), function() {
			frappe.call({
				method:'bondinsurance.api.get_data',
				callback: function() {
					listview.refresh();
				}
			});
		});
	}
};