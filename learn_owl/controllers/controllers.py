# -*- coding: utf-8 -*-
# from odoo import http


# class LearnOwl(http.Controller):
#     @http.route('/learn_owl/learn_owl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/learn_owl/learn_owl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('learn_owl.listing', {
#             'root': '/learn_owl/learn_owl',
#             'objects': http.request.env['learn_owl.learn_owl'].search([]),
#         })

#     @http.route('/learn_owl/learn_owl/objects/<model("learn_owl.learn_owl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('learn_owl.object', {
#             'object': obj
#         })

