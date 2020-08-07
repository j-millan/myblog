from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.utils.text import slugify
from django.conf import settings
from ..views import BlogPostCreateView
from ..models import BlogPost, BlogCategory
from ..forms import NewArticleForm
import os

class NewArticleViewTestCase(TestCase):
	def setUp(self):
		self.username = 'username'
		self.password = '123'
		self.user = User.objects.create_user(username=self.username, email='email@email.com', password=self.password)
		self.url = reverse('blog:new_article')

class NewArticleViewLoginRequiredTests(NewArticleViewTestCase):
	def setUp(self):
		super().setUp()
		self.response = self.client.get(self.url)

	def test_redirection(self):
		new_article_url = reverse('blog:new_article')
		login_url = reverse('accounts:login')
		self.assertRedirects(self.response, f'{login_url}?next={new_article_url}')

class NewArticleViewTests(NewArticleViewTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.response = self.client.get(self.url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_function(self):
		view = resolve('/article/new/')
		self.assertEquals(view.func.view_class, BlogPostCreateView)

	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_contains_form(self):
		form = self.response.context.get('form')
		self.assertIsInstance(form, NewArticleForm)

	def test_form_inputs(self):
		self.assertContains(self.response, '<input', 5)
		self.assertContains(self.response, '<textarea', 1)
		self.assertContains(self.response, 'type="file"', 1)
		self.assertContains(self.response, 'id="id_categories"', 1)

class SuccessfulNewArticleViewTests(NewArticleViewTestCase):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)

		upload_file = open(os.path.join(settings.BASE_DIR,'static/img/logopng.png'), 'rb')
		png = SimpleUploadedFile(upload_file.name, upload_file.read())

		cat = BlogCategory.objects.create(name='Off-topic', tag_color='is-light')
		self.title = 'This is an article'

		data = {
			'title': self.title,
			'body': 'aaaaa',
			'categories': {cat}
		}
		file_dict = {
			'thumbnail': png
		}
		self.form = NewArticleForm(data=data, files=file_dict)

	def test_redirection(self):
		pass
		#article_url = reverse('blog:article', kwargs={'slug': slugify(f'{self.user.username}-{self.title}')})
		#self.assertRedirects(self.response, article_url)

	def test_form_valid(self):
		self.assertTrue(self.form.is_valid())

class InvalidNewArticleViewTests(NewArticleViewTests):
	def setUp(self):
		super().setUp()
		self.client.login(username=self.username, password=self.password)
		self.response = self.client.post(self.url, {})

	def test_redirection(self):
		self.assertEquals(self.response.status_code, 200)

	def test_article_not_created(self):
		self.assertFalse(BlogPost.objects.exists())

	def test_form_errors(self):
		form = self.response.context.get('form')
		self.assertTrue(form.errors)