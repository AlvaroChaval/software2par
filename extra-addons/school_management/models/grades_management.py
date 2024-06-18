from odoo import models, fields

class Grade(models.Model):
    _name = 'school.grade'
    _description = 'school.grade'

    grade = fields.Float(string='Grade', required=True)
    year = fields.Integer(string='Year', required=True)
    student_name = fields.Many2one('school.student', string='Student', required=True)
    subject_name = fields.Many2one('school.subject', string='Subject', required=True)
    cycle_id = fields.Many2one('school.cycle', string='Cycle', required=True)

    # report_id = fields.Many2one('school.grade.report', string='Grade Report', ondelete='cascade')  # Añadir este campo para GradeReport

    # report_card_id = fields.Many2one('school.report.card', string='Report Card', ondelete='cascade')  # Campo existente para ReportCard

# class ReportCard(models.Model):
#     _name = 'school.report.card'
#     _description = 'Report Card'

#     student_id = fields.Many2one('school.student', string='Student', required=True)
#     cycle_id = fields.Many2one('school.cycle', string='Cycle', required=True)
#     grade_ids = fields.One2many('school.grade', 'report_card_id', string='Grades')

# class GradeReport(models.Model):
#     _name = 'school.grade.report'
#     _description = 'Grade Report'

#     student_id = fields.Many2one('school.student', string='Student', required=True)
#     cycle_id = fields.Many2one('school.cycle', string='Cycle', required=True)
#     grade_ids = fields.One2many('school.grade', 'report_id', string='Grades')  # Relación con Grade
