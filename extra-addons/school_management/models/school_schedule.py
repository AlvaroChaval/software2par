from odoo import models, fields

class Schedule(models.Model):
    _name = 'school.schedule'
    _description = 'Schedule'
    
    teacher_id = fields.Many2one('school.teaching.load', string='Teaching Load', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Classroom', required=True)
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    day_of_week = fields.Selection([
        ('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'),
        ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')],
        string='Day of the Week', required=True)
    
class ScheculeCourse(models.Model):
    _name = 'school.schedule.course'
    _description = 'Schedule Course'

    year = fields.Integer(string='Year', required=True)
    schedule_id = fields.Many2one('school.schedule', string='Schedule', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)