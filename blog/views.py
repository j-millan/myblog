from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, DetailView, CreateView, UpdateView
from django.views.generic.base import ContextMixin
from django.utils.decorators import method_decorator
from .forms import SearchForm, NewArticleForm
from .models import BlogPost

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

class HomeView(TemplateView, SearchFormMixin):
	template_name = 'blog/home.html'

	def get_context_data(self):
		context = super().get_context_data()
		context['latest_articles'] = BlogPost.objects.order_by('-date_published')[:12]
		context['popular_articles'] = order_by_attribute(BlogPost.objects.all(), 'comments')[:12]
		context['popular_authors'] = order_by_attribute(User.objects.all()[:12], 'followers')
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

class BlogPostDetailView(DetailView, SearchFormMixin):
    model = BlogPost
    context_object_name = 'article'
    slug_url_kwarg = 'slug'
    template_name = "blog/blog_post.html"

def search_results(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			articles = BlogPost.objects.all()
			return render(request, 'blog/search_results.html', {'articles': articles, 'search_form': form, 'query': form.cleaned_data.get('query')})
	
	else:
		form = SearchForm()

	return redirect('blog:home')