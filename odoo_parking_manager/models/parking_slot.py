from odoo import models, fields, api


class ParkingSlot(models.Model):
    _name = "parking.slot"
    _description = "Parking Slot"

    @api.model
    def get_slot_state_selection(self):
        return [("1", "Available"), ("2", "Taken"), ("3", "No Available")]

    name = fields.Char(index=True)
    takable = fields.Boolean
    distance_to_gate = fields.Float()
    distance_to_exit = fields.Float()
    exclusiveness = fields.Float()
    state = fields.Selection(selection="get_slot_state_selection")
    partner_id = fields.Many2one("res.partner", ondelete="set null", string="Occupant")
    vehicle_type = fields.Selection(
        selection=lambda self: self.env[
            "parking.vehicle"
        ]._get_vehicle_types_selection()
    )
    section_id = fields.Many2one("parking.section", ondelete="set null")
    owner_type = fields.Selection(
        selection=[
            ("pregnant", "Pregnant"),
            ("disabled", "Disabled"),
            ("normal", "Normal"),
        ],
        default="normal",
    )
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

    def log_slot_historical(self):
        val_list = []
        for record in self:
            val_list.append(
                {
                    "slot_id": record.id,
                    "partner_id": record.partner_id.id,
                    "section_id": record.section_id.id,
                    "historical_type": record.state,
                }
            )
        self.env["parking.slot.historical"].sudo().create(val_list)

    def write(self, vals):
        res = super(ParkingSlot, self).write(vals)

        if res and vals.get("state"):
            self.log_slot_historical()

        return res
