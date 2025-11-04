# PythonAnywhere File Upload Checklist

## Current Issue: Django works but showing default page instead of your todo app

This means Django is installed but your project files are missing or in wrong location.

## Files to Upload to PythonAnywhere

Upload these files/folders to `/home/Arpan5/` directory:

### 1. Core Django Files
- ✅ `manage.py`
- ✅ `db.sqlite3` (your database with tasks)
- ✅ `requirements.txt`

### 2. mysite/ folder (Django project)
- ✅ `mysite/__init__.py`
- ✅ `mysite/settings.py`
- ✅ `mysite/urls.py`
- ✅ `mysite/views.py`
- ✅ `mysite/wsgi.py`
- ✅ `mysite/asgi.py`

### 3. todo/ folder (Django app)
- ✅ `todo/__init__.py`
- ✅ `todo/admin.py`
- ✅ `todo/apps.py`
- ✅ `todo/models.py`
- ✅ `todo/views.py`
- ✅ `todo/urls.py`
- ✅ `todo/tests.py`
- ✅ `todo/migrations/` folder with all migration files

### 4. templates/ folder
- ✅ `templates/home.html` (your todo app interface)

## Upload Methods

### Method 1: Using PythonAnywhere Files Tab
1. Go to PythonAnywhere Dashboard → Files
2. Navigate to `/home/Arpan5/`
3. Upload each file/folder manually
4. Make sure to preserve folder structure

### Method 2: Using Git (Recommended)
```bash
# In PythonAnywhere bash console
cd /home/Arpan5
git clone https://github.com/arpanbhandari5/todo_django.git
mv todo_django/* .
mv todo_django/.[^.]* .
rmdir todo_django
```

### Method 3: Using zip file
1. Zip your entire project locally
2. Upload zip to PythonAnywhere
3. Extract in `/home/Arpan5/`

## After Upload - Verification Commands

Run these in PythonAnywhere bash console:

```bash
# Check file structure
ls -la /home/Arpan5/
ls -la /home/Arpan5/mysite/
ls -la /home/Arpan5/todo/
ls -la /home/Arpan5/templates/

# Test Django can find your project
python3.10 manage.py check

# Test if your models are accessible
python3.10 manage.py shell
# In shell, try: from todo.models import TODOAPP
```

## Final Steps
1. Update WSGI configuration (already done)
2. Reload web app
3. Your todo app should now be visible!

## Expected Result Structure on PythonAnywhere:
```
/home/Arpan5/
├── manage.py
├── db.sqlite3
├── requirements.txt
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
│   ├── urls.py
│   └── migrations/
└── templates/
    └── home.html
```
