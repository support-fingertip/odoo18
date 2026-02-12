# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProjectTestPlan(models.Model):
    _name = 'project.test.plan'
    _description = 'Test Plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Test Plan ID',
        required=True,
        readonly=True,
        default='/',
        copy=False,
        index=True,
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        required=True,
        tracking=True,
        index=True,
    )
    project_org_id = fields.Char(
        string='Project ORG ID',
    )
    introduction = fields.Html(
        string='Introduction',
        sanitize_attributes=False,
    )
    test_objectives = fields.Html(
        string='Test Objectives',
        sanitize_attributes=False,
    )
    scope_in = fields.Html(
        string='In Scope',
        sanitize_attributes=False,
    )
    scope_out = fields.Html(
        string='Out of Scope',
        sanitize_attributes=False,
    )
    test_approach = fields.Html(
        string='Test Approach',
        sanitize_attributes=False,
    )
    test_environment = fields.Html(
        string='Test Environment',
        sanitize_attributes=False,
    )
    schedule_start_date = fields.Date(
        string='Start Date',
    )
    schedule_end_date = fields.Date(
        string='End Date',
    )
    entry_criteria = fields.Html(
        string='Entry Criteria',
        sanitize_attributes=False,
    )
    exit_criteria = fields.Html(
        string='Exit Criteria',
        sanitize_attributes=False,
    )
    test_manager_id = fields.Many2one(
        'res.users',
        string='Test Manager',
        tracking=True,
        index=True,
    )
    test_engineer_ids = fields.Many2many(
        'res.users',
        'test_plan_engineer_rel',
        'plan_id',
        'user_id',
        string='Test Engineers',
    )
    developer_ids = fields.Many2many(
        'res.users',
        'test_plan_developer_rel',
        'plan_id',
        'user_id',
        string='Developers',
    )
    defect_management = fields.Html(
        string='Defect Management',
        sanitize_attributes=False,
    )
    assumptions = fields.Html(
        string='Assumptions',
        sanitize_attributes=False,
    )
    approval_authority = fields.Char(
        string='Approval Authority',
    )
    sign_off_details = fields.Html(
        string='Sign Off Details',
        sanitize_attributes=False,
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('closed', 'Closed'),
    ], string='State', default='draft', required=True, tracking=True, index=True)
    
    scenario_ids = fields.One2many(
        'project.test.scenario',
        'test_plan_id',
        string='Test Scenarios',
    )
    test_case_ids = fields.One2many(
        'project.test.case',
        'test_plan_id',
        string='Test Cases',
    )
    ticket_ids = fields.One2many(
        'project.ticket',
        'test_plan_id',
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
                vals['name'] = self.env['ir.sequence'].next_by_code('project.test.plan.sequence') or '/'
        return super().create(vals_list)

    def action_submit_for_review(self):
        self.write({'state': 'in_review'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_close(self):
        self.write({'state': 'closed'})

    def action_reset_to_draft(self):
        self.write({'state': 'draft'})
