# -*- coding: utf-8 -*-

# class ProductExtraFields(http.Controller):
#     @http.route('/product_extra_fields/product_extra_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_extra_fields/product_extra_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_extra_fields.listing', {
#             'root': '/product_extra_fields/product_extra_fields',
#             'objects': http.request.env['product_extra_fields.product_extra_fields'].search([]),
#         })

#     @http.route('/product_extra_fields/product_extra_fields/objects/<model("product_extra_fields.product_extra_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_extra_fields.object', {
#             'object': obj
#         })
