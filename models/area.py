from odoo import models, fields


class TradeArea(models.Model):
    _name = "trade.area"

    district_id = fields.Many2one(comodel_name="trade.district", string="District", required=True)
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Country", required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Country name must be unique !'),
        ('code_uniq', 'unique (name)', 'Country code must be unique !')
    ]