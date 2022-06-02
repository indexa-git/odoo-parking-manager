from odoo import models, fields


class ParkingSlot(models.Model):
    _name = "parking.slot"
    _description = "Parking Slot"
    name = fields.Char(index=True)
    state = fields.Selection(
        selection=[("1", "Available"), ("2", "Taken"), ("3", "No Available")]
    )
    partner_id = fields.Many2one("res.partner", ondelete="set null", string="Occupant")
    _get_vehicle_types_selection = fields.Selection(selection="parking_vehicle._get_vehicle_types_selection")
    section_id = fields.Many2one("parking.section", ondelete="set null")
    company_id = fields.Many2one(
        "res.company",
        ondelete="set null",
        default=lambda self: self.env.company,
    )
