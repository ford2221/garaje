# -*- coding: utf-8 -*-
{
    'name': "The Garage",

    'summary': """
        The garage app
    """,

    'description': """
        This app is about an garage to make something
    """,

    'author': "Ford Joseph",
    'website': "http://www.ford.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/garaje_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/garaje_aparcamiento_report.xml',
        'data/garaje_data.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    "application": True
}
