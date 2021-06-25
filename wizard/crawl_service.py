from odoo import models, fields, api

SITE = [("sag.mart", "Sagmart")]


class CrawlService(models.TransientModel):
    _name = "crawl.service"
    _description = "Crawl Service"

    site = fields.Selection(selection=SITE, string="Site", required=True)

    def trigger_crawl(self):
        self.env[self.site].trigger_crawl()
