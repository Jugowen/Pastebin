from django import forms
from .models import Post, WatchWord
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    invite = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Post
        fields = ['title', 'content' ,'private', 'invite']

class WatchForm(forms.ModelForm):
    
    class Meta:
        model = WatchWord
        fields = ['watch']
