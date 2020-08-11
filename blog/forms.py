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
			attrs={'rows': 15, 'placeholder': 'My first article!'}
		),
		help_text='Max characters amount is 25000.'
	)

	introduction = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 3, 'placeholder': 'Welcome to my article.'}
		),
		help_text='Introduction does not allow Markdown. More than one paragraph is not recommended. Max characters amount is 400.'
	)

	categories = forms.ModelMultipleChoiceField(
		queryset=BlogCategory.objects.all(),
		widget=forms.CheckboxSelectMultiple()
	)

	class Meta:
		model = BlogPost
		fields = ['title', 'thumbnail', 'introduction', 'body', 'categories', ]
		help_texts = {'thumbnail': 'Images with a 16x9 aspect ratio are recomemnded.'}

class NewCommentForm(forms.ModelForm):
	message = forms.CharField(
		widget=forms.Textarea(attrs={'rows': 3}),
		help_text='Max characters amount is 600. Comments do not allow Markdown.'
	)

	class Meta:
		model = BlogComment
		fields = ['message', ]