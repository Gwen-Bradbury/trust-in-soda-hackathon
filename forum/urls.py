from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_forum, name='forum'),
    path('<int:forum_id>/', views.forum_comments, name='forum_comments'),
    path('addforum/', views.add_forum, name='add_forum'),
    path('editforum/<int:forum_id>/', views.edit_forum, name='edit_forum'),
    path('deleteforum/<int:forum_id>/', views.delete_forum, name='delete_forum'),
    path('editcomment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('deletecomment/<int:comment_id>/',
         views.delete_comment, name='delete_comment')
]
