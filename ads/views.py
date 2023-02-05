from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from ads.models import Categories, Ads


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoriesListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for category in self.object_list:
            response.append({"id": category.id, "name": category.name})

        return JsonResponse(response, safe=False, status=200)


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for ads in self.object_list:
            response.append({"id": ads.id, "name": ads.name})

        return JsonResponse(response, safe=False, status=200)
