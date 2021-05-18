from django.contrib import admin
from groups.models import (Group, GroupMembers)

# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = GroupMembers

admin.site.register(Group)
admin.site.register(GroupMembers)
