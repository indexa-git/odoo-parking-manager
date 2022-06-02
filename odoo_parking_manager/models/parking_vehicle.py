from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ParkingVehicle(models.Model):
    _name = "parking.vehicle"
    _description = "Parking Vehicle"

    name = fields.Char(compute="_compute_name_vehicle", store=True, index=True)
    year = fields.Integer()
    maker_id = fields.Many2one("parking.vehicle.maker", required=True)
    model = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Owner")
    plate = fields.Char(size=30, required=True)
    color = fields.Char(size=10)

    vehicle_type = fields.Selection(selection="vehicle_types")

    @api.model
    def vehicle_types(self):
        return [
            ("bicycle", "Bicycle"),
            ("motorcycle", "Motorcycle"),
            ("Car", "Car"),
            ("jeepeta", "Jeepeta"),
        ]

    @api.depends("maker_id", "model", "plate")
    def _compute_name_vehicle(self):
        for record in self:
            record.name = " ".join(
                [record.maker_id.name or " ", record.model or " ", record.plate or " "]
            ).strip()

    _sql_constraints = [
        (
            "plate_unique",
            "unique(plate)",
            "Operacion cancelada. Existe una placa con esta combinacion",
        )
    ]
