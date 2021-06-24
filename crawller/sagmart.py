from odoo import models, fields


class SagMart(models.Model):
    _name = "sag.mart"
    _description = "Sagmart"

    sequence = fields.Char(string="sequence", readonly=True)
