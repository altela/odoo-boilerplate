# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Pre Init Check Boilerplate',
    'author': 'Altela Eleviansyah Pramardhika',
    'version': '12.0.1.0.0',
    'summary': 'Odoo Module Pre Init Check Boilerplate Example',
    'license': 'OPL-1',
    'sequence': 1,
    'description': """Odoo Module Pre Init Check Boilerplate Example""",
    'category': 'Sales',
    'website': 'https://altela.my.id',
    'price':'0',
    'currency':'USD',
    'depends': [
        'sale_management',
        'stock',
        'account',
    ],
    'data': [
    ],
    'images': [
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': 'm_pre_init_check',
}
