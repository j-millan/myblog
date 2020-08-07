from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from ..views import HomeView
from ..models import BlogPost
from ..forms import SearchForm
from .cases import UserLoginTestCase

class HomeViewTests(UserLoginTestCase):
	def setUp(self):
		self.url = reverse('blog:home')
		self.response = self.client.get(self.url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_function(self):
		view = resolve('/')
		self.assertEquals(view.func.view_class, HomeView)

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

	def test_contains_new_article_button(self):
		super().setUp()
		new_post_url = reverse('blog:new_article')
		self.client.login(username=self.username, password=self.password)
		response = self.client.get(self.url)
		self.assertContains(response, f'href="{new_post_url}"')