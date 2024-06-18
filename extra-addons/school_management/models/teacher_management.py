from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'school.teacher'

    name = fields.Char(string='Teacher Name', required=True)
    description = fields.Char(string='Teacher Description', required=True)
    title = fields.Char(string='Teacher Title', required=True)
    ci = fields.Char(string='Teacher CI', required=True)
    cellphone = fields.Char(string='Teacher Cellphone', required=True)
    hire_date = fields.Char(string='Teacher Hire Date', required=True)

class TeachingLoad(models.Model):
    _name = 'school.teaching.load'
    _description = 'Teaching Load'

    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    hours_per_week = fields.Integer(string='Hours per Week', required=True)
    hours_total = fields.Integer(string='Hours total', required=True)    
    schedule_id = fields.Many2one('school.schedule', string='Schedule')
