# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)


class Product(models.Model):
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    price = models.FloatField()


class Sale(models.Model):
    id = models.Index
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    seller = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)

    @models.permalink
    def get_absolute_url(self):
        return ('sale_detail', (),
                {
                   'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.id)
        super(Sale, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.ordering
