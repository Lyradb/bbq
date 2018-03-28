# -*- coding: utf-8 -*-
from odoo import http

# class /dev/bbq(http.Controller):
#     @http.route('//dev/bbq//dev/bbq/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//dev/bbq//dev/bbq/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/dev/bbq.listing', {
#             'root': '//dev/bbq//dev/bbq',
#             'objects': http.request.env['/dev/bbq./dev/bbq'].search([]),
#         })

#     @http.route('//dev/bbq//dev/bbq/objects/<model("/dev/bbq./dev/bbq"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/dev/bbq.object', {
#             'object': obj
#         })