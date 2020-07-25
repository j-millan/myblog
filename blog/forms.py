from django import forms
from .models import BlogPost

class SearchForm(forms.Form):
	query = forms.CharField(
		max_length=75,
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'search...'})
	)

class NewArticleForm(forms.ModelForm):
	body = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 15, 'placeholder': 'XD'}
		), 
		max_length=4000,
	)

	class Meta:
		model = BlogPost
		fields = ['title', 'thumbnail', 'body', 'category', ]