from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SignUpForm, UpdateProfileForm
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

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy('accounts:edit_profile')

    def get_object(self):
    	return self.request.user.profile

    def form_valid(self, form):
    	super().form_valid(form)
    	return redirect('blog:author_profile', pk=self.object.user.pk)