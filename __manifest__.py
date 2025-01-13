{
    'name': 'Order Sale Discount',
    'version': '1.0',
    'summary': 'Module for managing sales discount',
    'description': 'This module helps in managing the sales operations.',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'sale','product'],
    'data': [
        'views/sale_order_discount_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}