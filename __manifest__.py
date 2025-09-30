# -*- coding: utf-8 -*-
{
    'name': 'Partner Doctor Address',
    'version': '1.0',
    'summary': 'Adds Doctor Address type to contacts',
    'description': '''
	This module extends the res.partner model to include
	a new contact type (Doctor Address) and includes a test view
	to verify the module structure loads correctly.
    ''',
    'author': 'David Aciego',
    'website': 'https://zeoscientifix.com',
    'category': 'Contacts',
    'depends': [
	'base'
    ],
    'data': [
    
	    'views/res_partner_views.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
