from odoo import models, fields, api, _
from datetime import datetime, date 

class TeacherModel(models.Model):
    _name = 'teacher.model'
    _description = 'This is a table for holding teacher'
    _order = 'id desc'

    name = fields.Char(string='Name')
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    subject_ids = fields.Many2one(
        'subject.model',
        string="Subjects",
        required=False,
        readonly=False,
        )