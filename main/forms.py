from django import forms

class FormsAuth(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class FileForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(attrs={'class':'spec',
    'color':'red'}))
