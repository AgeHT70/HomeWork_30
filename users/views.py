from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializer import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserDestroySerializer


class UserListView(ListAPIView):
    queryset = User.objects.all().annotate(total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by(
        'username')
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
