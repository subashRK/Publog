from django.shortcuts import get_object_or_404, redirect, render
from posts.forms import PostCreateForm, CommentCreateForm
from posts.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

def home(request):
  posts = Post.objects.all()
  search = request.GET.get("search")

  if search is not None:
    posts = Post.objects.filter(text__icontains=search)
  else:
    posts = Post.objects.all()

  return render(request, "posts.html", { "posts": posts })

def user_posts(request, id):
  user = get_object_or_404(User, id=id)
  posts = Post.objects.filter(user=user)

  return render(request, "posts.html", { "posts": posts })

def followers_posts(request):
  posts = Post.objects.filter(user__in=request.user.profile.following.all())
  return render(request, "posts.html", { "posts": posts })

def post_detail(request, id):
  post = get_object_or_404(Post, id=id)
  comments = Comment.objects.filter(post=post)

  return render(request, "post-detail.html", { "post": post, "comments": comments })

@login_required
def add_comment(request, id):
  post = get_object_or_404(Post, id=id)

  if request.method == "POST":
    form = CommentCreateForm(request.POST)
  else:
    form = CommentCreateForm()

  if form.is_valid():
    form = form.save(commit=False)
    form.post = post
    form.user = request.user
    form.save()

    next = request.GET.get("next")

    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  return render(request, "post-form.html", { "form": form, "title": "Create Comment" })

@login_required
def edit_comment(request, id):
  comment = get_object_or_404(Comment, id=id)
  next = request.GET.get("next")

  if comment.user.id != request.user.id:
    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  if request.method == "POST":
    form = CommentCreateForm(request.POST, instance=comment)
  else:
    form = CommentCreateForm(instance=comment)

  if form.is_valid():
    form.save()

    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  return render(request, "post-form.html", { "form": form, "title": "Edit Comment" })

@login_required
def add_post(request):
  if request.method == "POST":
    form = PostCreateForm(request.POST)
  else:
    form = PostCreateForm()

  if form.is_valid():
    form = form.save(commit=False)
    form.user = request.user
    form.save()

    next = request.GET.get("next")

    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  return render(request, "post-form.html", { "form": form, "title": "Create Post" })

@login_required
def delete_comment(request, id):
  comment = get_object_or_404(Comment, id=id)
  next = request.GET.get("next")

  if comment.user.id != request.user.id:
    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  if request.method == "POST":
    comment.delete()

    if next is not None:
      return redirect(next)
    else:
      redirect("all_posts")

  return render(request, "comment-delete.html")

@login_required
def edit_post(request, id):
  post = get_object_or_404(Post, id=id)
  next = request.GET.get("next")

  if post.user.id != request.user.id:
    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  if request.method == "POST":
    form = PostCreateForm(request.POST, instance=post)
  else:
    form = PostCreateForm(instance=post)

  if form.is_valid():
    form.save()

    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  return render(request, "post-form.html", { "form": form, "title": "Edit Post" })

@login_required
def delete_post(request, id):
  post = get_object_or_404(Post, id=id)
  next = request.GET.get("next")

  if post.user.id != request.user.id:
    if next is not None:
      return redirect(next)
    else:
      return redirect("all_posts")

  if request.method == "POST":
    post.delete()

    if next is not None:
      return redirect(next)
    else:
      redirect("all_posts")

  return render(request, "post-delete.html")

@login_required
def like_post(request, id):
  if request.method == "POST":
    post = get_object_or_404(Post, id=id)

    like_action = "added"

    if request.user in post.likes.all():
      post.likes.remove(request.user)
      like_action = "removed"
    else:
      post.likes.add(request.user)
      like_action = "added"

    return JsonResponse({ "message": f"Successfully {like_action} like!", "likes": post.likes.count(), "like_action": like_action }, status=200)

  return JsonResponse({ "message": "Invalid request method!" }, status=400)

@login_required
def like_comment(request, id):
  if request.method == "POST":
    comment = get_object_or_404(Comment, id=id)

    like_action = "added"

    if request.user in comment.likes.all():
      comment.likes.remove(request.user)
      like_action = "removed"
    else:
      comment.likes.add(request.user)
      like_action = "added"

    return JsonResponse({ "message": f"Successfully {like_action} like!", "likes": comment.likes.count(), "like_action": like_action }, status=200)

  return JsonResponse({ "message": "Invalid request method!" }, status=400)
