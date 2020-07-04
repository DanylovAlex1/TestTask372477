from rest_framework import serializers
from wt.aggregateusage.models import AggregatedDataUsage, AggregatedVoiceUsage
from wt.usage.models import DataUsageRecord


class AggregatedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedDataUsage
        fields = '__all__'


class AggregatedVoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedVoiceUsage
        fields = '__all__'


class UserPriceDataLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedDataUsage
        fields = ['user_id', 'price']


class DataUsageBySubscrSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedDataUsage
        fields = ['price',
                  'kilobytes_used',
                  'att_subscription_id_id',
                  'sprint_subscription_id_id']


class VoiceUsageBySubscrSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedVoiceUsage
        fields = ['price',
                  'seconds_used',
                  'att_subscription_id_id',
                  'sprint_subscription_id_id']


class SubscriptionExceededLimitSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sprint_subscription_id_id=serializers.IntegerField()
    att_subscription_id_id=serializers.IntegerField()
    price=serializers.CharField()
    usage_type=serializers.CharField()

