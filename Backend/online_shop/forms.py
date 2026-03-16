from django import forms
from .models import Posts


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your post here...'}),
        }
