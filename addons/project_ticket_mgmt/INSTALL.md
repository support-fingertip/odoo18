# Installation and Verification Guide

## Module Structure
```
project_ticket_mgmt/
├── README.md                          # Module documentation
├── __init__.py                        # Main module initialization
├── __manifest__.py                    # Module manifest
├── data/
│   └── sequence_data.xml             # Sequences for auto-IDs (TP-, TS-, TC-, TK-)
├── models/
│   ├── __init__.py                   # Models initialization
│   ├── test_plan.py                  # Test Plan model
│   ├── test_scenario.py              # Test Scenario model
│   ├── test_case.py                  # Test Case model
│   ├── ticket.py                     # Ticket/Bug model
│   └── ticket_report.py              # Ticket Analysis report model
├── report/
│   └── ticket_report_views.xml       # Report pivot/graph views
├── security/
│   ├── ir.model.access.csv           # Access control rights
│   └── ticket_security.xml           # Security groups
├── tests/
│   ├── __init__.py                   # Tests initialization
│   └── test_ticket_basic.py          # Basic CRUD and workflow tests
└── views/
    ├── menus.xml                      # Menu structure
    ├── test_case_views.xml            # Test Case views
    ├── test_plan_views.xml            # Test Plan views
    ├── test_scenario_views.xml        # Test Scenario views
    └── ticket_views.xml               # Ticket views (kanban, form, tree, pivot)
```

## Installation Steps

### 1. Standard Installation
```bash
# Navigate to Odoo directory
cd /path/to/odoo18

# The module is already in addons/project_ticket_mgmt/

# Start Odoo with the module in the addons path
./odoo-bin -c odoo.conf -d your_database -u project_ticket_mgmt

# Or via UI:
# 1. Login to Odoo
# 2. Go to Apps
# 3. Update Apps List
# 4. Search for "Project Ticket Management"
# 5. Click Install
```

### 2. Verify Installation
```bash
# Run module tests
./odoo-bin -c odoo.conf -d test_database -i project_ticket_mgmt --test-enable --stop-after-init
```

### 3. Post-Installation Configuration

#### Assign Security Groups
1. Go to Settings > Users & Companies > Users
2. Edit users and assign appropriate groups:
   - **Developer**: For developers who fix bugs
   - **Test Engineer**: For QA engineers who create tests and tickets
   - **QA Manager**: For QA managers with full access

#### Create Your First Test Plan
1. Go to QA & Testing > Test Plans
2. Click "Create"
3. Fill in:
   - Project (required)
   - Test Objectives
   - Scope (In/Out)
   - Test Approach
   - Test Manager and Team
4. Submit for Review > Approve

#### Create Tickets
1. Go to QA & Testing > Tickets
2. Click "Create" (Kanban view)
3. Fill in:
   - Title (required)
   - Project (required)
   - Severity and Priority
   - Description and Steps to Reproduce
   - Attach evidence (screenshots, logs)
4. Assign to a developer

## Key Features

### 1. Test Planning
- Create comprehensive test plans with objectives, scope, and criteria
- Manage test team and schedule
- Track test plan approval workflow

### 2. Test Execution
- Organize tests into scenarios and cases
- Record test steps, data, and expected results
- Track test execution and results

### 3. Defect Tracking
- Log bugs with detailed information
- Set severity (Blocker to Trivial) and priority (P0-P4)
- Track through workflow: Open → In Progress → Fixed → Closed
- Attach evidence files
- Link to test cases and projects

### 4. Reporting
- Pivot analysis of tickets by project, severity, priority
- Track average days to fix
- Filter and group by multiple dimensions

## Testing

### Run All Tests
```bash
./odoo-bin -c odoo.conf -d test_db -i project_ticket_mgmt --test-enable --stop-after-init
```

### Run Specific Test
```bash
./odoo-bin -c odoo.conf -d test_db --test-tags project_ticket_mgmt --stop-after-init
```

### Expected Test Results
- ✓ test_create_test_plan: Verify test plan creation with sequence
- ✓ test_create_test_scenario: Verify test scenario creation
- ✓ test_create_test_case: Verify test case creation
- ✓ test_create_ticket: Verify ticket creation
- ✓ test_ticket_workflow: Verify ticket state transitions
- ✓ test_test_plan_workflow: Verify test plan state transitions

## Troubleshooting

### Module Not Appearing in Apps List
```bash
# Update apps list
./odoo-bin -c odoo.conf -d your_database -u all --stop-after-init
```

### Access Denied Errors
- Check user group assignments in Settings > Users
- Verify security groups are properly loaded

### Sequence Issues
- If sequences don't auto-generate, check:
  - Database sequences are created: SELECT * FROM ir_sequence WHERE code LIKE 'project.%'
  - Sequence records exist: Check Settings > Technical > Sequences

## Module Information

**Name**: Project Ticket Management  
**Version**: 1.0  
**Category**: Services/Project  
**Dependencies**: project, mail  
**License**: LGPL-3  

**Models**:
- project.test.plan
- project.test.scenario
- project.test.case
- project.ticket
- project.ticket.report

**Lines of Code**: ~1,660  
**Test Coverage**: 6 test methods covering CRUD and workflows
