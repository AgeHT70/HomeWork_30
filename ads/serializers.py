from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from ads.models import Ads


class AdsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    category = serializers.CharField()
    locations = SerializerMethodField()

    class Meta:
        model = Ads
        fields = '__all__'

    def get_locations(self, ads):
        return [location.name for location in ads.author_id.locations.all()]
