from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from ..views import UserDetailView
from ..models import BlogPost, UserFollowing
from ..forms import SearchForm
from .cases import AuthorProfileViewTestCase
from accounts.models import Profile

class AuthorProfileViewTests(AuthorProfileViewTestCase):
	def setUp(self):
		super().setUp()
		self.url = reverse('blog:author_profile', kwargs={'pk': self.author.pk})
		self.response = self.client.get(self.url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_function(self):
		view = resolve('/author/1/')
		self.assertEquals(view.func.view_class, UserDetailView)

	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_contains_search_bar(self):
		form = self.response.context.get('search_form')
		self.assertIsInstance(form, SearchForm)

	def test_contains_authentication_links(self):
		login_url = reverse('accounts:login')
		signup_url = reverse('accounts:signup')
		self.assertContains(self.response, f'href="{login_url}"')
		self.assertContains(self.response, f'href="{signup_url}"')

class AuthorProfileViewAuthenticatedTests(AuthorProfileViewTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.url = reverse('blog:author_profile', kwargs={'pk': self.author.pk})
		self.response = self.client.get(self.url)

	def test_contains_new_article_button(self):
		new_post_url = reverse('blog:new_article')
		response = self.client.get(self.url)
		self.assertContains(response, f'href="{new_post_url}"')

	def test_contains_follow_button(self):
		follow_url = reverse('blog:follow_author', kwargs={'pk': self.author.pk})
		self.assertContains(self.response, f'href="{follow_url}"')

	def test_contains_unfollow_button(self):
		UserFollowing.objects.create(user=self.user, user_following=self.author)
		response = self.client.get(self.url)
		unfollow_url = reverse('blog:unfollow_author', kwargs={'pk': self.author.pk})
		self.assertContains(response, f'href="{unfollow_url}"')