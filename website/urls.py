"""Endpoints of APIs for user."""

from django.urls import path

from website.views import RedirectUrlView, CreateHashUrlView

app_name = 'website'

urlpatterns = [
    path(r'<uuid:hash_value>', RedirectUrlView.as_view(),
         name='redirect_urls'),
    path('create', CreateHashUrlView.as_view(),
         name='create_hash_urls'),
]
