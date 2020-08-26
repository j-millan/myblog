from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('explore/', views.ExploreView.as_view(), name='explore'),
	path('results/', views.search_results, name='search_results'),
	path('article/new/', views.BlogPostCreateView.as_view(), name='new_article'),
	path('article/<slug:slug>/', views.BlogPostDetailView.as_view(), name='article'),
	path('article/<slug:slug>/comment/<int:pk>/edit/', views.BlogCommentUpdateView.as_view(), name='edit_comment'),
	path('author/<int:pk>/', views.UserDetailView.as_view(), name='author_profile'),
	path('author/<int:pk>/follow/', views.follow_author, name='follow_author'),
	path('author/<int:pk>/unfollow/', views.unfollow_author, name='unfollow_author')
]