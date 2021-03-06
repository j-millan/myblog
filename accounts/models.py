from django.db import models
from django.contrib.auth.models import User
from phonenumber_field import modelfields
from . import validators

def upload_location(instance, filename):
	return f'img/profile_pictures/author{instance.user.pk}-picture'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
	about = models.CharField(max_length=250, null=True, blank=True)
	profile_picture = models.ImageField(upload_to=upload_location, default='img/profile_pictures/default.png')
	phone_number = modelfields.PhoneNumberField(null=True, blank=True)
	facebook_page = models.URLField(max_length=150, null=True, blank=True, validators=[validators.validate_facebook_url])
	twitter_profile = models.URLField(max_length=150, null=True, blank=True, validators=[validators.validate_twitter_url])
	instagram_profile = models.URLField(max_length=150, null=True, blank=True, validators=[validators.validate_instagram_url])

	def __str__(self):
		return f"{self.user.username}'s profile"

	def get_full_name(self):
		return f'{self.user.first_name} {self.user.last_name}'

	def get_ordered_posts(self):
		return self.user.posts.all().order_by('-date_published')