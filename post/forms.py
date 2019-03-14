from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    invite = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Post
        fields = ['title', 'content' ,'private', 'invite', 'expires']

class WatchForm(forms.ModelForm):
    watch = forms.CharField()

    class Meta:
        model = User
        fields = ['watch']
