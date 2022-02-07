from django import forms
class RawSearch(forms.Form):
    search = forms.CharField()

class Dateform(forms.Form):
    date = forms.DateField(label='Internships before date: ')