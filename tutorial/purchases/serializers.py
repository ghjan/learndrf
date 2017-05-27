#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 5/25/17 5:15 PM
"""

from rest_framework import serializers
from purchases.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    # url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Purchase
        fields = ('url', 'product_name', 'price', 'proprice', 'amount',
                  'buyer')
