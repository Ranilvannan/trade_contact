from odoo import models, fields


class TradeDistrict(models.Model):
    _name = "trade.district"

    state_id = fields.Many2one(comodel_name="trade.country.state", string="State", required=True)
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Country", required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Country name must be unique !'),
        ('code_uniq', 'unique (name)', 'Country code must be unique !')
    ]