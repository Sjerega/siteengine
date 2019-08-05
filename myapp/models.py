from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def slug_gen(s):
    return slugify(s, allow_unicode=True) + '-' + str(int(time()))


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='products')
    date_add = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_gen(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_gen(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)
