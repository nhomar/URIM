# -*- coding: utf-8 -*-
# from odoo import http


# class SalesInvoicingFixedDiscount(http.Controller):
#     @http.route('/sales_invoicing_fixed_discount/sales_invoicing_fixed_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_invoicing_fixed_discount/sales_invoicing_fixed_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_invoicing_fixed_discount.listing', {
#             'root': '/sales_invoicing_fixed_discount/sales_invoicing_fixed_discount',
#             'objects': http.request.env['sales_invoicing_fixed_discount.sales_invoicing_fixed_discount'].search([]),
#         })

#     @http.route('/sales_invoicing_fixed_discount/sales_invoicing_fixed_discount/objects/<model("sales_invoicing_fixed_discount.sales_invoicing_fixed_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_invoicing_fixed_discount.object', {
#             'object': obj
#         })
