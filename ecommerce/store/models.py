from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, blank=False, null = False)
    slug = models.SlugField(max_length=200, unique=True)
    meta_title = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/category')

    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )

    status  = models.IntegerField(default=1, choices=STATUS)
    
    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=200, blank=False, null = False)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True, blank=False, null = False)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product', blank=True, null=True)
    image = models.ImageField(upload_to='images/product')
    meta_title = models.TextField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    UNAVAILABLE = 0
    AVAILABLE = 1
    STATUS = (
        (UNAVAILABLE, _('Unavailable')),
        (AVAILABLE, _('Available')),
    )
    status  = models.IntegerField(default=1, choices=STATUS)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    