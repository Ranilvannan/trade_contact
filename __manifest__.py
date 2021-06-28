# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Trade Contact',
    'version': '1.1',
    'summary': 'Trade Contact',
    'sequence': 18,
    'description': 'Trade Contact',
    'category': 'New',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'web', 'mail'],
    'data': [
        'data/trade_contact_data.xml',
        'data/trade_country_data.xml',
        'security/trade_contact_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/sagmart_view.xml',
        'views/history_view.xml',
        'views/country_view.xml',
        'views/state_view.xml',
        'views/district_view.xml',
        'views/area_view.xml',
        'wizard/crawl_service_view.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
