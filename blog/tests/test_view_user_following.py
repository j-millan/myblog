from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from ..views import follow_author, unfollow_author
from ..models import BlogPost, UserFollowing
from .cases import AuthorProfileViewTestCase
from accounts.models import Profile

class FollowAuthorViewTestCases(AuthorProfileViewTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.url = reverse('blog:follow_author', kwargs={'pk': self.author.pk})
		self.response = self.client.get(self.url)

	def test_redirection(self):
		author_profile_url = reverse('blog:author_profile', kwargs={'pk': self.author.pk})
		self.assertRedirects(self.response, author_profile_url)

	def test_follower_created(self):
		self.assertTrue(UserFollowing.objects.exists())

class UnfollowAuthorViewTestCases(AuthorProfileViewTestCase):
	def setUp(self):
		super().setUp()
		UserFollowing.objects.create(user=self.user, user_following=self.author)
		self.client.login(username=self.username, password=self.password)
		self.url = reverse('blog:unfollow_author', kwargs={'pk': self.author.pk})
		self.response = self.client.get(self.url)

	def test_redirection(self):
		author_profile_url = reverse('blog:author_profile', kwargs={'pk': self.author.pk})
		self.assertRedirects(self.response, author_profile_url)

	def test_follower_deleted(self):
		self.assertFalse(UserFollowing.objects.exists())