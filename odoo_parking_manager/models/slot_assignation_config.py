from odoo import models, fields


class SlotAssignationConfig:
    type = fields.Selection(
        selection=[
            ("gate", "Distance near to gate."),
            ("exit", "Distance near to exit"),
            ("exclusiveness", "Less exclusiveness"),
        ]
    )
    mandatory = fields.Boolean
