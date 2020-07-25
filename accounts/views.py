from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Profile
from blog.views import SearchFormMixin

class SignUpView(CreateView, SearchFormMixin):
	model = User
	form_class = SignUpForm
	template_name = 'accounts/signup.html'

	def form_valid(self, form):
		user = form.save()
		profile = Profile.objects.create(user=user)
		profile.save()
		login(self.request, user)
		return redirect('blog:home')