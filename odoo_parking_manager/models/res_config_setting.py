from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mandatory = fields.Boolean(string="Mandatory")
    type = fields.Selection(
            selection=[
                ("gate", "Distance near to gate."),
                ("exit", "Distance near to exit"),
                ("exclusiveness", "Less exclusiveness"),
            ]
        )
