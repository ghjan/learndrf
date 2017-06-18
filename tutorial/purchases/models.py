#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Purchase(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)
    product_name = models.CharField(max_length=100, blank=True, default='', db_index=True)
    price = models.FloatField(default=0, verbose_name=u'原价')
    proprice = models.FloatField(blank=True, null=True, verbose_name=u'促销价')
    amount = models.IntegerField(default=1)
    buyer = models.ForeignKey('auth.User', related_name='purchases', on_delete=models.CASCADE)

    class Meta:
        app_label = "purchases"
        verbose_name = u'购买详情'
        verbose_name_plural = u'购买详情'
        ordering = ('created',)

        # def get_absolute_url(self):
        #     return reverse('purchase-detail', args=[str(self.id)])
