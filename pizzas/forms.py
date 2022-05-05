from xml.etree.ElementTree import Comment
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_name']
        labels = {'comment_name':''}
        widgets = {'comment_name': forms.Textarea(attrs={'cols':80})}