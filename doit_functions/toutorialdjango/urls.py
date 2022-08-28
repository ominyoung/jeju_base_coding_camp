from django.contrib import admin
from django.urls import path

from main.views import hospitaldetail, hospitallist, index

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='index'),
    path('hospitallist/', hospitallist, name='hospitallist'),
    path('hospitaldetail/<str:name>', hospitaldetail, name='hospitaldetail'),
]
