{
    "name": "Odoo Parking Manager",
    "summary": "",
    "description": """
    """,
    "author": "CECOMSA, CardNet, Indexa",
    "website": "",
    "category": "",
    "version": "14.0.0.3.1",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/odoo_parking_manager_menu.xml",
        "views/parking_section_views.xml",
        "views/parking_vehicle_maker_views.xml",
        "views/res_partner_views.xml",
        "views/parking_vehicle_views.xml",
        "views/parking_slot_views.xml",
        "views/parking_slot_historical_views.xml",
    ],
    "demo": [
        "demo/parking_section_demo.xml",
        "demo/slot_demo.csv",
    ],
}
