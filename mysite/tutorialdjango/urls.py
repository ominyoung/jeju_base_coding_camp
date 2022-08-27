from django.contrib import admin
from django.urls import path

from main.views import cafedetails, cafelist, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cafelist/', cafelist),
    path('cafedetails/<int:pk>', cafedetails),
]
