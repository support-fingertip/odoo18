# Quick Start: Installing Project Ticket Management Module

## 📋 Prerequisites

Before installing, ensure you have:
- ✅ Odoo 18 installed and running
- ✅ Access to Odoo database
- ✅ Administrator privileges
- ✅ The `project` and `mail` modules installed (they are standard Odoo modules)

## 🚀 Installation Method 1: Via Odoo UI (Recommended)

This is the easiest method for most users.

### Step 1: Login to Odoo
1. Open your web browser
2. Navigate to your Odoo instance (e.g., `http://localhost:8069`)
3. Login with administrator credentials

### Step 2: Enable Developer Mode
1. Go to **Settings** (⚙️ icon in the top menu)
2. Scroll down to find **Developer Tools** section
3. Click **Activate the developer mode**
   - Or use the URL: `http://your-odoo-url/web?debug=1`

### Step 3: Update Apps List
1. Go to **Apps** menu (you should see it in the main menu bar)
2. Click the **⋮** (three dots) button or **Update Apps List** button
3. Click **Update** in the dialog that appears
4. Wait for the update to complete (this may take a few seconds)

### Step 4: Install the Module
1. In the **Apps** page, use the search bar
2. Remove any default filters (click ❌ on any filter chips)
3. Type: `Project Ticket Management` or `ticket`
4. You should see the module with:
   - **Name**: Project Ticket Management
   - **Technical Name**: project_ticket_mgmt
   - **Category**: Services/Project
5. Click the **Install** button
6. Wait for installation to complete (usually 5-10 seconds)

### Step 5: Verify Installation
1. Look for a new menu item: **QA & Testing** in the main menu bar
2. Click on it to see:
   - Dashboard
   - Test Plans
   - Test Scenarios
   - Test Cases
   - Tickets
   - Reporting

✅ **Installation Complete!** You can now start using the module.

---

## 🖥️ Installation Method 2: Via Command Line

For developers or when you have command-line access.

### Step 1: Verify Module Location
```bash
cd /path/to/odoo18
ls -la addons/project_ticket_mgmt/
```

You should see:
```
__init__.py
__manifest__.py
models/
views/
security/
data/
report/
tests/
```

### Step 2: Install via Odoo CLI

**Option A: Install on existing database**
```bash
./odoo-bin -c /path/to/odoo.conf -d your_database -i project_ticket_mgmt --stop-after-init
```

**Option B: Create new database with module**
```bash
./odoo-bin -c /path/to/odoo.conf -d new_database -i base,project,project_ticket_mgmt --stop-after-init
```

**Option C: Update existing installation**
```bash
./odoo-bin -c /path/to/odoo.conf -d your_database -u project_ticket_mgmt --stop-after-init
```

### Step 3: Start Odoo Server
```bash
./odoo-bin -c /path/to/odoo.conf
```

### Step 4: Access via Browser
Navigate to `http://localhost:8069` (or your configured URL)

---

## 🐳 Installation Method 3: Docker

If you're using Odoo in Docker:

### Step 1: Copy Module to Docker Volume
```bash
# If using docker-compose with volumes
docker cp /path/to/project_ticket_mgmt your-odoo-container:/mnt/extra-addons/

# Or mount it in docker-compose.yml:
volumes:
  - ./addons/project_ticket_mgmt:/mnt/extra-addons/project_ticket_mgmt
```

### Step 2: Restart Container
```bash
docker-compose restart odoo
```

### Step 3: Follow UI Installation Steps
Go to Apps > Update Apps List > Install

---

## ⚙️ Post-Installation Configuration

### 1. Assign User Groups

Users need appropriate permissions to use the module:

1. Go to **Settings** > **Users & Companies** > **Users**
2. Select a user
3. Click **Edit**
4. Scroll to **Ticket Management** section (or search for it)
5. Assign one of these groups:
   - **QA Manager** - Full access (recommended for QA leads)
   - **Test Engineer** - Can create tests and tickets (for QA team)
   - **Developer** - Can view and update tickets (for developers)

### 2. Create Your First Project (if needed)

The module requires at least one project:

1. Go to **Project** menu
2. Click **Create**
3. Fill in project name and details
4. Save

### 3. Create Your First Test Plan

1. Go to **QA & Testing** > **Test Plans**
2. Click **Create**
3. Fill in:
   - Project (required)
   - Test Objectives
   - Test Manager
4. Click **Save**

---

## ✅ Verification Checklist

After installation, verify these items:

