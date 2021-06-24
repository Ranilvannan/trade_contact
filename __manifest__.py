# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Trade Contact',
    'version': '1.1',
    'summary': 'Trade Contact',
    'sequence': 15,
    'description': 'Trade Contact',
    'category': 'New',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'web', 'mail'],
    'data': [
        'data/trade_contact.xml',
        'data/category.xml',
        'security/trade_contact_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}