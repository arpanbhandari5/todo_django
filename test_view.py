# Simple test view for debugging
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("""
    <h1>🎉 Django is Working!</h1>
    <p>This is a test page from your todo app.</p>
    <p>If you see this, Django is properly configured.</p>
    <a href="/">Go to Todo App</a>
    """)
