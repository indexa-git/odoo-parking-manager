{
    "name": "Odoo Parking Manager",
    "summary": "",
    "description": """
    """,
    "author": "CECOMSA, CardNet, Indexa",
    "website": "",
    "category": "",
    "version": "14.0.0.3.1",
    "depends": ["base_setup", "mail"],
    "data": [
        "security/ir_rule_data.xml",
        "security/res_user_data.xml",
        "security/res_groups_data.xml",
        "security/ir.model.access.csv",
        "data/res_partner_data.xml",
        "views/odoo_parking_manager_menu.xml",
        "views/parking_section_views.xml",
        "views/parking_vehicle_maker_views.xml",
        "views/res_partner_views.xml",
        "views/parking_vehicle_views.xml",
        "views/parking_slot_views.xml",
        "views/parking_slot_historical_views.xml",
        "views/res_config_settings_views.xml",
        "data/parking.vehicle.maker.csv",
    ],
    "demo": [
        "demo/res_partner_demo.xml",
        "demo/parking_section_demo.xml",
        "demo/parking.slot.csv",
    ],
}
