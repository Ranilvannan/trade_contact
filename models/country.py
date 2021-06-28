from odoo import models, fields


class Country(models.Model):
    _name = "trade.country"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Country", required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Country name must be unique !'),
        ('code_uniq', 'unique (name)', 'Country code must be unique !')
    ]