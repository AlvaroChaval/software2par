from odoo import models, fields

class School(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char(string='School Name', required=True)
    description = fields.Char(string='School Description', required=True)
    address = fields.Char(string='School Address', required=True)
    cellphone = fields.Char(string='School Cellphone', required=True)
    email = fields.Char(string='School Email', required=True)

class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Classroom'

    name = fields.Char(string='Classroom Name', required=True)
    capacity = fields.Integer(string='Capacity')

class Course(models.Model):
    _name = 'school.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    parallel = fields.Char(string='Course Parallel')
    level = fields.Char(string='Course Level')
    description = fields.Text(string='Course Description')

class Cycle(models.Model):
    _name = 'school.cycle'
    _description = 'Cycle'

    name = fields.Char(string='Cycle Name', required=True)
    description = fields.Char(string='Cycle Description')    
    duration = fields.Selection([('bimester', 'Bimester'), ('trimester', 'Trimester')], string='Type')

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    description = fields.Char(string='Subject Description')
