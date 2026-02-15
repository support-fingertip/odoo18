#!/bin/bash
# Installation Verification Script for Project Ticket Management Module
# This script helps verify that the module is properly installed

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║     Project Ticket Management Module - Installation Verification         ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print success
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Function to print error
print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Function to print warning
print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Function to print info
print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Step 1: Check if we're in Odoo directory
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 1: Checking Odoo installation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -f "odoo-bin" ]; then
    print_success "Found odoo-bin - Odoo installation detected"
else
    print_error "odoo-bin not found - Please run this script from Odoo root directory"
    exit 1
fi

# Step 2: Check if module directory exists
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 2: Checking module location"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

MODULE_PATH="addons/project_ticket_mgmt"

if [ -d "$MODULE_PATH" ]; then
    print_success "Module directory found at: $MODULE_PATH"
else
    print_error "Module directory not found at: $MODULE_PATH"
    echo ""
    print_info "Please ensure the module is placed in the addons directory"
    exit 1
fi

# Step 3: Check module files
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 3: Verifying module files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

REQUIRED_FILES=(
    "__init__.py"
    "__manifest__.py"
    "models/__init__.py"
    "models/test_plan.py"
    "models/test_scenario.py"
    "models/test_case.py"
    "models/ticket.py"
    "models/ticket_report.py"
    "views/test_plan_views.xml"
    "views/test_scenario_views.xml"
    "views/test_case_views.xml"
    "views/ticket_views.xml"
    "views/menus.xml"
    "security/ticket_security.xml"
    "security/ir.model.access.csv"
    "data/sequence_data.xml"
)

missing_files=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$MODULE_PATH/$file" ]; then
        print_success "$file"
    else
        print_error "$file - MISSING"
        missing_files=$((missing_files + 1))
    fi
done

if [ $missing_files -gt 0 ]; then
    echo ""
    print_error "Missing $missing_files required file(s)"
    exit 1
fi

# Step 4: Validate Python syntax
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 4: Validating Python syntax"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command -v python3 &> /dev/null; then
    python_errors=0
    for py_file in $(find $MODULE_PATH -name "*.py" -not -path "*/__pycache__/*"); do
        if python3 -m py_compile "$py_file" 2>/dev/null; then
            print_success "$(basename $py_file)"
        else
            print_error "$(basename $py_file) - Syntax error"
            python_errors=$((python_errors + 1))
        fi
    done
    
    if [ $python_errors -eq 0 ]; then
        print_success "All Python files are valid"
    else
        print_error "Found $python_errors Python syntax error(s)"
        exit 1
    fi
else
    print_warning "Python3 not found - Skipping syntax check"
fi

# Step 5: Check manifest file
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 5: Checking module manifest"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if python3 -c "import ast; ast.literal_eval(open('$MODULE_PATH/__manifest__.py').read())" 2>/dev/null; then
    print_success "Manifest file is valid"
    
    # Extract info from manifest
    MODULE_NAME=$(python3 -c "import ast; manifest = ast.literal_eval(open('$MODULE_PATH/__manifest__.py').read()); print(manifest.get('name', 'Unknown'))")
    MODULE_VERSION=$(python3 -c "import ast; manifest = ast.literal_eval(open('$MODULE_PATH/__manifest__.py').read()); print(manifest.get('version', 'Unknown'))")
    
    print_info "Module Name: $MODULE_NAME"
    print_info "Module Version: $MODULE_VERSION"
else
    print_error "Manifest file is invalid"
    exit 1
fi

# Step 6: Summary and next steps
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 6: Installation Status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

print_success "Module is ready for installation!"
echo ""
print_info "Next steps to install the module:"
echo ""
echo "  Method 1: Via Odoo UI (Recommended)"
echo "  ────────────────────────────────────"
echo "  1. Start Odoo: ./odoo-bin -c odoo.conf"
echo "  2. Login to Odoo web interface"
echo "  3. Go to: Apps > Update Apps List"
echo "  4. Search: 'Project Ticket Management'"
echo "  5. Click: Install"
echo ""
echo "  Method 2: Via Command Line"
echo "  ──────────────────────────"
echo "  ./odoo-bin -c odoo.conf -d DATABASE -i project_ticket_mgmt --stop-after-init"
echo ""
echo "  Method 3: Run Tests"
echo "  ───────────────────"
echo "  ./odoo-bin -c odoo.conf -d DATABASE -i project_ticket_mgmt --test-enable --stop-after-init"
echo ""

print_info "For detailed instructions, see: QUICKSTART.md"
echo ""
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                    ✓ Verification Complete                               ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
