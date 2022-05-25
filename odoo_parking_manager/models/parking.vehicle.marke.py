from odoo import models, fields


class ParkingVehicleMarke(models.Model):
    _name = "parking.vehicle.marke"
    _description = "Parking Vehicle Marke"
    name = fields.Char(50, True, index=True)
