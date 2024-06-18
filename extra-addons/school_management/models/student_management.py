from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    cellphone = fields.Char(string='Cellphone')
    ci = fields.Char(string='CI')
    tutor_principal = fields.Many2one('school.tutor', string='Tutor')
    tutor_secundary = fields.Many2one('school.tutor', string='Tutor Secundario')
    enrollment_ids = fields.One2many('school.enrollment', 'student_id', string='Enrollments')

class Tutor(models.Model):
    _name = 'school.tutor'
    _description = 'Tutor'

    name = fields.Char(string='Tutor Name', required=True)
    last_name = fields.Char(string='Tutor Last Name', required=True)
    cellphone = fields.Char(string='Tutor cellphone', required=True)
    email = fields.Char(string='Tutor Email', required=True)

class Enrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    date_of_enrollment = fields.Date(string='Date of Enrollment', required=True)
