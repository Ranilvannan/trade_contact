from odoo import models, fields, api
from datetime import datetime


class SagMart(models.Model):
    _name = "sag.mart"
    _description = "Sagmart"
    _domain_host = "http://www.sagmart.com/"
    _domain_url = "http://www.sagmart.com/dealer-id{record_id}-vaigai-electronics-chennai"
    _info = "Sagmart"

    sequence = fields.Char(string="sequence", readonly=True)
    name = fields.Char(string="Name")
    address = fields.Text(string="Address")
    area = fields.Char(string="Area")
    state = fields.Char(string="state")
    pincode = fields.Char(string="Pincode")
    contact = fields.Char(string="Contact")
    landmark = fields.Char(string="Landmark")
    opening_hours = fields.Char(string="Opening Hours")
    opening_days = fields.Char(string="Opening Days")

    # Crawl Site
    url = fields.Char(string="URL")
    date = fields.Date(string="Date", default=datetime.now())
    is_valid = fields.Boolean(string="Is Valid", default=False)
    is_exported = fields.Boolean(string="Is Exported", default=False)

    def trigger_crawl(self):
        rec = self.env[""]
        print("ji")

    @api.model
    def create(self, vals):
        vals["sequence"] = self.env['ir.sequence'].next_by_code(self._name)
        return super(SagMart, self).create(vals)
