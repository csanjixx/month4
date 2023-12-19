from django.contrib import admin
from django.urls import include, path
from Product import urls as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(product_urls)),
]
