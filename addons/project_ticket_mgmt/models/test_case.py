# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProjectTestCase(models.Model):
    _name = 'project.test.case'
    _description = 'Test Case'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Test Case ID',
        required=True,
        readonly=True,
        default='/',
        copy=False,
        index=True,
    )
    test_case_title = fields.Char(
        string='Test Case Title',
        required=True,
        tracking=True,
    )
    module = fields.Char(
        string='Module',
    )
    test_objective = fields.Html(
        string='Test Objective',
        sanitize_attributes=False,
    )
    pre_conditions = fields.Html(
        string='Pre Conditions',
        sanitize_attributes=False,
    )
    test_data = fields.Html(
        string='Test Data',
        sanitize_attributes=False,
    )
    test_steps = fields.Html(
        string='Test Steps',
        sanitize_attributes=False,
    )
    expected_result = fields.Html(
        string='Expected Result',
        sanitize_attributes=False,
    )
    actual_result = fields.Html(
        string='Actual Result',
        sanitize_attributes=False,
    )
    status = fields.Selection([
        ('draft', 'Draft'),
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('blocked', 'Blocked'),
        ('not_executed', 'Not Executed'),
    ], string='Status', default='draft', tracking=True, index=True)
    
    severity = fields.Selection([
        ('blocker', 'Blocker'),
        ('critical', 'Critical'),
        ('major', 'Major'),
        ('minor', 'Minor'),
        ('trivial', 'Trivial'),
    ], string='Severity', tracking=True, index=True)
    
    environment = fields.Selection([
        ('sandbox', 'Sandbox'),
        ('production', 'Production'),
        ('staging', 'Staging'),
        ('development', 'Development'),
    ], string='Environment', index=True)
    
    executed_date = fields.Datetime(
        string='Executed Date',
    )
    executed_by_id = fields.Many2one(
        'res.users',
        string='Executed By',
    )
    test_type = fields.Selection([
        ('smoke', 'Smoke'),
        ('uat', 'UAT'),
        ('regression', 'Regression'),
        ('integration', 'Integration'),
        ('system', 'System'),
        ('functional', 'Functional'),
    ], string='Test Type', index=True)
    
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        index=True,
    )
    test_plan_id = fields.Many2one(
        'project.test.plan',
        string='Test Plan',
        index=True,
    )
    test_scenario_id = fields.Many2one(
        'project.test.scenario',
        string='Test Scenario',
        index=True,
    )
    ticket_ids = fields.One2many(
        'project.ticket',
        'test_case_id',
        string='Tickets',
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', '/') == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('project.test.case.sequence') or '/'
        return super().create(vals_list)
