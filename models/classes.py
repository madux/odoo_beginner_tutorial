from odoo import models, fields, api, _
from datetime import datetime, date 

class ClassModel(models.Model):
    _name = 'class.model'
    _description = 'This is a table for holding classes'
    _order = 'id desc'

    name = fields.Char(string='Name')
    maximum_number_of_pupil = fields.Char(string="Address", required=False)
    head_teacher_phone = fields.Char(string="Phone", required=True)
    head_teacher = fields.Many2one(
        'teacher.model',
        string="Head Teacher",
        required=False,
        readonly=False,
        )
    
    class_prefect = fields.Many2one(
        'students.model',
        string="Prefect",
        required=False,
        readonly=False,
        )






