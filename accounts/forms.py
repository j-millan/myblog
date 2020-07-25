from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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