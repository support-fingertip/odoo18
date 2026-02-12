# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProjectTestScenario(models.Model):
    _name = 'project.test.scenario'
    _description = 'Test Scenario'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Test Scenario ID',
        required=True,
        readonly=True,
        default='/',
        copy=False,
        index=True,
    )
    date = fields.Date(
        string='Date',
        default=fields.Date.context_today,
    )
    test_scenario_id_display = fields.Char(
        string='Test Scenario ID',
        compute='_compute_test_scenario_id_display',
        store=True,
    )
    module = fields.Char(
        string='Module',
    )
    description = fields.Html(
        string='Description',
        sanitize_attributes=False,
    )
    status = fields.Selection([
        ('draft', 'Draft'),
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('invalid', 'Invalid'),
    ], string='Status', default='draft', tracking=True, index=True)
    
    comments = fields.Html(
        string='Comments',
        sanitize_attributes=False,
    )
    created_by_id = fields.Many2one(
        'res.users',
        string='Created By',
        default=lambda self: self.env.user,
        readonly=True,
    )
    reviewed_by_id = fields.Many2one(
        'res.users',
        string='Reviewed By',
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        required=True,
        index=True,
    )
    test_plan_id = fields.Many2one(
        'project.test.plan',
        string='Test Plan',
        index=True,
    )
    test_case_ids = fields.One2many(
        'project.test.case',
        'test_scenario_id',
        string='Test Cases',
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
    )

    @api.depends('name')
    def _compute_test_scenario_id_display(self):
        for record in self:
            record.test_scenario_id_display = record.name

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', '/') == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('project.test.scenario.sequence') or '/'
        return super().create(vals_list)
