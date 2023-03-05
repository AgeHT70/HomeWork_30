from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


from ads.models import Ads, Selection


class AdsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    category = serializers.CharField()
    locations = SerializerMethodField()

    class Meta:
        model = Ads
        fields = '__all__'

    def get_locations(self, ads):
        return [location.name for location in ads.author_id.locations.all()]


class AdsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['id']


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdsListSerializer(many=True)

    class Meta:
        model = Selection
        fields = ["id", "items", "name", "owner"]


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]
