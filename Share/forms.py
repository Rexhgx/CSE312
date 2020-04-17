from django import forms


class PostForm(forms.Form):
    post_photo = forms.FileField()