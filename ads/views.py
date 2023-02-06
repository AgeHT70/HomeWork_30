import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
# from django.views.generic.list import ListView

from ads.models import Categories, Ads


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for category in self.object_list:
            response.append({"id": category.id, "name": category.name})

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        category_data = json.loads(request.body)
        category = Categories()
        category.name = category_data["name"]
        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for ads in self.object_list:
            response.append({"id": ads.id,
                             "name": ads.name,
                             "author": ads.author,
                             "price": ads.price,
                             "description": ads.description,
                             "address": ads.address,
                             "is_published": ads.is_published
                             })

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ads_data = json.loads(request.body)
        ads = Ads()

        ads.name = ads_data["name"]
        ads.author = ads_data["author"]
        ads.price = ads_data["price"]
        ads.description = ads_data["description"]
        ads.address = ads_data["address"]
        ads.is_published = ads_data["is_published"]

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        }, safe=False)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = get_object_or_404(Ads, *args, **kwargs)

        return JsonResponse({"id": ads.id,
                             "name": ads.name,
                             "author": ads.author,
                             "price": ads.price,
                             "description": ads.description,
                             "address": ads.address,
                             "is_published": ads.is_published
                             }, safe=False)


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Categories, *args, **kwargs)

        return JsonResponse({"id": category.id,
                             "name": category.name
                             }, safe=False)
