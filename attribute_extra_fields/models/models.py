# -*- coding: utf-8 -*-

from odoo import models, fields


class attribute_extra_fields(models.Model):
    _name = 'product.attribute'
    _inherit = 'product.attribute'

    option_id = fields.Integer('Option ID')
  

    _sql_constraints = [
        ('option_id_uniq', 'unique (option_id)', "A option_id already exists with this ID . ID must be unique!"),
    ]

	
class attribute_value_extra_fields(models.Model):
    _name = 'product.attribute.value'
    _inherit = 'product.attribute.value'

    option_value_id = fields.Integer('Option Value ID')
  

    _sql_constraints = [
        ('option_value_id_uniq', 'unique (option_value_id)', "A option_value_id already exists with this ID . ID must be unique!"),
    ]
