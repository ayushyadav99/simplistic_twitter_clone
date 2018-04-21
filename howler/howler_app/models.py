from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by',symmetrical=False)
    picture = models.ImageField(upload_to='profile_picture',blank=True,default = 'profile_picture/blankgravatar.jpg')
    def __str__(self):
        return self.user.username

class Howler(models.Model):
    howl = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)
