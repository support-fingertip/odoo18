# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Ticket Management',
    'version': '1.0',
    'category': 'Services/Project',
    'sequence': 100,
    'summary': 'QA Testing and Ticket/Case Management System',
    'description': """
        Comprehensive Ticket (Case) Management System for Quality Assurance and Testing.
        Includes Test Plans, Test Scenarios, Test Cases, and Bug/Defect Tracking.
    """,
    'depends': [
        'project',
        'mail',
    ],
    'data': [
        'security/ticket_security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/test_plan_views.xml',
        'views/test_scenario_views.xml',
        'views/test_case_views.xml',
        'views/ticket_views.xml',
        'report/ticket_report_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
