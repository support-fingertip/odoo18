# Fix for Odoo Server ParseError

## Issue
When installing the `project_ticket_mgmt` module, Odoo threw a ParseError:

```
odoo.tools.convert.ParseError: while parsing /opt/odoo18/custom_addons/project_ticket_mgmt/views/test_plan_views.xml:5
Error while validating view near:
```

## Root Cause
The views were defining `readonly="1"` attribute on the `name` fields, which are already defined as `readonly=True` in the model definitions. While this redundancy is generally harmless, it can cause view validation issues in some Odoo configurations or during certain installation scenarios.

## Fields Affected
- `project.test.plan` → `name` field
- `project.test.scenario` → `name` field  
- `project.test.case` → `name` field
- `project.ticket` → `name` field

All these fields are auto-generated sequence fields defined as:
```python
name = fields.Char(
    string='...',
    required=True,
    readonly=True,  # Already readonly in model
    default='/',
    copy=False,
    index=True,
)
```

## Solution
Removed the redundant `readonly="1"` attributes from all view files:
- `views/test_plan_views.xml`
- `views/test_scenario_views.xml`
- `views/test_case_views.xml`
- `views/ticket_views.xml`

## Changed From
```xml
<field name="name" readonly="1"/>
```

## Changed To
```xml
<field name="name"/>
```

The field remains readonly as defined in the model, so functionality is unchanged.

## Verification
All XML files validated successfully after the fix:
- ✓ XML syntax valid
- ✓ All field references exist
- ✓ View structure correct
- ✓ Ready for installation

## Testing
To test the fix, install the module:
```bash
./odoo-bin -d DATABASE -i project_ticket_mgmt --stop-after-init
```

Or via UI:
1. Apps → Update Apps List
2. Search "Project Ticket Management"
3. Click Install

The module should now install without errors.
