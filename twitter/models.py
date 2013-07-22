from django.db import models
from django.contrib.auth.models import User


class Twitter(models.Model):
    user = models.ForeignKey(User)
    status = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)  

    def __unicode__(self):
        return self.user

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    aboutme = models.TextField(blank=True, null=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __unicode__(self):
        return self.user

#Metodo Lambda
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
