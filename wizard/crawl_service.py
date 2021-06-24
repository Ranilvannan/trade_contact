from odoo import models, fields, api

CRAWL_TYPE = [("first_page", "First Page"), ("history", "History")]
SITE = [("sagmart", "Sagmart")]


class CrawlService(models.TransientModel):
    _name = "crawl.service"
    _description = "Crawl Service"

    site = fields.Selection(selection=SITE, string="Site", required=1)
    crawl_type = fields.Selection(selection=CRAWL_TYPE, string="Crawl Type", required=1)

    def trigger_crawl(self):
        if self.site == "sagmart":
            site_model = "sag.mart"

        if self.crawl_type == "first_page":
            self.data_crawl(site_model)
        elif self.crawl_type == "history":
            self.history_crawl(site_model)

    def data_crawl(self, site_model):
        domain = self.env[site_model]._domain_url
        obj = self.env[site_model].create({
            "domain": domain,
            "url": domain,
            "page": 1})

        obj.trigger_crawl()

    def history_crawl(self, site_model):
        domain = self.env[site_model]._domain_url
        history_obj = self.env["history.history"].search([("domain", "=", domain)])
        if history_obj:
            obj = self.env[site_model].create({
                "domain": domain,
                "url": history_obj.url,
                "page": 5})

            obj.trigger_crawl()
