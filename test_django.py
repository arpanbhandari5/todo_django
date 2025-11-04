# Test Django configuration
import os
import sys
import django

# Add the project directory to Python path
project_dir = '/home/Arpan5/todo_django'
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Test imports
try:
    from django.conf import settings
    print("✅ Django settings imported successfully")
    print(f"DEBUG = {settings.DEBUG}")
    print(f"ALLOWED_HOSTS = {settings.ALLOWED_HOSTS}")
    
    from django.urls import get_resolver
    resolver = get_resolver()
    print("✅ URL resolver working")
    
    from todo.views import home
    print("✅ Todo views imported successfully")
    
    from todo.models import TODOAPP
    print("✅ Todo models imported successfully")
    print(f"Total tasks in database: {TODOAPP.objects.count()}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
