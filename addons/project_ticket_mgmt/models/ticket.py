# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProjectTicket(models.Model):
    _name = 'project.ticket'
    _description = 'Ticket/Bug'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority asc, create_date desc'

    name = fields.Char(
        string='Bug ID',
        required=True,
        readonly=True,
        default='/',
        copy=False,
        index=True,
    )
    title = fields.Char(
        string='Title',
        required=True,
        tracking=True,
        index='trigram',
    )
    description = fields.Html(
        string='Description',
        sanitize_attributes=False,
    )
    steps_to_reproduce = fields.Html(
        string='Steps to Reproduce',
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
    environment = fields.Selection([
        ('sandbox', 'Sandbox'),
        ('production', 'Production'),
        ('staging', 'Staging'),
        ('development', 'Development'),
    ], string='Environment', index=True)
    
    device = fields.Selection([
        ('mobile', 'Mobile'),
        ('desktop', 'Desktop'),
        ('tablet', 'Tablet'),
        ('all', 'All'),
    ], string='Device')
    
    severity = fields.Selection([
        ('blocker', 'Blocker'),
        ('critical', 'Critical'),
        ('major', 'Major'),
        ('minor', 'Minor'),
        ('trivial', 'Trivial'),
    ], string='Severity', tracking=True, index=True)
    
    priority = fields.Selection([
        ('p0', 'P0'),
        ('p1', 'P1'),
        ('p2', 'P2'),
        ('p3', 'P3'),
        ('p4', 'P4'),
    ], string='Priority', tracking=True, index=True)
    
    state = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('fixed', 'Fixed'),
        ('closed', 'Closed'),
        ('reopened', 'Re-opened'),
        ('deferred', 'Deferred'),
    ], string='State', default='open', required=True, tracking=True, index=True)
    
    reproducibility = fields.Selection([
        ('always', 'Always'),
        ('sometimes', 'Sometimes'),
        ('rare', 'Rare'),
        ('unable', 'Unable to Reproduce'),
    ], string='Reproducibility')
    
    evidence_ids = fields.Many2many(
        'ir.attachment',
        'project_ticket_attachment_rel',
        'ticket_id',
        'attachment_id',
        string='Evidence',
    )
    reporter_id = fields.Many2one(
        'res.users',
        string='Reporter',
        default=lambda self: self.env.user,
        required=True,
        index=True,
    )
    reported_date = fields.Datetime(
        string='Reported Date',
        default=fields.Datetime.now,
        required=True,
    )
    assigned_to_id = fields.Many2one(
        'res.users',
        string='Assigned To',
        tracking=True,
        index=True,
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        required=True,
        tracking=True,
        index=True,
    )
    task_id = fields.Many2one(
        'project.task',
        string='Related Task',
        index=True,
    )
    test_plan_id = fields.Many2one(
        'project.test.plan',
        string='Test Plan',
        index=True,
    )
    test_case_id = fields.Many2one(
        'project.test.case',
        string='Test Case',
        index=True,
    )
    resolution = fields.Html(
        string='Resolution',
        sanitize_attributes=False,
    )
    fixed_date = fields.Datetime(
        string='Fixed Date',
    )
    fixed_by_id = fields.Many2one(
        'res.users',
        string='Fixed By',
    )
    verified_by_id = fields.Many2one(
        'res.users',
        string='Verified By',
    )
    verified_date = fields.Datetime(
        string='Verified Date',
    )
    tag_ids = fields.Many2many(
        'project.tags',
        string='Tags',
    )
    color = fields.Integer(
        string='Color Index',
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
                vals['name'] = self.env['ir.sequence'].next_by_code('project.ticket.sequence') or '/'
        return super().create(vals_list)

    def action_start_progress(self):
        self.write({'state': 'in_progress'})

    def action_mark_fixed(self):
        self.write({
            'state': 'fixed',
            'fixed_date': fields.Datetime.now(),
            'fixed_by_id': self.env.user.id,
        })

    def action_close(self):
        self.write({'state': 'closed'})

    def action_reopen(self):
        self.write({'state': 'reopened'})

    def action_defer(self):
        self.write({'state': 'deferred'})
