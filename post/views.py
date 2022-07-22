# from django.shortcuts import render

from rest_framework import generics
# Create your views here.
from .models import Post, Author, Comment
from .serializers import PostSerializer, AuthorSerializer, CommentSerializer


class PostListView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class AuthorListView(generics.ListCreateAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class AuthorPostView(generics.ListCreateAPIView):
	serializer_class = PostSerializer
	def get_queryset(self):
		queryset = Post.objects.all()
		author_id = self.kwargs['pk']
		if author_id:
			queryset = Post.objects.filter(author__id=author_id)
		return queryset


class CommentListView(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class PostCommentsView(generics.ListCreateAPIView):
	serializer_class = CommentSerializer
	def get_queryset(self):
		pk = self.kwargs['pk']
		if pk:
			queryset = Comment.objects.filter(post__id=pk)
		return queryset