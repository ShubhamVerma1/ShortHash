from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse

import uuid

from website.forms import CreateUrlHashForm
from website.models import UrlMapping, StoreClicks


class RedirectUrlView(View):
    """Redirect hased url to original url."""

    def get(self, request, hash_value):
        try:
            url_obj = UrlMapping.objects.get(
                hash_value=hash_value,
                expiry_counter__gt=0
            )
            url_obj.expiry_counter -= 1
            url_obj.save()
            StoreClicks.objects.create(url=url_obj)
            return redirect(url_obj.original_url)
        except:
            return render(
                request,
                'expired.html'
            )


class CreateHashUrlView(View):
    """Create hashed url."""

    def get(self, request):
        return render(
            request,
            'create_hash_url.html',
            {
                'form': CreateUrlHashForm()
            }
        )

    def post(self, request):
        form = CreateUrlHashForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request,
                'create_hash_url.html',
                {'form': form}
            )
        cleaned_data = form.cleaned_data
        hash_value = str(uuid.uuid4())#.replace('-', '')
        UrlMapping.objects.create(
            original_url=cleaned_data['url'],
            hash_value=hash_value,
            expiry_counter=cleaned_data['no_of_expiry_clicks']
        )
        return render(
            request,
            'hashed_url.html',
            {
                'hash_value': hash_value
            }
        )
