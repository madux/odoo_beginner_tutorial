# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Odoo Beginners Tutorial',
    'version' : '0.1',
    'sequence': 10,
    'summary' : 'Odoo technical tutorial',
    'description' : """Odoo technical tutorial""",
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/school_view.xml',
    ],

    'installable': True,
    'application': True,
}
