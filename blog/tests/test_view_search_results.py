from django.test import TestCase
from django.urls import reverse, resolve
from ..views import search_results
from ..models import BlogPost
from ..forms import SearchForm

class SearchReultsViewTests(TestCase):
	def setUp(self):
		url = reverse('blog:search_results')
		self.response = self.client.get(url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 302)
		self.assertRedirects(self.response, reverse('blog:home'))

class SuccessSearchResults(TestCase):
	def setUp(self):
		url = reverse('blog:search_results')
		self.query = 'food articles'
		self.response = self.client.post(url, {'query': self.query})

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_function(self):
		view = resolve('/results/')
		self.assertEquals(view.func, search_results)

	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_contains_search_bar(self):
		form = self.response.context.get('search_form')
		self.assertIsInstance(form, SearchForm)

	def test_contains_query(self):
		query = self.response.context.get('query')
		self.assertEquals(self.query, query)
		self.assertContains(self.response, self.query)

class InvalidSearchResults(TestCase):
	def setUp(self):
		url = reverse('blog:search_results')
		self.query = 'food articles'
		self.response = self.client.post(url, {})

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 302)
		self.assertRedirects(self.response, reverse('blog:home'))