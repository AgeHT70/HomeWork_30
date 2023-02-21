import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView

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


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({"id": category.id,
                             "name": category.name
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesCreateView(CreateView):
    model = Categories
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Categories.objects.create(name=category_data["name"])

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesUpdateView(UpdateView):
    model = Categories
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)
        self.object.name = category_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        }, status=200)


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


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({"id": ads.id,
                             "name": ads.name,
                             "author": ads.author,
                             "price": ads.price,
                             "description": ads.description,
                             "is_published": ads.is_published,
                             "image": ads.image,
                             "category": ads.category
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    fields = ["name", "author", "price", "description", "is_published", "image", "category"]

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)
        ads = Ads.objects.create(
            name=ads_data["name"],
            author=ads_data["author"],
            price=ads_data["price"],
            description=ads_data["description"],
            is_published=ads_data["is_published"],
            image=ads_data["image"],
            category=ads_data["category"]
        )

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": ads.image,
            "category": ads.category
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ["name", "author", "price", "description", "is_published", "image", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ads_data = json.loads(request.body)

        self.object.name = ads_data["name"]
        self.object.author = ads_data["author"]
        self.object.price = ads_data["price"]
        self.object.description = ads_data["description"]
        self.object.is_published = ads_data["is_published"]
        self.object.image = ads_data["image"]
        self.object.category = ads_data["category"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image,
            "category": self.object.category
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        }, status=200)
