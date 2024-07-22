# -*- coding: utf-8 -*-
{
    'name': "Invoice Endpoint",
    'summary': """
        REST API Odoo Invoice""",

    'description': """
        Long description of module's purpose
    """,
    'author': "Vivy Cahyani",
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "account", "sale","base_rest_auth_api_key","base_rest_datamodel"],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
}
