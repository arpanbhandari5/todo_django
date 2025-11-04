#!/usr/bin/env python3
"""
Verification script to run on PythonAnywhere after uploading project files
Run this in PythonAnywhere bash console: python3.10 verify_upload.py
"""

import os
import sys

def check_file_exists(filepath, description):
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {filepath}")
    return exists

def check_directory_contents(dirpath, description):
    if os.path.exists(dirpath):
        contents = os.listdir(dirpath)
        print(f"✅ {description} contents: {contents}")
        return True
    else:
        print(f"❌ {description} directory not found: {dirpath}")
        return False

print("=== PYTHONANYWHERE PROJECT UPLOAD VERIFICATION ===\n")

base_path = "/home/Arpan5"
print(f"Checking project in: {base_path}\n")

# Check core files
print("1. CORE FILES:")
check_file_exists(f"{base_path}/manage.py", "Django manage.py")
check_file_exists(f"{base_path}/db.sqlite3", "SQLite database")
check_file_exists(f"{base_path}/requirements.txt", "Requirements file")

print("\n2. MYSITE FOLDER:")
mysite_exists = check_directory_contents(f"{base_path}/mysite", "mysite")
if mysite_exists:
    check_file_exists(f"{base_path}/mysite/__init__.py", "mysite __init__.py")
    check_file_exists(f"{base_path}/mysite/settings.py", "Django settings")
    check_file_exists(f"{base_path}/mysite/urls.py", "mysite URLs")
    check_file_exists(f"{base_path}/mysite/views.py", "mysite views")
    check_file_exists(f"{base_path}/mysite/wsgi.py", "WSGI config")

print("\n3. TODO APP FOLDER:")
todo_exists = check_directory_contents(f"{base_path}/todo", "todo")
if todo_exists:
    check_file_exists(f"{base_path}/todo/__init__.py", "todo __init__.py")
    check_file_exists(f"{base_path}/todo/models.py", "todo models")
    check_file_exists(f"{base_path}/todo/views.py", "todo views")
    check_file_exists(f"{base_path}/todo/urls.py", "todo URLs")
    check_file_exists(f"{base_path}/todo/admin.py", "todo admin")
    check_directory_contents(f"{base_path}/todo/migrations", "todo migrations")

print("\n4. TEMPLATES FOLDER:")
templates_exists = check_directory_contents(f"{base_path}/templates", "templates")
if templates_exists:
    check_file_exists(f"{base_path}/templates/home.html", "home.html template")

print("\n5. DJANGO FUNCTIONALITY TEST:")
os.chdir(base_path)

try:
    # Test Django can import settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()
    print("✅ Django settings loaded successfully")
    
    # Test models import
    from todo.models import TODOAPP
    task_count = TODOAPP.objects.count()
    print(f"✅ Todo models imported successfully. Tasks in database: {task_count}")
    
    # Test views import
    from todo.views import home
    print("✅ Todo views imported successfully")
    
    # Test URL configuration
    from django.urls import reverse
    home_url = reverse('home')
    print(f"✅ URL routing working. Home URL: {home_url}")
    
except Exception as e:
    print(f"❌ Django functionality error: {e}")
    import traceback
    traceback.print_exc()

print("\n=== NEXT STEPS ===")
print("If all checks pass:")
print("1. Reload your web app in PythonAnywhere")
print("2. Visit https://arpan5.pythonanywhere.com")
print("3. You should see your TaskFlow todo app!")
print("\nIf any checks fail:")
print("1. Upload the missing files")
print("2. Run this script again")
print("3. Contact support if issues persist")

print("\n=== END VERIFICATION ===")
