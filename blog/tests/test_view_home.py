from django.test import TestCase
from django.urls import reverse, resolve
from ..views import HomeView

class HomeViewTests(TestCase):
	def setUp(self):
		url = reverse('blog:home')
		self.response = self.client.get(url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_function(self):
		view = resolve('/home/')
		self.assertEquals(view.view_class, HomeView)

	def test_csrf(self):
		self.assertContains(self, 'csrfmiddlewaretoken')

	def test_contains_search_bar(self):
		self.assertContains(self, '<input type="text" class="input" placeholder="search...">', 1)