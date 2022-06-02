from odoo import models, fields, api


class ParkingSlot(models.Model):
    _name = "parking.slot"
    _description = "Parking Slot"

    name = fields.Char(index=True)
    state = fields.Selection(selection="get_slot_state_selection")
    partner_id = fields.Many2one("res.partner", ondelete="set null", string="Occupant")
    section_id = fields.Many2one("parking.section", ondelete="set null")
    company_id = fields.Many2one(
        "res.company",
        ondelete="set null",
        default=lambda self: self.env.company,
    )

    def set_available_slot(self):
        self.state = "1"

    def set_taken_slot(self):
        self.state = "2"

    def set_no_available_slot(self):
        self.state = "3"

    @api.model
    def get_slot_state_selection(self):
        return [("1", "Available"), ("2", "Taken"), ("3", "No Available")]

    def log_slot_historical(self):
        self.sudo().env["parking.slot.historical"].create(
            {
                "slot_id": self.id,
                "partner_id": self.partner_id.id,
                "section_id": self.section_id.id,
                "historical_type": self.state,
            }
        )

    def write(self, vals):
        res = super(ParkingSlot, self).write(vals)

        if res and vals.get("state"):
            self.log_slot_historical()

        return res
