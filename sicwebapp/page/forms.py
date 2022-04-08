from django import forms
from .models import Internship, BRANCH_CHOICES

# class RawSearch(forms.Form):
#     search = forms.CharField()
#
# class Dateform(forms.Form):
#     date = forms.DateField(label='Internships before date: ')

# class MyForm(forms.ModelForm):
#     mulField = forms.MultipleChoiceField(choices=BRANCH_CHOICES, widget=forms.SelectMultiple)
#     class Meta:
#         model = Internship
#         fields = '__all__'