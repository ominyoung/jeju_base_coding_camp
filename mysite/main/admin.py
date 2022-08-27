from django.contrib import admin
from main.models import Cafe

# 방법1
admin.site.register(Cafe)

# 방법2
# @admin.register(Cafe)
# class CafeAdmin(admin.ModelAdmin):
#     list_display = ['id','name','content','create_at']
#     list_display_links = ['id','name']