from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
  user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
  bio = models.TextField(default="I too have a Publog account!")
  image = models.ImageField(upload_to="users/", default="default-user-profile.png")
  followers = models.ManyToManyField(User, related_name="followers")
  following = models.ManyToManyField(User, related_name="following")

  def __str__(self):
    return self.user.username
