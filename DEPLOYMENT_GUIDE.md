# PythonAnywhere Deployment Instructions for Django Todo App

## Step 1: Upload Your Files
1. Go to https://www.pythonanywhere.com/login/
2. Login with:
   - Username: Arpan5
   - Password: OMprakash5*

## Step 2: Upload Project Files
1. Click on "Files" tab
2. Navigate to your home directory (/home/Arpan5/)
3. Create a new folder called "todo_django"
4. Upload all your project files to this folder

## Step 3: Open a Bash Console
1. Click on "Consoles" tab
2. Click "Bash" to open a new bash console

## Step 4: Set up Virtual Environment
Run these commands in the bash console:

```bash
cd ~
python3.10 -m venv todo_venv
source todo_venv/bin/activate
cd todo_django
pip install -r requirements.txt
```

## Step 5: Set up Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```

## Step 6: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## Step 7: Configure Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Choose "Python 3.10"
5. Click "Next"

## Step 8: Configure WSGI File
1. In the Web tab, find the "Code" section
2. Click on the WSGI configuration file link
3. Replace the contents with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/Arpan5/todo_django'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Step 9: Configure Virtual Environment
1. In the Web tab, find the "Virtualenv" section
2. Enter: /home/Arpan5/todo_venv

## Step 10: Configure Static Files
1. In the Web tab, find the "Static files" section
2. Add a new static file mapping:
   - URL: /static/
   - Directory: /home/Arpan5/todo_django/static

## Step 11: Reload and Test
1. Click the green "Reload" button
2. Visit your app at: https://arpan5.pythonanywhere.com

## Your App URLs:
- Main site: https://arpan5.pythonanywhere.com
- Admin: https://arpan5.pythonanywhere.com/admin

## Troubleshooting:
- Check error logs in the Web tab
- Make sure all file paths are correct
- Ensure virtual environment is activated
- Check that all dependencies are installed
