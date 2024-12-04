from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    preferences = models.JSONField(default=dict)  # Stores user's anime preferences as JSON
    watched_anime = models.JSONField(default=list)  # Stores a list of watched anime titles (optional)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Custom related name to resolve conflict
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Custom related name to resolve conflict
        blank=True,
    )


class CachedAnime(models.Model):
    anime_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    genres = models.JSONField()
    popularity = models.IntegerField()

