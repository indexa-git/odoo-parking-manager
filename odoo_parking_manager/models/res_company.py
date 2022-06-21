
from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    odoo_parking_manager_mandatory = fields.Boolean(string="Mandatory")
    odoo_parking_manager_type = fields.Selection(
            selection=[
                ("gate", "Distance near to gate."),
                ("exit", "Distance near to exit"),
                ("exclusiveness", "Less exclusiveness"),
            ]
        )
