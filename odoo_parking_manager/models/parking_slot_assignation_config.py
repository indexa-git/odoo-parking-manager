from odoo import models, fields


class ParkingSlotAssignationConfig:
    _name = "parking.slot.assignation.config"
    _description = "Parking Slot Assignation Config"

    type = fields.Selection(
        selection=[
            ("gate", "Distance near to gate."),
            ("exit", "Distance near to exit"),
            ("exclusiveness", "Less exclusiveness"),
        ]
    )
    mandatory = fields.Boolean
