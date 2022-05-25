from odoo import fields, models


class ParkingSection(models.Model):
    _name = 'parking.section'

    name = fields.Char(30, True, index=True, required=True)
    parent_id = fields.Many2one()
    children_ids = fields.One2many()
    slot_ids = fields.One2many()

