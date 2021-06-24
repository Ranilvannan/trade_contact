from odoo import models, fields


class TradeContact(models.Model):
    _name = "trade.contact"
    _description = "Trade Contact"

    sequence = fields.Char(string="Sequence", readonly=True)
    name = fields.Char(string="Name")
