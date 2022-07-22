from django.db import models
from django.contrib.auth.models import User

from helpers.models import Base
# Create your models here.

class Author(Base):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	followers = models.ManyToManyField('self', blank=True)
	followings = models.ManyToManyField('self', blank=True)

	def make_follow(self, another_account):
		self.followings.add(another_account)
		another_account.followers.add(self)

	def make_unfollow(self, another_account):
		self.followings.remove(another_account)
		another_account.followers.remove(self)

	def __str__(self):
		return str(self.user)



class Tag(Base):
	name = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name


class Post(Base):
	title = models.CharField(max_length=256, blank=True, null=True)
	sub_title = models.CharField(max_length=128, blank=True, null=True)
	text = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='post/', null=True, blank=True)

	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag, blank=True)

	slug = models.SlugField(max_length=128, null=True, blank=True)
	read_time = models.PositiveIntegerField(default=0)
	views_count = models.PositiveIntegerField(default=0)
	published_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Comment(Base):
	text = models.TextField(null=True, blank=True)

	comment_by = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Subscriber(Base):
	email = models.EmailField(unique=True)