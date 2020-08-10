from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, DetailView, CreateView, UpdateView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from .forms import SearchForm, NewArticleForm, NewCommentForm
from .models import BlogPost, UserFollowing, BlogComment

def order_by_attribute(listset, attr):
	l = list(listset)
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			if getattr(l[i], attr).count() < getattr(l[j], attr).count():
				l[i], l[j] = l[j], l[i]

	return l

class SearchFormMixin(ContextMixin):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search_form'] = SearchForm()
		return context

@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView, SearchFormMixin):
    model = BlogPost
    form_class = NewArticleForm
    template_name = "blog/new_blog_post.html"

    def form_valid(self, form):
    	article = form.save(commit=False)
    	article.author = self.request.user
    	article.save()
    	form.save_m2m()
    	return redirect('blog:article', slug=article.slug)

class HomeView(TemplateView, SearchFormMixin):
	template_name = 'blog/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_articles'] = BlogPost.objects.order_by('-date_published')[:12]
		context['popular_articles'] = context['latest_articles']
		context['popular_authors'] = User.objects.all()[:12]
		return context

class BlogPostDetailView(CreateView, SearchFormMixin):
	model = BlogComment
	form_class = NewCommentForm
	template_name = "blog/blog_post.html"

	def form_valid(self, form):
		article = get_object_or_404(BlogPost, slug=self.kwargs['slug'])
		self.object = form.save(commit=False)
		self.object.created_by = self.request.user
		self.object.article = article
		self.object.save()
		return redirect('blog:article', slug=article.slug)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['article'] = get_object_or_404(BlogPost, slug=self.kwargs['slug'])
		return context

class UserDetailView(DetailView, SearchFormMixin):
    model = User
    context_object_name = 'author'
    template_name = "blog/user_profile.html"


@login_required
def follow_author(request, pk):
	author = get_object_or_404(User, pk=pk)
	new_follower = UserFollowing.objects.filter(user=request.user, user_following=author)
	if not new_follower.exists():
		new_follower = UserFollowing.objects.create(user=request.user, user_following=author)

	return redirect('blog:author_profile', pk=pk)

@login_required
def unfollow_author(request, pk):
	author = get_object_or_404(User, pk=pk)
	follower = UserFollowing.objects.filter(user=request.user, user_following=author)
	if follower.exists():
		follower.delete()

	return redirect('blog:author_profile', pk=pk)
	
def search_results(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			articles = BlogPost.objects.all()
			return render(request, 'blog/search_results.html', {'articles': articles, 'search_form': form, 'query': form.cleaned_data.get('query')})
	
	else:
		form = SearchForm()

	return redirect('blog:home')
