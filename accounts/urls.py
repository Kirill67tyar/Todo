from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'), # http://127.0.0.1:8000/accounts/login/
    path('login/', auth_views.LoginView.as_view(), name='login'),   # Пока мы берем класс формы из коробки
    # логина из коробки джанго он редиректит на success_url - /accounts/profile/
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('pwd-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('pwd-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('pwd-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('pwd-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# login мы свой определили, но пока будем использовть готовые классы из django.contrib.auth
# папка registration в templates - создавалась для них
