# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import request as req

import base64


class MyModule(http.Controller):
    @http.route('/crud/create', auth='public')
    def crud_create(self, **kw):
        return req.render('om_hospital.create', {
            'aaa': 'aaa',
        })

    @http.route('/crud/create/process', auth='public', csrf=False)
    def crud_create_process(self, **kw):
        product_values = {
            'name': kw.get('name'),
            'list_price': float(kw.get('list_price'))
        }

        image_1920 = kw.get('image_1920')
        product_values['image_1920'] = base64.b64encode(image_1920.read())

        pd = req.env['product.template'].sudo().create(product_values)

        # print('pd : ', pd)
        return req.render('om_hospital.create_process', {
            'pd': pd,
        })

    @http.route('/crud/read_all', auth='public', csrf=False)
    def crud_read_all(self, **kw):
        products = req.env['product.template'].sudo().search([])
        # print('products', products)

        return req.render('om_hospital.read_all', {
            'products': products,
        })

    @http.route('/crud/read', auth='public', csrf=False)
    def crud_read(self, **kw):
        product_id = kw.get('product_id')

        product = req.env['product.template'].sudo().search([('id', '=', product_id)])
        print('product', product)

        return req.render('om_hospital.read', {
            'product': product,
        })

    @http.route('/crud/update', auth='public', csrf=False)
    def crud_update(self, **kw):
        product_id = kw.get('product_id')

        product = req.env['product.template'].sudo().search([('id', '=', product_id)])

        return req.render('om_hospital.update', {
            'product': product,
        })

    @http.route('/crud/update/process', auth='public', csrf=False)
    def crud_update_process(self, **kw):
        product_id = kw.get('product_id')

        product = req.env['product.template'].sudo().search([('id', '=', product_id)])

        update_products = {
            'name': kw.get('name'),
            'list_price': kw.get('list_price'),
        }

        image_1920 = kw.get('image_1920')
        if image_1920:
            update_products['image_1920'] = base64.b64encode(image_1920.read()).decode('utf-8')

        product_id = kw.get('product_id')
        if product_id:
            product = request.env['product.template'].browse(product_id)
            if product.exists():
                product.write(update_products)

        return req.render('om_hospital.update_process')

    @http.route('/crud/delete', auth='public', csrf=False)
    def crud_delete(self, **kw):
        product_id = kw.get('product_id')
        product = req.env['product.template'].sudo().search([('id', '=', product_id)])

        if product:
            product.unlink()

        return req.render('om_hospital.main_page')

    @http.route('/home', auth='public', csrf=False)
    def home(self, **kw):
        product = req.env['product.template'].sudo().search([('id', '=', 32)])

        return req.render('om_hospital.home', {
            'product': product,
        })
