from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    odoo_parking_manager_mandatory = fields.Boolean(related="company_id.odoo_parking_manager_mandatory", readonly=False)
    # odoo_parking_manager_type = fields.Selection(
    #         related="company_id.odoo_parking_manager_type",
    #         readonly=False,
    #     )
