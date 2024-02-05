{
    'name': "Flowers Shop",

    'summary': "BTCO Flowers Shop Exercises",

    'author': "Digital Roots",
    'website': "https://digitalroots.com.kw",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','product','website_sale','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_views.xml',
        'views/stock_lot_view.xml',
        'views/actions.xml',
        'data/paperformat.xml',
        'reports/flower_sale_order_views.xml',
        'data/irrigation_scheduled_action.xml',
        'data/groups.xml',
        'data/warehouse_actions.xml',
        'security/sally_shop_rules.xml',
        'views/weather_api_system_parameter.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
