from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.text import slugify, Truncator
from django.utils.html import mark_safe
from markdown import markdown

from accounts.models import Profile

DEFAULT_CATEGORY_ID = 1 # The id of the category all BlogPost objects will fall in by default.

def upload_location(instance, filename):
	return f'img/blog_thumbnails/author{instance.author.pk}/{instance.title}-thumbnail'

class BlogPost(models.Model):
	title = models.CharField(max_length=75, null=False, blank=False, unique=True)
	body = models.TextField(max_length=25000, null=False, blank=False)
	thumbnail = models.ImageField(upload_to=upload_location, default='img/blog_thumbnails/default.jpg')
	author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=False)
	date_published  = models.DateTimeField(auto_now_add=True, verbose_name='date published') 
	date_updated  = models.DateTimeField(auto_now=True, verbose_name='date updated')
	categories = models.ManyToManyField('BlogCategory', default=DEFAULT_CATEGORY_ID, related_name='articles')
	slug = models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title

	def get_body_as_markdown(self):
		return mark_safe(markdown(self.body, safe_mode='escape'))

	def get_truncated_body(self):
		return Truncator(self.body).chars(250)

	def get_ordered_comments(self):
		return self.comments.order_by('-created_at')

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, *args, **kwargs):
	instance.image.delete(False)

def pre_save_blogpost_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(f'{instance.author.username}-{instance.title}')

pre_save.connect(pre_save_blogpost_receiver, sender=BlogPost)

class BlogComment(models.Model):
	message = models.CharField(max_length=600, blank=False)
	article = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	edited_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'"{Truncator(self.message).chars(10)}" at {self.article}'


class UserFollowing(models.Model):
	user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
	user_following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
	date_followed = models.DateField(auto_now_add=True)

	class Meta:
		unique_together = ['user', 'user_following']

	def __str__(self):
		return f'{self.user} follows {self.user_following}'

class BlogCategory(models.Model):
	name = models.CharField(max_length=50, unique=True)
	color_choices = [
		('ISL', 'is-light'),
		('ISP', 'is-primary'),
		('ISL', 'is-link'),
		('ISI', 'is-info'),
		('ISS', 'is-success'),
		('ISW', 'is-warning'),
		('ISD', 'is-danger')
	]
	tag_color = models.CharField(max_length=10, choices=color_choices, default='is-light')

	def __str__(self):
		return self.name