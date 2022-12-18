from django.contrib import admin
from .models import Profile, Event
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

admin.site.register(Profile)
# admin.site.register(Event)

@admin.register(Event)
class ViewAdmin(ImportExportModelAdmin):
    pass

# class RegisteredOppAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('<int:id>/change/registered-opportunity/', self.admin_site.admin_view(self.OpportunityRegStudents))
#         ]
#         return my_urls + urls
#
#     def OpportunityRegStudents(self, request, id):
#         print("==========>>>>>>.", id)
#         context = {
#             "userids": User.objects.get(id=id)
#         }
#         return render(request, "admin/regStudents.html", context)

# admin.site.unregister(User)
# admin.site.register(User, RegisteredOppAdmin)