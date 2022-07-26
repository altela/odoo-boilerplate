# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Inherit Res Config Settings',
    'author': 'Altela Softwares',
    'version': '15.0.1.0.0',
    'summary': 'Inherit res.config.settings',
    'license': 'GPL-3',
    'sequence': 1,
    'description': """Inherit res.config.settings""",
    'category': 'Inventory',
    'website': 'https://www.altela.net',
    'depends': [
        'stock',
        'mail',
    ],
    'images': [
        'static/description/assets/banner.gif',
    ],
    'data': [
        'views/res_config_settings.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
