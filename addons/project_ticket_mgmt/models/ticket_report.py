# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools


class ProjectTicketReport(models.Model):
    _name = 'project.ticket.report'
    _description = 'Ticket Analysis Report'
    _auto = False
    _rec_name = 'id'
    _order = 'create_date desc'

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Bug ID', readonly=True)
    title = fields.Char(string='Title', readonly=True)
    project_id = fields.Many2one('project.project', string='Project', readonly=True)
    severity = fields.Selection([
        ('blocker', 'Blocker'),
        ('critical', 'Critical'),
        ('major', 'Major'),
        ('minor', 'Minor'),
        ('trivial', 'Trivial'),
    ], string='Severity', readonly=True)
    priority = fields.Selection([
        ('p0', 'P0'),
        ('p1', 'P1'),
        ('p2', 'P2'),
        ('p3', 'P3'),
        ('p4', 'P4'),
    ], string='Priority', readonly=True)
    state = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('fixed', 'Fixed'),
        ('closed', 'Closed'),
        ('reopened', 'Re-opened'),
        ('deferred', 'Deferred'),
    ], string='State', readonly=True)
    environment = fields.Selection([
        ('sandbox', 'Sandbox'),
        ('production', 'Production'),
        ('staging', 'Staging'),
        ('development', 'Development'),
    ], string='Environment', readonly=True)
    reporter_id = fields.Many2one('res.users', string='Reporter', readonly=True)
    assigned_to_id = fields.Many2one('res.users', string='Assigned To', readonly=True)
    create_date = fields.Datetime(string='Created Date', readonly=True)
    reported_date = fields.Datetime(string='Reported Date', readonly=True)
    fixed_date = fields.Datetime(string='Fixed Date', readonly=True)
    verified_date = fields.Datetime(string='Verified Date', readonly=True)
    days_to_fix = fields.Float(string='Days to Fix', readonly=True, group_operator='avg')
    ticket_count = fields.Integer(string='# Tickets', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    t.id as id,
                    t.name as name,
                    t.title as title,
                    t.project_id as project_id,
                    t.severity as severity,
                    t.priority as priority,
                    t.state as state,
                    t.environment as environment,
                    t.reporter_id as reporter_id,
                    t.assigned_to_id as assigned_to_id,
                    t.create_date as create_date,
                    t.reported_date as reported_date,
                    t.fixed_date as fixed_date,
                    t.verified_date as verified_date,
                    CASE
                        WHEN t.fixed_date IS NOT NULL AND t.reported_date IS NOT NULL
                        THEN EXTRACT(EPOCH FROM (t.fixed_date - t.reported_date)) / 86400.0
                        ELSE NULL
                    END as days_to_fix,
                    1 as ticket_count,
                    t.company_id as company_id
                FROM project_ticket t
            )
        """ % self._table)
