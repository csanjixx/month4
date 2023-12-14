from django.http import HttpResponse
from datetime import datetime, timezone, timedelta

def hello_view(request):
    return HttpResponse("Hello! It's my project")

def current_date_bishkek(request):
    current_date_utc = datetime.now(timezone.utc).date()
    current_date_bishkek = current_date_utc + timedelta(hours=6)
    formatted_date = current_date_bishkek.strftime("%d-%m-%Y")
    return HttpResponse(f"Current Date in Bishkek: {formatted_date}")

def goodbye_view(request):
    return HttpResponse("Goodbye user!")
