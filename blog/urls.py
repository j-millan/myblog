from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('results/', views.search_results, name='search_results'),
	path('article/new/', views.BlogPostCreateView.as_view(), name='new_article'),
	path('article/<slug:slug>/', views.BlogPostDetailView.as_view(), name='article')
]