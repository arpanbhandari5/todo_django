# PythonAnywhere Django Deployment Fix for 502 Backend Error

## Issue: 502-backend error indicates WSGI application failed to start

## Solution Steps:

### 1. Check your file structure on PythonAnywhere
Your files should be in `/home/Arpan5/` with this structure:
```
/home/Arpan5/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── todo/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── home.html
├── manage.py
├── db.sqlite3
└── requirements.txt
```

### 2. Update WSGI Configuration
In your PythonAnywhere Web tab, the WSGI configuration file should contain:

```python
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
```

### 3. Install Django in PythonAnywhere
Run these commands in your PythonAnywhere bash console:

```bash
# Install Django
pip3.10 install --user django

# Or if you have a requirements.txt:
pip3.10 install --user -r requirements.txt
```

### 4. Check Virtual Environment (if using one)
If you created a virtual environment:

```bash
# Activate virtual environment
source /home/Arpan5/.virtualenvs/your-env-name/bin/activate

# Install Django in virtual environment
pip install django
```

Then update WSGI file to use virtual environment:
```python
# Activate virtual environment
activate_this = '/home/Arpan5/.virtualenvs/your-env-name/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
```

### 5. Set Correct Python Version
In PythonAnywhere Web tab:
- Set Python version to 3.10 (or your preferred version)
- Make sure it matches the version you installed Django with

### 6. Reload Web App
After making changes:
- Click "Reload" button in PythonAnywhere Web tab
- Wait for the reload to complete
- Check error logs again

### 7. Static Files (if needed later)
```bash
python3.10 manage.py collectstatic --noinput
```

### 8. Debug Commands
Run these in PythonAnywhere bash console to debug:

```bash
# Check if Django is installed
python3.10 -c "import django; print(django.get_version())"

# Test your Django settings
cd /home/Arpan5
python3.10 -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings'); import django; django.setup(); print('Django setup successful')"

# Check your project structure
ls -la /home/Arpan5/
ls -la /home/Arpan5/mysite/
```

## Most Common Fixes:
1. **Path issue**: Change WSGI path from `/home/Arpan5/todo_django` to `/home/Arpan5`
2. **Django not installed**: Install Django with `pip3.10 install --user django`
3. **Wrong Python version**: Make sure web app uses same Python version as Django installation
4. **File permissions**: Check that all files are readable by web server

After trying these fixes, reload your web app and check if the 502 error is resolved.
