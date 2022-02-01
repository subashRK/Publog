from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import *

urlpatterns = [
  path("login/", auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
  path("signup/", signup, name="signup"),
  path("update/", update_user, name="update_user"),
  path("update-profile/", update_profile, name="update_profile"),
  path("profile/<int:id>/", profile, name="profile"),
  path("follow/<int:id>/", follow, name="follow"),
  path("logout/", LogoutView.as_view(), name="logout"),
  path("password/", auth_views.PasswordChangeView.as_view(template_name="password/change-password.html"), name="update_password"),
  path("update-password-done/", auth_views.PasswordChangeDoneView.as_view(template_name="password/change-password-done.html"), name="password_change_done"),
  path("password-reset/", auth_views.PasswordResetView.as_view(template_name="password/password-reset.html"), name="password_reset"),
  path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password/password-reset-confirm.html"), name="password_reset_confirm"),
  path("password-reset-done/", auth_views.PasswordResetDoneView.as_view(template_name="password/password-reset-done.html"), name="password_reset_done"),
  path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password/password-reset-complete.html"), name="password_reset_complete"),
]
