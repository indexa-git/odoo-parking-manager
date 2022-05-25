from odoo import models, fields


class ParkingSlot(models.Model):
    _name = "parking.slot"
    _description = "Model for represent the parking slots registers."

    name = fields.Char(index=True)
    state = fields.Selection(
        section=[("1", "Available"), ("2", "Taken"), ("3", "No Available")]
    )
    occupant_id = fields.Many2one("res.partner", ondelete="set null")
    section_id = fields.Many2one("parking.section", ondelete="set null")
    company_id = fields.Many2one("res.company", ondelete="set null")
