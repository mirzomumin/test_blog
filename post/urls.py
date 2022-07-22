from django.urls import path

from . import views


urlpatterns = [
	path('posts/', views.PostListView.as_view()),
	path('posts/<int:pk>/', views.PostDetailView.as_view()),
	path('posts/<int:pk>/comments/', views.PostCommentsView.as_view()),
	path('authors/', views.AuthorListView.as_view()),
	path('authors/<int:pk>/', views.AuthorDetailView.as_view()),
	path('authors/<int:pk>/posts/', views.AuthorPostView.as_view()),
	path('comments/', views.CommentListView.as_view()),
	path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]