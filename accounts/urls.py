from django.urls import path, re_path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('settings/', views.UserUpdateView.as_view(), name='settings'),
	path('edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),

	path('password/reset/', auth_views.PasswordResetView.as_view(
		template_name='accounts/password_reset/password_reset.html',
		email_template_name='accounts/password_reset/password_reset_email.html',
		subject_template_name='accounts/password_reset/password_reset_subject.html',
		success_url=reverse_lazy('accounts:password_reset_done')
		),
		name='password_reset'
	),
	path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset/password_reset_done.html'), name='password_reset_done'),
	re_path(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
		auth_views.PasswordResetConfirmView.as_view(
			template_name='accounts/password_reset/password_reset_confirm.html',
			success_url=reverse_lazy('accounts:passsword_reset_complete')
		),
		name='password_reset_confirm'
	),
	path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset/password_reset_complete.html'), name='passsword_reset_complete'),

	path('password/change/', 
		auth_views.PasswordChangeView.as_view(
			template_name='accounts/password_change/password_change.html',
			success_url=reverse_lazy('accounts:password_change_done')
		),
		name='password_change'
	),
	path('password/change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
]