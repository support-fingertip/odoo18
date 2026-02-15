# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestTicketBasic(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestTicketBasic, cls).setUpClass()
        cls.Project = cls.env['project.project']
        cls.TestPlan = cls.env['project.test.plan']
        cls.TestScenario = cls.env['project.test.scenario']
        cls.TestCase = cls.env['project.test.case']
        cls.Ticket = cls.env['project.ticket']

        # Create a test project
        cls.project = cls.Project.create({
            'name': 'Test Project',
        })

    def test_create_test_plan(self):
        """Test creating a test plan"""
        test_plan = self.TestPlan.create({
            'project_id': self.project.id,
            'test_objectives': '<p>Test objectives</p>',
        })
        self.assertTrue(test_plan.name.startswith('TP-'))
        self.assertEqual(test_plan.state, 'draft')
        self.assertEqual(test_plan.project_id, self.project)

    def test_create_test_scenario(self):
        """Test creating a test scenario"""
        test_scenario = self.TestScenario.create({
            'project_id': self.project.id,
            'module': 'Test Module',
        })
        self.assertTrue(test_scenario.name.startswith('TS-'))
        self.assertEqual(test_scenario.status, 'draft')

    def test_create_test_case(self):
        """Test creating a test case"""
        test_case = self.TestCase.create({
            'test_case_title': 'Test Case Title',
            'project_id': self.project.id,
        })
        self.assertTrue(test_case.name.startswith('TC-'))
        self.assertEqual(test_case.status, 'draft')

    def test_create_ticket(self):
        """Test creating a ticket"""
        ticket = self.Ticket.create({
            'title': 'Test Bug',
            'project_id': self.project.id,
        })
        self.assertTrue(ticket.name.startswith('TK-'))
        self.assertEqual(ticket.state, 'open')
        self.assertEqual(ticket.reporter_id, self.env.user)

    def test_ticket_workflow(self):
        """Test ticket state workflow"""
        ticket = self.Ticket.create({
            'title': 'Test Bug Workflow',
            'project_id': self.project.id,
        })
        
        # Start progress
        ticket.action_start_progress()
        self.assertEqual(ticket.state, 'in_progress')
        
        # Mark as fixed
        ticket.action_mark_fixed()
        self.assertEqual(ticket.state, 'fixed')
        self.assertTrue(ticket.fixed_date)
        self.assertEqual(ticket.fixed_by_id, self.env.user)
        
        # Close ticket
        ticket.action_close()
        self.assertEqual(ticket.state, 'closed')
        
        # Reopen ticket
        ticket.action_reopen()
        self.assertEqual(ticket.state, 'reopened')

    def test_test_plan_workflow(self):
        """Test test plan state workflow"""
        test_plan = self.TestPlan.create({
            'project_id': self.project.id,
        })
        
        # Submit for review
        test_plan.action_submit_for_review()
        self.assertEqual(test_plan.state, 'in_review')
        
        # Approve
        test_plan.action_approve()
        self.assertEqual(test_plan.state, 'approved')
        
        # Close
        test_plan.action_close()
        self.assertEqual(test_plan.state, 'closed')
        
        # Reset to draft
        test_plan.action_reset_to_draft()
        self.assertEqual(test_plan.state, 'draft')
