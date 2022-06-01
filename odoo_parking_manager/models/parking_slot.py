from odoo import models, fields


class ParkingSlot(models.Model):
    _name = "parking.slot"
    _description = "Parking Slot"

    name = fields.Char(index=True)
    state = fields.Selection(
        selection=[("1", "Available"), ("2", "Taken"), ("3", "No Available")]
    )
    partner_id = fields.Many2one("res.partner", ondelete="set null", string="Occupant")
    section_id = fields.Many2one("parking.section", ondelete="set null")
    company_id = fields.Many2one("res.company", ondelete="set null")

    def log_slot_historical(self, historical_type=""):
        if not historical_type:
            historical_type_mapping = {"1": "exit", "2": "entry"}

            historical_type = historical_type_mapping[self.state]

        self.env["parking.slot.historical"].create(
            {
                "slot_id": self.id,
                "partner_id": self.partner_id.id,
                "section_id": self.section_id.id,
                "historical_type": historical_type,
            }
        )

    def write(self, vals):
        res = super(ParkingSlot, self).write(vals)

        if vals.get("state"):
            self.log_slot_historical()

        return res
