# Installation Cheat Sheet - Project Ticket Management

## 📦 What You Need
- Odoo 18 installed ✅
- Admin access ✅
- Modules: `project`, `mail` (standard, usually pre-installed) ✅

## 🚀 3-Step Installation (UI Method)

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: Access Apps                                        │
│ Login → Click "Apps" in main menu                          │
└─────────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Update Apps List                                   │
│ Click "Update Apps List" → Click "Update"                  │
│ (Wait a few seconds)                                        │
└─────────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Install Module                                     │
│ Search: "Project Ticket Management"                        │
│ Click: "Install" button                                    │
│ (Wait 5-10 seconds)                                        │
└─────────────────────────────────────────────────────────────┘
              ↓
         ✅ DONE!
   Look for "QA & Testing" menu
```

## 💻 One-Line Installation (CLI Method)

```bash
./odoo-bin -c odoo.conf -d YOUR_DB -i project_ticket_mgmt --stop-after-init
```

## ✅ Quick Verification

After installation, check:
- [ ] "QA & Testing" menu appears in main menu bar
- [ ] Can open: Test Plans, Test Scenarios, Test Cases, Tickets
- [ ] Create a ticket → ID starts with "TK-"

## 🔧 First Time Setup (2 minutes)

### 1. Assign User Groups
```
Settings → Users & Companies → Users → Edit User
Scroll to "Ticket Management" section
Select: QA Manager / Test Engineer / Developer
```

### 2. Create First Test Plan
```
QA & Testing → Test Plans → Create
Fill: Project (required), Test Objectives
Save → Check ID is "TP-0001"
```

### 3. Create First Ticket
```
QA & Testing → Tickets → Create (Kanban)
Fill: Title, Project (required)
Save → Check ID is "TK-0001"
```

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not in Apps list | Update Apps List (Step 2) |
| Can't see "QA & Testing" menu | Check user groups assigned |
| IDs not auto-generating | Restart Odoo or reinstall module |
| Access denied errors | Assign user to QA Manager group |

## 📚 Documentation Files

- `QUICKSTART.md` - Full installation guide with screenshots
- `README.md` - Feature overview and usage
- `INSTALL.md` - Technical installation details
- `TECHNICAL.md` - Architecture and code details

## 🧪 Run Verification Script

```bash
cd /path/to/odoo18
./addons/project_ticket_mgmt/verify_installation.sh
```

## 📞 Common Commands

```bash
# Install with tests
./odoo-bin -d DB -i project_ticket_mgmt --test-enable --stop-after-init

# Update/upgrade module
./odoo-bin -d DB -u project_ticket_mgmt --stop-after-init

# Start Odoo
./odoo-bin -c odoo.conf

# Install in Docker
docker exec CONTAINER ./odoo-bin -d DB -i project_ticket_mgmt --stop-after-init
```

## 🎯 What Gets Installed

✅ 5 Models (Test Plan, Scenario, Case, Ticket, Report)  
✅ 4 Sequences (TP-, TS-, TC-, TK-)  
✅ 3 Security Groups  
✅ 21 Views (Forms, Trees, Kanban, Pivot)  
✅ 8 Menu Items under "QA & Testing"  
✅ Reporting & Analytics

---

**Module:** project_ticket_mgmt  
**Version:** 1.0  
**Odoo:** 18.0  
**License:** LGPL-3
