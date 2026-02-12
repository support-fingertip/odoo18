# Project Ticket Management

## Overview
Comprehensive Ticket (Case) Management System for Quality Assurance and Testing in Odoo 18.

## Features

### Core Models
1. **Test Plan** - Master document for QA planning per project
2. **Test Scenario** - Test scenarios linked to projects and test plans
3. **Test Case** - Detailed test cases with steps, data, and results
4. **Ticket/Bug** - Bug/defect tracking with comprehensive workflow

### Key Capabilities
- Auto-generated sequential IDs (TP-, TS-, TC-, TK-)
- Complete state workflows for test plans and tickets
- Rich HTML fields for detailed documentation
- Integration with existing project module
- Comprehensive reporting and analytics
- Role-based access control (Developer, Test Engineer, QA Manager)

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list: `Settings > Apps > Update Apps List`
3. Search for "Project Ticket Management"
4. Click "Install"

## Usage

### Access Control
Three user groups are provided:
- **Developer**: Can view tickets assigned to them and update status/resolution
- **Test Engineer**: Can create/edit test cases, scenarios, and tickets
- **QA Manager**: Full access to all models

### Menu Structure
Access the module from the "QA & Testing" menu:
- Dashboard (Tickets Kanban view)
- Test Plans
- Test Scenarios
- Test Cases
- Tickets
- Reporting > Ticket Analysis

### Workflow

#### Test Planning
1. Create a Test Plan linked to a project
2. Define test objectives, scope, approach, and criteria
3. Assign test manager and team members
4. Submit for review and get approval

#### Test Execution
1. Create Test Scenarios for different modules/features
2. Add detailed Test Cases with steps and expected results
3. Execute tests and record actual results
4. Update status (Pass/Fail/Blocked)

#### Bug Tracking
1. Create Tickets for failed tests or discovered bugs
2. Set severity (Blocker/Critical/Major/Minor/Trivial)
3. Set priority (P0/P1/P2/P3/P4)
4. Assign to developers
5. Track through workflow: Open > In Progress > Fixed > Closed
6. Attach evidence (screenshots, logs, recordings)

## Technical Details

### Dependencies
- project
- mail

### Models
- `project.test.plan`
- `project.test.scenario`
- `project.test.case`
- `project.ticket`
- `project.ticket.report`

### Security
Security groups and access rights are defined in:
- `security/ticket_security.xml`
- `security/ir.model.access.csv`

## Support
For issues and feature requests, please contact the development team.

## License
LGPL-3
