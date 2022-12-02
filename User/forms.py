# from django import forms
# from .models import 

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ('header', 'text', 'image')

#         widgets = {
#             'header': forms.TextInput(attrs={
#                 'class': 'form-control',
#             }),
#             'text': forms.Textarea(attrs={
#                 'class': 'form-control',
#             }),
#         } 

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('text', )

#         widgets = {
#                 'text': forms.Textarea(attrs={
#                     'class': 'form-control',
#                     'cols': 5,
#                     'rows': 2,
#                 })
#             }


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(CustomRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'