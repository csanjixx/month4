from django.urls import path
from myapp.views import hello_view, current_date_view, goodbye_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('current_date/', current_date_view, name='current_date'),
    path('goodbye/', goodbye_view, name='goodbye'),
]

