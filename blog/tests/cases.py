from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile

class AuthorProfileViewTestCase(TestCase):
	def setUp(self):
		self.username = 'username'
		self.password = '123'
		self.author = User.objects.create_user(username='author', password='456')
		self.user = User.objects.create_user(username=self.username, password=self.password)
		profile = Profile.objects.create(user=self.user)
		author_profile = Profile.objects.create(user=self.author, facebook_page='https://www.facebook.com')