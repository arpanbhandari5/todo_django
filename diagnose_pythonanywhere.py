#!/usr/bin/env python3
"""
Diagnostic script for PythonAnywhere deployment issues
Run this in your PythonAnywhere bash console to diagnose path and Django issues
"""

import os
import sys

print("=== PYTHONANYWHERE DJANGO DIAGNOSTIC ===\n")

# Check current directory
print(f"Current working directory: {os.getcwd()}")

# Check home directory contents
home_dir = os.path.expanduser('~')
print(f"Home directory: {home_dir}")
print("Contents of home directory:")
try:
    for item in os.listdir(home_dir):
        print(f"  - {item}")
except Exception as e:
    print(f"Error listing home directory: {e}")

print()

# Check if mysite directory exists
mysite_paths = [
    os.path.join(home_dir, 'mysite'),
    os.path.join(home_dir, 'todo_django'),
    os.path.join(home_dir, 'todo_django', 'mysite'),
    '/var/www/arpan5_pythonanywhere_com_wsgi.py'
]

for path in mysite_paths:
    exists = os.path.exists(path)
    print(f"Path exists: {path} -> {exists}")
    if exists and os.path.isdir(path):
        try:
            contents = os.listdir(path)
            print(f"  Contents: {contents}")
        except:
            pass

print()

# Check Python path
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Python path:")
for p in sys.path:
    print(f"  - {p}")

print()

# Try to import Django
try:
    import django
    print(f"Django version: {django.get_version()}")
    print("Django location:", django.__file__)
except ImportError as e:
    print(f"Django import error: {e}")

print()

# Try to import your Django settings
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()
    from django.conf import settings
    print("Django settings imported successfully")
    print(f"DEBUG: {settings.DEBUG}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
except Exception as e:
    print(f"Django settings import error: {e}")
    import traceback
    traceback.print_exc()

print("\n=== END DIAGNOSTIC ===")
