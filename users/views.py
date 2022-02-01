from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from users.forms import *
from django.contrib.auth.views import LogoutView as LogoutClassView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signup(request):
  if request.method == "POST":
    form = CreateUserForm(request.POST)
  else:
    form = CreateUserForm()

  if form.is_valid():
    form.save()
    return redirect("login")

  return render(request, "signup.html", { "form": form })

@login_required
def update_user(request):
  if request.method == "POST":
    form = UpdateUserForm(request.POST, instance=request.user)
  else:
    form = UpdateUserForm(instance=request.user)

  if form.is_valid():
    form.save()
    return redirect("profile")

  return render(request, "update-user.html", { "form": form })

@login_required
def update_profile(request):
  if request.method == "POST":
    print(request.FILES)
    form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
  else:
    form = UpdateUserProfileForm(instance=request.user.profile)

  if form.is_valid():
    form.save()
    return redirect("profile")

  return render(request, "update-profile.html", { "form": form })

def profile(request, id):
  user = get_object_or_404(User, id=id)
  return render(request, "profile.html", { "user_data": user })

@login_required
def follow(request, id):
  if request.method == "POST" and request.user.id != id:
    user = get_object_or_404(User, id=id)

    follow_action = "added"

    if request.user in user.profile.followers.all():
      user.profile.followers.remove(request.user)
      request.user.profile.following.remove(user)
      follow_action = "removed"
    else:
      user.profile.followers.add(request.user)
      request.user.profile.following.add(user)
      follow_action = "added"

    return JsonResponse({ "message": f"Successfully {follow_action} a follower!", "followers_count": user.profile.followers.count(), "follow_action": follow_action }, status=200)

  return JsonResponse({ "message": "Invalid request method!" }, status=400)

class LogoutView(LoginRequiredMixin, LogoutClassView):
  template_name = "logout.html"
  redirect_field_name = None
