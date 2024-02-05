from odoo import models, fields, api


class StockLot(models.Model):
    _inherit = 'stock.lot'

    water_ids = fields.One2many("flower.water", "serial_id")
    is_flower=fields.Boolean(related='product_id.is_flower')
    
    def action_water_flower(self):
        flowers = self.filtered(lambda rec: rec.is_flower)
        for record in flowers:
            if record.water_ids:
                last_watered_date = record.water_ids[0].date
                frequency = record.product_id.flower_id.Irrigation_frequency
                today = fields.Date.today()
                if (today - last_watered_date).days < frequency:
                    continue
            self.env["flower.water"].create({
                "serial_id": record.id,
            })

    def action_open_Irrigation_times(self):
        action = {
            'name': 'Irrigation Times',
            'type': 'ir.actions.act_window',
            'res_model': 'flower.water',
            'view_mode': 'tree,form',
            'domain': [('serial_id', '=', self.id)],
            'target': 'current',
        }
        return action

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product = self.env["product.product"].browse(vals["product_id"])
            if product.sequence_id:
                vals["name"] = product.sequence_id.next_by_id()
        return super().create(vals_list)
