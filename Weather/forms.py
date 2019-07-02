from django import forms

class WeatherSearchForm(forms.Form):
    ZipCode = forms.IntegerField(required=False)
    City_Name = forms.CharField(required=False) 