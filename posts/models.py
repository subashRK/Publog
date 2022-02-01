from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
  text = models.TextField(null=False, blank=False)
  likes = models.ManyToManyField(User, related_name="likes")
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ("-timestamp",)

  def __str__(self):
      return self.user.username + " | " + self.text[:15]

class Comment(models.Model):
  post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
  user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
  likes = models.ManyToManyField(User, related_name="comment_likes")
  comment = models.TextField(null=False, blank=False)
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ("-timestamp",)
    
  def __str__(self):
      return self.user.username +  " | " + self.comment[:15]
