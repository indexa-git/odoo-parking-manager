from odoo import fields, models


class ParkingSection(models.Model):
    _name = "parking.section"
    _description = "Parking Section"

    name = fields.Char(size=50, index=True, required=True)
    description = fields.Text()
    parent_id = fields.Many2one("parking.section", ondelete="set null")
    children_ids = fields.One2many("parking.section", "parent_id", "Child Sections")
    slot_ids = fields.One2many("parking.slot", "section_id")
