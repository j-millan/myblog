from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, DetailView, CreateView, UpdateView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from itertools import chain
from .forms import SearchForm, NewArticleForm, NewCommentForm
from .models import BlogPost, UserFollowing, BlogComment, BlogCategory

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

@method_decorator(login_required, name='dispatch')
class BlogCommentUpdateView(UpdateView):
    model = BlogComment
    form_class = NewCommentForm
    template_name = "blog/edit_comment.html"

    def get(self, request, *args, **kwargs):
    	comment = self.get_object()
    	form = NewCommentForm()
    	form.initial['message'] = comment.message
    	if request.user == comment.created_by:
    		return render(request, 'blog/edit_comment.html', {'comment': comment, 'form': form})
    	
    	return redirect('blog:article', slug=self.kwargs['slug'])

    def get_success_url(self):
    	return reverse_lazy('blog:article', kwargs={'slug': self.kwargs['slug']})

class HomeView(TemplateView, SearchFormMixin):
	template_name = 'blog/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		user = self.request.user
		latest = list()
		following = list()
		if user.is_authenticated:
			if user.following.exists():
				following = [f.user_following for f in (user.following.all())] 
				latest = BlogPost.objects.filter(author__in=following).order_by('-date_published')[:12]
				following.append(user)

		fill = BlogPost.objects.exclude(author__in=following).order_by('-date_published')
		latest = list(chain(latest, fill[:12]))
		context['latest_articles'] = latest[:12]
		context['popular_articles'] = context['latest_articles']
		context['popular_authors'] = User.objects.all()[:12]
		return context

class ExploreView(TemplateView, SearchFormMixin):
	template_name = "blog/explore.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category_sets = list()
		for c in (BlogCategory.objects.all()):
			articles = BlogPost.objects.filter(categories__in=[c])[:8]
			category_set = {'category': c, 'articles': articles}
			category_sets.append(category_set)

		context['category_sets'] = category_sets
		context['popular_authors'] = order_by_attribute(User.objects.all()[:20], 'followers')
		return context

class CategoryPostsView(DetailView, SearchFormMixin):
	template_name = 'blog/category_articles.html'
	model = BlogCategory
	context_object_name = 'category'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category = self.get_object()
		context['articles'] = BlogPost.objects.filter(categories__in=[category])
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
			search_query = form.cleaned_data.get('query')
			articles = []
			for a in (BlogPost.objects.all()):
				if a.title.lower().find(search_query.lower()) != -1:
					articles.append(a)

			return render(request, 'blog/search_results.html', {'articles': articles, 'search_form': form, 'query': search_query})
	
	else:
		form = SearchForm()

	return redirect('blog:home')