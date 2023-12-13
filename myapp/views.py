# myapp/views.py
from django.http import HttpResponse
from datetime import datetime

def hello_view(request):
    return HttpResponse("Hello! It's my project")

def current_date_view(request):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current Date and Time: {current_date}")

def goodbye_view(request):
    return HttpResponse("Goodbye user!")
