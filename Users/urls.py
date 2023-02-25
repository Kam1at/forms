from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetConfirmView
from django.urls import path
from Users.apps import UsersConfig
from Users.views import CustomLoginView, UserEditProfileView, UserCreateProfileView, MyPasswordChangeView, \
    user_activation
from Users.views import CustomPasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('register/', UserCreateProfileView.as_view(), name='register'),
    path('password/', MyPasswordChangeView.as_view(), name='change_passwd'),
    path('activate/<str:token>/', user_activation, name='activate'),
    path('password_reset_confirm/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>', CustomPasswordResetView.as_view(), name='password_reset_confirm'),
]
