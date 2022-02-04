# -*- coding: utf-8 -*-
{
    'name': "Invoicing Fixed Discount|Invoice Fixed Discount|Invoice Discount|"
            "Sales Fixed Discount|Sale Fixed Discount|Sale Discount"
            "|Fixed Discount Amount On Sale Order and Invoice Lines",
    'summary': """
        Set a fixed discount amount on Sales and Invoicing lines
        """,

    'description': """
        Adding a new custom fixed discount by amount field on Sale Order Line and Invoice Line. If you add a value by
        percentage it will automatically calculate the fixed amount for it, and vice versa.
    """,

    'images': ["static/description/main_banner.png"],
    'author': "Sayed Hassan",
    'version': '14.0.02',
    'license': "AGPL-3",
    'price': '6.00',
    'currency': 'USD',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ]
}
