from odoo import models

class GradesReport(models.AbstractModel):
    _name = 'report.school_management.grades_report_template'
    _description = 'Grades Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['school.grade'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'school.grade',
            'docs': docs,
            'data': data,
        }
