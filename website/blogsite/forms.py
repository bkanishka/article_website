from .models import Post
from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-group'}),
            'author': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'user-name', 'id':'name'}),
            'body': forms.TextInput(attrs={'class': 'form-group'}),
            
        }

class URLForm(forms.Form):
    url = forms.URLField(label="Enter a URL")


