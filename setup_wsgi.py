#!/usr/bin/env python3
"""
Automated WSGI Configuration Script for PythonAnywhere
Run this after the deploy.sh script completes
"""

import os

# WSGI Configuration Content
wsgi_content = '''import os
import sys

# Add your project directory to the sys.path
path = '/home/Arpan5'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''

print("=== AUTOMATED WSGI CONFIGURATION ===")
print("Setting up WSGI configuration for PythonAnywhere...")

# Get the path to the WSGI file (this varies by username)
wsgi_path = "/var/www/arpan5_pythonanywhere_com_wsgi.py"

try:
    # Write the WSGI configuration
    with open(wsgi_path, 'w') as f:
        f.write(wsgi_content)
    
    print(f"✅ WSGI configuration written to: {wsgi_path}")
    print("✅ WSGI setup complete!")
    
    print("\n=== FINAL STEPS ===")
    print("1. Go to PythonAnywhere Web tab")
    print("2. Click 'Reload' button")
    print("3. Wait 30 seconds for reload to complete")
    print("4. Visit https://arpan5.pythonanywhere.com")
    print("5. Your TaskFlow todo app should be working! 🎉")
    
except PermissionError:
    print("❌ Permission denied - you need to update WSGI manually")
    print("\n📋 MANUAL WSGI CONFIGURATION:")
    print("Go to PythonAnywhere Web tab → WSGI configuration file")
    print("Replace the contents with this:")
    print("-" * 50)
    print(wsgi_content)
    print("-" * 50)
    print("Then click Save and Reload your web app")

except Exception as e:
    print(f"❌ Error: {e}")
    print("\n📋 MANUAL WSGI CONFIGURATION:")
    print("Go to PythonAnywhere Web tab → WSGI configuration file")
    print("Replace the contents with this:")
    print("-" * 50)
    print(wsgi_content)
    print("-" * 50)
    print("Then click Save and Reload your web app")

print("\n=== DEPLOYMENT COMPLETE! ===")
