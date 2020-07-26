from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..views import SignUpView

class SignUpTests(TestCase):
	def setUp(self):
		url = reverse('accounts:signup')
		self.response = self.client.get(url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view(self):
		view = resolve('/auth/signup/')
		self.assertEquals(view.func.view_class, SignUpView)

	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_contains_form(self):
		form = self.response.context.get('form')
		self.assertIsInstance(form, UserCreationForm)

	def test_form_inputs(self):
		self.assertContains(self.response, '<input', 7)
		self.assertContains(self.response, 'type="text"', 3)
		self.assertContains(self.response, 'type="email"', 1)
		self.assertContains(self.response, 'type="password"', 2)

class SuccessfulSignUpTests(TestCase):
	def setUp(self):
		url = reverse('accounts:signup')
		data = {
			'first_name': 'Jhonattan',
			'last_name': 'Millán',
			'username': 'username',
			'email': 'hola@gmail.com',
			'password1': 'wwwwwwwwwww1',
			'password2': 'wwwwwwwwwww1',
		}
		self.response = self.client.post(url, data)
		self.home_url = reverse('blog:home')

	def test_redirection(self):
		self.assertRedirects(self.response, self.home_url)

	def test_user_creation(self):
		self.assertTrue(User.objects.exists())

	def test_user_authentication(self):
		response = self.client.get(self.home_url)
		user = response.context.get('user')
		self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase):
	def setUp(self):
		url = reverse('accounts:signup')
		self.response = self.client.post(url, {})

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_form_errors(self):
		form = self.response.context.get('form')
		self.assertTrue(form.errors)

	def test_donot_create_user(self):
		self.assertFalse(User.objects.exists())