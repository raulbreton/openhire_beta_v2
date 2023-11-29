from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    #Fields to display
    fields = ["email","is_candidate","is_employer"]

admin.site.register(CustomUser, UserAdmin)