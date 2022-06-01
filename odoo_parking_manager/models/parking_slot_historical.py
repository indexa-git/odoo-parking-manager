from odoo import models, fields
from odoo.exceptions import UserError


class ParkingSlotHistorical(models.Model):
    _name = "parking.slot.historical"
    _description = "Historical slots parking"

    slot_id = fields.Many2one("parking.slot", string="Parking Slot", index=True)
    partner_id = fields.Many2one("res.partner", string="Occupant", index=True)
    section_id = fields.Many2one("parking.section", string="Section")
    date = fields.Datetime(default=fields.Datetime.now)
    historical_type = fields.Selection([("entry", "Entry"), ("exit", "Exit")])
    company_id = fields.Many2one(
        "res.company",
        required=True,
        string="Company",
        default=lambda self: self.env.company,
    )

    def unlink(self):
        raise UserError('You cannot remove/deactivate the historical.')
