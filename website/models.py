from django.db import models


class UrlMapping(models.Model):
    """Store original url to short url mapping."""

    original_url = models.URLField()
    expiry_counter = models.IntegerField(default=1)
    hash_value = models.CharField(max_length=10, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class StoreClicks(models.Model):
    clicked_at = models.DateTimeField(auto_now_add=True)
    url = models.ForeignKey(UrlMapping, on_delete=models.CASCADE)
