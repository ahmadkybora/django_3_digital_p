from rest_framework import serializers

from .models import Package, Subscription

class PackageSerializer(Package):
    class Meta:
        model = Package
        fields = ('title', 'sku', 'description', 'avatar', 'price', 'duration')

class SubscriptionSerialzer(Subscription):
    class Meta:
        model = Subscription
        fields = ('package', 'created_time', 'expire_time')