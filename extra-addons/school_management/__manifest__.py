{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manage school infrastructure, schedules, teachers, students, payments, grades, and reports',
    'description': """
        This module allows you to manage the entire infrastructure of a school including:
        - Classrooms
        - Courses
        - Cycles (Bimester, Trimester, etc.)
        - Schedules
        - Subjects
        - Parallels
        - Teacher assignments and loads
        - Student enrollments
        - Payment plans and payments
        - Grades and report cards
        - Necessary reports
        - Payment receipts for accounting
    """,
    'author': 'sw1',
    'website': 'http://www.yourwebsite.com',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/school_management_groups.xml',
        'security/school_management_security.xml',
        'views/school_management_menus.xml',
        'views/school_infrastructure_views.xml',
        'views/school_schedule_views.xml',
        'views/teacher_management_views.xml',
        'views/student_management_views.xml',
        'views/payment_management_views.xml',
        'views/grades_management_views.xml',        
        'data/school_infrastructure_data.xml',
        'data/school_infrastructure_demo.xml',     
    ],
    'demo': [
        'data/school_infrastructure_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
