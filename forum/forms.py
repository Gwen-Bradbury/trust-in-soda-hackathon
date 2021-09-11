from django import forms
from .widgets import CustomClearableFileInput
from .models import Forum, Comment


class AddForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = (
                  'image_url',
                  'image',
                  'forum_name',
                  'forum_description',
                 )

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
                  'comment_title',
                  'comment_content',
                 )
