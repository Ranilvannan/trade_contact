from odoo import models, fields, exceptions


class History(models.Model):
    _name = "history.history"
    _description = "History"
    _rec_name = "site"

    site = fields.Char(string="Site")
    url = fields.Char(string="URL")
