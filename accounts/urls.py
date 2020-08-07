from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('settings/', views.UserUpdateView.as_view(), name='settings'),
	path('edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),
	path('password/change/', 
		auth_views.PasswordChangeView.as_view(
			template_name='accounts/password_change/password_change.html',
			success_url=reverse_lazy('accounts:password_change_done')
		),
		name='password_change'
	),
	path('password/change/done/', views.PasswordChangeDone.as_view(), name='password_change_done')
]