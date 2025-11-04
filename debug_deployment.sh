#!/bin/bash
# Debug script for PythonAnywhere deployment

echo "🔍 Django Todo App - Debug Information"
echo "====================================="

echo "📁 Current directory:"
pwd

echo ""
echo "📄 Files in current directory:"
ls -la

echo ""
echo "🔧 Python path check:"
python3 -c "import sys; print('Python sys.path:'); [print(p) for p in sys.path]"

echo ""
echo "🐍 Django version:"
python3 -c "import django; print('Django version:', django.get_version())"

echo ""
echo "⚙️ Django settings check:"
python3 manage.py check

echo ""
echo "🌐 URL patterns:"
python3 manage.py show_urls 2>/dev/null || echo "show_urls command not available"

echo ""
echo "📊 Database check:"
python3 manage.py showmigrations

echo ""
echo "💾 Database content:"
python3 -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from todo.models import TODOAPP
print('Total tasks:', TODOAPP.objects.count())
print('Active tasks:', TODOAPP.objects.filter(is_completed=False).count())
print('Completed tasks:', TODOAPP.objects.filter(is_completed=True).count())
"
