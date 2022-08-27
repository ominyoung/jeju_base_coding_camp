from django.contrib import admin
from django.urls import path

from main.views import cafedetails, cafelist, index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cafelist/', cafelist),
    path('cafedetails/<int:pk>', cafedetails, name='cafedetails'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
