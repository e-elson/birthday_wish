from django import forms
from .models import Wish

class WishForm(forms.Form):
    author = forms.CharField(max_length=40,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your name'
                             })
                             )
    email = forms.CharField(max_length=40,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email',
                                 'type': 'email',
                                 'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
                             })
                             )

    description = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'A short description of yourself/who AY is to you or how you know her'
                             })
                             )

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Leave a birthday wish for AY'
    })
    )


class ReplyForm(forms.Form):
    msg = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Leave a reply'
    })
    )