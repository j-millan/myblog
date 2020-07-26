from django.test import TestCase
from django.urls import reverse, resolve
from ..views import HomeView
from ..models import BlogPost
from ..forms import SearchForm

class HomeViewTests(TestCase):
	def setUp(self):
		url = reverse('blog:home')
		self.response = self.client.get(url)

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