from django.db import models

class Banner(models.Model):

    title = models.CharField(max_length=200)

    subtitle = models.CharField(max_length=200)

    image = models.ImageField(upload_to="banners/")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title