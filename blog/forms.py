from django import forms
from .models import BlogPost, BlogCategory, BlogComment

class SearchForm(forms.Form):
	query = forms.CharField(
		max_length=75,
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Search content...'})
	)

class NewArticleForm(forms.ModelForm):
	body = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 15, 'placeholder': 'XD'}
		),
	)

	categories = forms.ModelMultipleChoiceField(
		queryset=BlogCategory.objects.all(),
		widget=forms.CheckboxSelectMultiple()
	)

	class Meta:
		model = BlogPost
		fields = ['title', 'thumbnail', 'body', 'categories', ]

class NewCommentForm(forms.ModelForm):
	message = forms.CharField(
		widget=forms.Textarea(attrs={'rows': 3}),
		required=True
	)

	class Meta:
		model = BlogComment
		fields = ['message', ]