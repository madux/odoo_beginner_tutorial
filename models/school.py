from odoo import models, fields, api, _
from datetime import datetime, date 
from odoo.exceptions import ValidationError
from math import sin 

class SchoolModel(models.Model):
    _name = 'school.model'
    _description = 'This is a table for holding schools'
    _order = 'id desc'

    name = fields.Char(string='Name of school')
    address = fields.Char(string="Address", required=False)
    phone_number = fields.Char(string="Phone", required=True)
    email = fields.Char(
        string="Email",
        required=True,
        )
    class_ids = fields.Many2many(
        'class.model',
        string="Classes",
        readonly=False,
        )
    date_of_creation = fields.Date(
        string="Date of Creation",
        required=False,
        default=fields.Date.today())

    def action_confirm(self):
        raise ValidationError("There is no function to run")






