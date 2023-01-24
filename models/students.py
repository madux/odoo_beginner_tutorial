from odoo import models, fields, api, _
from datetime import datetime, date 

class StudentModel(models.Model):
    _name = 'students.model'
    _description = 'This is a table for holding students'
    _order = 'id desc'

    name = fields.Char(string='Name')
    address = fields.Char(string="Address", required=False)
    phone_number = fields.Char(string="Phone", required=True)
    email = fields.Char(
        string="Email",
        required=True,
        )
    date_of_birth = fields.Date(
        string="Date of Birth",
        required=False,
        default=fields.Date.today())

    subject_ids = fields.Many2many(
        'subject.model',
        string="Subject",
        required=False,
        readonly=False,
        )






