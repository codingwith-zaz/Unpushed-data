from django.contrib import admin
from members.models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display =  ("firstname", "lastname", "joined_date", "phone", "location",)
    list_filter = ("lastname",)
    list_display_links = ("firstname", "lastname",)

admin.site.register(Member, MemberAdmin)