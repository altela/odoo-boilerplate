# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Create Wizard Boilerplate',
    'author': 'Altela Eleviansyah Pramardhika',
    'version': '12.0.1.0.0',
    'summary': 'Create Wizard Boilerplate',
    'license': 'LGPL-3',
    'sequence': 1,
    'description': """Create Wizard Boilerplate""",
    'category': 'Inventory',
    'website': 'https://altela.my.id',
    'price':'0',
    'currency':'USD',
    'depends': [
        'stock',
        'account',
    ],
    'data': [
        'views/wizard_boilerplate.xml',
        'wizard/wizard_boilerplate_wiz_views.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
