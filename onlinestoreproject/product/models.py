import uuid
from django.db import models
from django.core.validators import MinValueValidator

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Brand(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, to_field='name', null=True)
    weight = models.FloatField()
    dimensions = models.CharField(max_length=255, null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], default=500)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name')

    def __str__(self):
        return self.product.name + self.category.name

class ProductImage(models.Model):
    img = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name')

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name')
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=10)

    def __str__(self):
        return self.product.name

class PriceRange(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    min = models.IntegerField(default=500, validators=[MinValueValidator(0)])
    max = models.IntegerField(default=500,validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('min', 'max')

    def __str__(self):
        return str(self.key)

class Availability(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.key)


@receiver(post_save, sender=Product)
def create_product_stock(sender, instance=None, created=False, **kwargs):
    if created:
        Stock.objects.create(product = instance)


    