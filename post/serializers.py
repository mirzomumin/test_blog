from rest_framework import serializers

from .models import Author, Tag, Post, Comment, Subscriber


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscriber
		fields = '__all__'