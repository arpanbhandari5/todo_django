"""
WSGI config for mysite project for PythonAnywhere deployment.
"""
import os
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
