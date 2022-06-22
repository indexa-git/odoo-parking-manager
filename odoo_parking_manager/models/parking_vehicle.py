from odoo import models, fields, api


class ParkingVehicle(models.Model):
    _name = "parking.vehicle"
    _description = "Parking Vehicle"

    @api.model
    def _get_vehicle_types_selection(self):
        return [
            ("bicycle", "Bicycle"),
            ("motorcycle", "Motorcycle"),
            ("car", "Car"),
            ("jeepeta", "Jeepeta"),
        ]

    name = fields.Char(compute="_compute_name_vehicle", store=True, index=True)
    year = fields.Integer()
    maker_id = fields.Many2one("parking.vehicle.maker", required=True)
    model = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Owner")
    plate = fields.Char(required=True)
    color = fields.Char()
    vehicle_type = fields.Selection(selection="_get_vehicle_types_selection")
    company_id = fields.Many2one(
        "res.company",
        required=True,
        string="Company",
        default=lambda self: self.env.company,
    )

    _sql_constraints = [
        (
            "plate_unique",
            "unique(plate)",
            "Operation cancelled. There is a plate with this combination",
        )
    ]

    @api.depends("maker_id", "model", "plate")
    def _compute_name_vehicle(self):
        for record in self:
            record.name = " ".join(
                [record.maker_id.name or " ", record.model or " ", record.plate or " "]
            ).strip()