- [ ] **Menu visible**: "QA & Testing" appears in main menu
- [ ] **Models accessible**: Can open Test Plans, Test Scenarios, Test Cases, Tickets
- [ ] **Sequences working**: Creating a test plan generates "TP-0001" ID
- [ ] **Security working**: Different users see appropriate access levels
- [ ] **Chatter working**: Can post messages on tickets
- [ ] **Reports working**: Ticket Analysis pivot view loads

---

## 🧪 Test the Installation

Run these quick tests to ensure everything works:

### Test 1: Create a Test Plan
```
QA & Testing > Test Plans > Create
- Enter project name
- Save
- Check: ID should be "TP-0001" or similar
```

### Test 2: Create a Ticket
```
QA & Testing > Tickets > Create (in Kanban view)
- Enter title: "Test Bug"
- Select project
- Save
- Check: ID should be "TK-0001" or similar
```

### Test 3: Check Workflow
```
Open the ticket you created
- Click "Start Progress" button
- Check: State changes to "In Progress"
- Click "Mark as Fixed"
- Check: State changes to "Fixed", dates are filled
```

---

## 🔧 Troubleshooting

### Issue 1: Module Not Appearing in Apps List

**Solution:**
1. Make sure you updated the apps list (Step 3 of UI method)
2. Remove all filters in the Apps search
3. Try searching by technical name: `project_ticket_mgmt`
4. Check if the module folder exists: `ls addons/project_ticket_mgmt/`

### Issue 2: "Module Not Found" Error

**Possible causes:**
- Module not in addons path
- Odoo not restarted after copying module

**Solution:**
```bash
# Check addons path in your configuration
grep addons_path /path/to/odoo.conf

# Add the path if needed:
addons_path = /path/to/odoo/addons,/path/to/custom/addons

# Restart Odoo
./odoo-bin -c /path/to/odoo.conf
```

### Issue 3: Installation Fails with Dependencies Error

**Error:** "Could not find module 'project' or 'mail'"

**Solution:**
```bash
# Install dependencies first
./odoo-bin -d your_database -i project,mail --stop-after-init

# Then install the ticket module
./odoo-bin -d your_database -i project_ticket_mgmt --stop-after-init
```

### Issue 4: "Access Denied" Errors

**Solution:**
1. Assign appropriate user groups (see Post-Installation Configuration)
2. Or temporarily grant admin rights for testing
3. Check security groups: Settings > Users & Companies > Groups

### Issue 5: Sequences Not Generating

**Solution:**
```bash
# Re-install the module to reload data
./odoo-bin -d your_database -u project_ticket_mgmt --stop-after-init
```

Or via UI:
1. Apps > Search "Project Ticket Management"
2. Click "Upgrade" button

---

## 📊 What Gets Installed

When you install the module, Odoo automatically:

1. **Creates 5 new models:**
   - project.test.plan
   - project.test.scenario
   - project.test.case
   - project.ticket
   - project.ticket.report

2. **Adds 4 sequences:**
   - TP-XXXX for Test Plans
   - TS-XXXX for Test Scenarios
   - TC-XXXX for Test Cases
   - TK-XXXX for Tickets

3. **Creates 3 security groups:**
   - Developer
   - Test Engineer
   - QA Manager

4. **Adds menu items:**
   - QA & Testing (main menu)
   - Sub-menus for each model
   - Reporting menu

5. **Creates 21 views:**
   - Forms, trees, searches, kanban, pivot views

---

## 🎯 Next Steps

After successful installation:

1. **Read the documentation:**
   - `README.md` - Feature overview
   - `TECHNICAL.md` - Architecture details
   - `MODULE_SUMMARY.md` - Complete feature list

2. **Assign user groups** to your team members

3. **Create your first test plan** linked to a project

4. **Start logging tickets** for bugs and issues

5. **Explore the reporting** features in Ticket Analysis

---

## 💡 Quick Tips

- **Kanban View**: Tickets are best viewed in Kanban mode (grouped by state)
- **Evidence**: Attach screenshots to tickets using the evidence field
- **Tags**: Use project tags to categorize tickets
- **Chatter**: Use chatter for communication about tickets
- **Workflows**: Use action buttons (Start Progress, Mark as Fixed, etc.)

---

## 📞 Need Help?

- Check `TECHNICAL.md` for implementation details
- Check `README.md` for usage guide
- Review `MODULE_SUMMARY.md` for complete feature list
- Check Odoo logs: `less /var/log/odoo/odoo.log`

---

**Module Version:** 1.0  
**Odoo Version:** 18.0  
**Last Updated:** 2026-02-15
