from django.db import models
from account.models import Account
from product.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid

class Review(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='username')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    date_posted = models.DateTimeField(auto_now_add=True, editable=True)

    # def __str__(self):
    #     return self.title + ", " + self.product.name + ", " + self.user.username
    