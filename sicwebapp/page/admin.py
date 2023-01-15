from django.contrib import admin
# from .forms import MyForm
# from django import forms
from django.urls import path
from django.shortcuts import render
# from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Internship, Member, Suggestions, Scolarships, Hackathons, Fellowships, CareerFul, Internship_archive

# Register your models here.
# admin.site.register(Internship)
# admin.site.register(Member)
admin.site.register(Suggestions)
# admin.site.register(Certifications)
# admin.site.register(Scolarships)
# admin.site.register(Hackathons)
# admin.site.register(Fellowships)
# admin.site.register(Competetive)

@admin.register(Fellowships, Scolarships, Hackathons, Member, CareerFul, Internship_archive)
class ViewAdmin(ImportExportModelAdmin):
    pass

class RegisteredStudetesAdmin(admin.ModelAdmin):
    # exclude = ('registered',)
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:id>/change/registered-students/', self.admin_site.admin_view(self.InternshipRegStudents))
        ]
        return my_urls + urls

    def InternshipRegStudents(self, request, id):
        context = {
            "userids": Internship.objects.get(id=id)
        }
        return render(request, "admin/regStudents.html", context)

admin.site.register(Internship, RegisteredStudetesAdmin)