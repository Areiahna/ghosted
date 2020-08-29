from django import forms
from ghost_app.models import PostModel
from django.utils import timezone
from datetime import datetime


class AddPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["post", "text"]
