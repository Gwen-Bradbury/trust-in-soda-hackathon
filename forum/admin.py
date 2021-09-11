from django.contrib import admin
from .models import Forum, Comment


class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'forum_name',
        'forum_creator',
        'forum_date_created',
    )

    ordering = ('-forum_date_created',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_title',
        'comment_author',
        'comment_date_posted',
    )

    ordering = ('-comment_date_posted',)


admin.site.register(Forum, ForumAdmin)
admin.site.register(Comment, CommentAdmin)
