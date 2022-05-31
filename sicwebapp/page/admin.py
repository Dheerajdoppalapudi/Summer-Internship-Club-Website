from django.contrib import admin
# from .forms import MyForm
# from django import forms
# from django.urls import path
# from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Internship, Member, Suggestions, Scolarships, Hackathons, Fellowships, CareerFul

# Register your models here.
# admin.site.register(Internship)
# admin.site.register(Member)
admin.site.register(Suggestions)
# admin.site.register(Certifications)
# admin.site.register(Scolarships)
# admin.site.register(Hackathons)
# admin.site.register(Fellowships)
# admin.site.register(Competetive)

@admin.register(Internship, Fellowships, Scolarships, Hackathons, Member, CareerFul)
class ViewAdmin(ImportExportModelAdmin):
    pass

