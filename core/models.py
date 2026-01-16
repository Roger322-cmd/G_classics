from django.db import models
from ckeditor.fields import RichTextField

class SiteSettings(models.Model):
    primary_color = models.CharField(max_length=7, default="#0d6efd")
    secondary_color = models.CharField(max_length=7, default="#6c757d")
    glass_background = models.CharField(max_length=20, default="rgba(255,255,255,0.08)")
    glass_border_color = models.CharField(max_length=20, default="rgba(255,255,255,0.25)")
    featured_title = models.CharField(max_length=100, default="Featured Classics")

    class Meta:
        verbose_name = "Theme & Site Settings"
        verbose_name_plural = "Theme & Site Settings"

    def __str__(self):
        return "Theme Settings"



class StaticPage(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
