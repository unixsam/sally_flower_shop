from odoo import models, fields


class FlowerWater(models.Model):
    _name = "flower.water"
    _description = "Flower Irrigation"
    _order = "date"

    serial_id = fields.Many2one("stock.lot")
    date = fields.Date(string="Irrigation Date",default=fields.Date.context_today)
    flower_name = fields.Char(string="Flower Name", related='serial_id.product_id.flower_id.name', store=True)
