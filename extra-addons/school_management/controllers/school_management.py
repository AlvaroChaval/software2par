from odoo import http
from odoo.http import request

class SchoolManagement(http.Controller):

    @http.route('/school_management', auth='public')
    def index(self, **kw):
        return "Welcome to School Management"

    @http.route('/school_management/teachers', auth='public', type='json')
    def list_teachers(self, **kwargs):
        teachers = request.env['school.teacher'].search([])
        return [{'name': teacher.name, 'subjects': teacher.subject_ids.mapped('name')} for teacher in teachers]
