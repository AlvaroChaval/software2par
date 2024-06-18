from odoo import models, fields

class PaymentPlan(models.Model):
    _name = 'school.paymentplan'
    _description = 'school.paymentPlan'

    name = fields.Char(string='Payment Plan Name', required=True)
    description = fields.Char(string='Payment Plan Description', required=True)
    amount_plan = fields.Integer(string='Payment Plan Amount', required=True)
    
class StudentPlan(models.Model):
    _name = 'school.studentplan'
    _description = 'school.studentplan'

    student_name = fields.Many2one('school.student', string='Student', required=True)
    payment_plan = fields.Many2one('school.payment.plan', string='Payment Plan', required=True)
    date_save = fields.Date()
    
class Payments(models.Model):
    _name = 'school.payments'
    _description = 'school.payments'

    date_payment = fields.Date(string='Date Payment', required=True)
    total_amount = fields.Float(string='Total Amount', required=True)
    student_name = fields.Many2one('school.student', string='Student Name', required=True)
    payment_plan_name = fields.Many2one('school.paymentplan', string='Payment Plan Name', required=True)