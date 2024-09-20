from django.contrib import admin
from .models import Welcome

class MemberAdmin(admin.ModelAdmin):
    list_display=("name","age",)

# Register your models here.
admin.site.register(Welcome,MemberAdmin)