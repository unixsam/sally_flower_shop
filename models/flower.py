from odoo import models, fields


class Flower(models.Model):
    _name = 'sally.flower'
    _description = 'sally.flower'

    name = fields.Char()
    scientific_name = fields.Char()
    season_start = fields.Date()
    season_end = fields.Date()
    Irrigation_frequency = fields.Integer(help="Number of days")
    Irrigation_amount = fields.Integer(help="In Milliliters")
