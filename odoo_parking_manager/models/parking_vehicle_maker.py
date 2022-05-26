from odoo import models, fields


class ParkingVehicleMaker(models.Model):
    _name = "parking.vehicle.maker"
    _description = "Parking Vehicle Maker"

    name = fields.Char(size=50, required=True, index=True)
