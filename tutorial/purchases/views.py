#!/usr/bin/env python
# encoding: utf-8

from rest_framework import permissions
from rest_framework import viewsets
from purchases.permissions import IsOwnerOrReadOnly

from purchases.models import Purchase
from purchases.serializers import PurchaseSerializer


class PurchasesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    You can have an action only on your purchases.

    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Purchase.objects.filter(buyer=user)
