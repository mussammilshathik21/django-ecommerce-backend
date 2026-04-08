from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    CATEGORY_CHOICES = [
        ("shirt", "Shirt"),
        ("tshirt","Tshirt"),
        ("pant", "Pant"),
        ("shoe", "Shoe"),
        ("slipper", "Slipper"),
        ("chain", "Chain"),
        ("watch", "Watch"),
        ("ring", "Ring"),
        ("belt", "Belt"),
    ]

    name = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    image = models.ImageField(upload_to="products/")

    description = models.TextField(blank=True)

    sizes = models.JSONField(default=list, blank=True)

    is_trending = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    

class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"