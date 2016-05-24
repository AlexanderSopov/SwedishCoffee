from django import forms

class EmailForm(forms.Form):
    your_email = forms.EmailField(label="",)