#!/bin/bash
# Automated PythonAnywhere Deployment Script
# Run this in your PythonAnywhere bash console

echo "=== AUTOMATED PYTHONANYWHERE DEPLOYMENT ==="
echo "Starting deployment for TaskFlow Todo App..."

# Step 1: Navigate to home directory
echo "� Navigating to home directory..."
cd /home/Arpan5

# Step 2: Remove any existing project files
echo "🧹 Cleaning up existing files..."
rm -rf mysite/ todo/ templates/ manage.py db.sqlite3 requirements.txt *.py

# Step 3: Clone the repository
echo "📥 Cloning repository from GitHub..."
git clone https://github.com/arpanbhandari5/todo_django.git temp_repo

# Step 4: Move files to correct location
echo "📋 Moving files to correct location..."
mv temp_repo/* . 2>/dev/null
mv temp_repo/.[^.]* . 2>/dev/null
rmdir temp_repo

# Step 5: Install requirements
echo "📦 Installing Python packages..."
pip3.10 install --user -r requirements.txt

# Step 6: Run Django migrations
echo "🗃️ Setting up database..."
python3.10 manage.py migrate

# Step 7: Create superuser (optional)
echo "👤 Creating superuser (optional)..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python3.10 manage.py shell 2>/dev/null

# Step 8: Collect static files
echo "🎨 Collecting static files..."
python3.10 manage.py collectstatic --noinput

# Step 9: Test Django setup
echo "🧪 Testing Django configuration..."
python3.10 manage.py check

# Step 10: Verify project structure
echo "📋 Verifying project structure..."
echo "Project files:"
ls -la
echo ""
echo "mysite folder:"
ls -la mysite/ 2>/dev/null
echo ""
echo "todo folder:"
ls -la todo/ 2>/dev/null
echo ""
echo "templates folder:"
ls -la templates/ 2>/dev/null

echo ""
echo "=== DEPLOYMENT COMPLETE! ==="
echo "Next steps:"
echo "1. Go to PythonAnywhere Web tab"
echo "2. Click 'Reload' button"
echo "3. Visit https://arpan5.pythonanywhere.com"
echo "4. Your TaskFlow todo app should be working!"

echo ""
echo "If you see any errors above, please report them."
echo "Otherwise, your deployment was successful! 🎉"
