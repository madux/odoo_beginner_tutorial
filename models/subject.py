from odoo import models, fields, api, _
from datetime import datetime, date 

class SubjectModel(models.Model):
    _name = 'subject.model'
    _description = 'This is a table for holding subject'
    _order = 'id desc'

    name = fields.Char(string='Course Name')
    duration_of_study = fields.Integer(string='Course Duration')