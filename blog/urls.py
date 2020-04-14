from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('<pk>/publish/', views.post_publish, name='post_publish'),
    path('<pk>/remove/', views.post_remove, name='post_remove'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:pk>/approve/comment/', views.comment_approve, name='comment_approve'),
    path('<int:pk>/remove/comment/', views.comment_remove, name='comment_remove'),
]
