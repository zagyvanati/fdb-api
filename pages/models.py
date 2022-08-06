from django.db import models

class Page(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=10000, blank=True)

    def __str__(self) -> str:
        return self.slug