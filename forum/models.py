from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Forum(models.Model):
    image_url = models.URLField(max_length=1024, default="", blank=True)
    image = models.ImageField(default="", blank=True)
    forum_name = models.CharField(max_length=100)
    forum_description = models.TextField()
    forum_date_created = models.DateTimeField(default=timezone.now)
    forum_creator = models.ForeignKey(User, default="", blank=True,
                                      on_delete=models.CASCADE,
                                      related_name='forum')

    class Meta:
        ordering = ['-forum_date_created']

    def __str__(self):
        return self.forum_name


class Comment(models.Model):
    forum_id = models.ForeignKey('Forum', null=True,
                                 related_name="comments", blank=True,
                                 on_delete=models.SET_NULL)
    comment_title = models.CharField(max_length=50)
    comment_content = models.TextField(max_length=500)
    comment_date_posted = models.DateTimeField(default=timezone.now)
    comment_author = models.ForeignKey(User, null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name='comment')

    class Meta:
        ordering = ['-comment_date_posted']

    def __str__(self):
        return self.comment_title
