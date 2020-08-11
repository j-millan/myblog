from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
	email = forms.CharField(
		max_length=80,
		required=True,
		widget=forms.EmailInput()
	)

	first_name = forms.CharField(
		max_length=60,
		required=True,
		widget=forms.TextInput()
	)

	last_name = forms.CharField(
		max_length=60,
		required=True,
		widget=forms.TextInput()
	)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
	email = forms.EmailField()

	first_name = forms.CharField(
		max_length=60,
		required=True,
		widget=forms.TextInput()
	)

	last_name = forms.CharField(
		max_length=60,
		required=True,
		widget=forms.TextInput()
	)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

class UpdateProfileForm(forms.ModelForm):
	about = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 4, 'placeholder': 'About me'}
		),
		required=False,
		help_text = 'Max characters amount is 250.'
	)

	class Meta:
		model = Profile
		fields = ['profile_picture', 'about', 'phone_number', 'instagram_profile', 'facebook_page', 'twitter_profile']
		help_texts = {'profile_picture': 'Square images are recomended.'}