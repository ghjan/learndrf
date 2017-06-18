#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = []

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    # url(r'^', include('snippets.urls')),
    # url(r'^purchases/', include('purchases.urls')),
    url(r'^admin/', admin.site.urls),
    # Login and logout views for the browsable API
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^schema/$', schema_view),

]
from django.conf.urls import url, include
# from snippets import views
import snippets.views
import purchases.views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', snippets.views.SnippetViewSet)
router.register(r'users', snippets.views.UserViewSet)
router.register(r'purchases', purchases.views.PurchasesViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns += [
    url(r'^', include(router.urls)),
]
