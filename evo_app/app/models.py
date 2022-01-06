from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Meta:
    managed = True
    db_table = 'user'


class FullUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    last_login = models.DateTimeField(blank=True, null=True)
    date_first = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def get_object(self, queryset=None):
        obj = FullUser.objects.filter(pk=self.kwargs['id'])
        return obj