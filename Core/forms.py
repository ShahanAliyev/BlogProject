from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('header', 'category','text', 'image')

        widgets = {
            'header': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        } 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

        widgets = {
                'text': forms.Textarea(attrs={
                    'class': 'form-control',
                    'cols': 5,
                    'rows': 2,
                })
            } 