from django import forms


class UserForm(forms.Form):
    photo = forms.FileField()
