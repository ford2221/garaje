# -*- coding: utf-8 -*-
# from odoo import http


# class ./addons/garaje(http.Controller):
#     @http.route('/./addons/garaje/./addons/garaje/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./addons/garaje/./addons/garaje/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./addons/garaje.listing', {
#             'root': '/./addons/garaje/./addons/garaje',
#             'objects': http.request.env['./addons/garaje../addons/garaje'].search([]),
#         })

#     @http.route('/./addons/garaje/./addons/garaje/objects/<model("./addons/garaje../addons/garaje"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./addons/garaje.object', {
#             'object': obj
#         })
