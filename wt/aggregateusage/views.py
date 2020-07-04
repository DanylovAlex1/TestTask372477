from rest_framework import viewsets
from itertools import chain
from .utils import *

from wt.aggregateusage.models import AggregatedVoiceUsage, AggregatedDataUsage
from wt.aggregateusage.serializers import AggregatedDataSerializer, \
    AggregatedVoiceSerializer, UserPriceDataLimitSerializer, VoiceUsageBySubscrSerializer, DataUsageBySubscrSerializer, \
    SubscriptionExceededLimitSerializer


class AggregatedDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = AggregatedDataUsage.objects.all()
    serializer_class = AggregatedDataSerializer


class AggregatedVoiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = AggregatedVoiceUsage.objects.all()
    serializer_class = AggregatedVoiceSerializer


class UserPriceDataLimitReached(viewsets.ReadOnlyModelViewSet):
    """  that API accepts a price limit as a request parameter.
    Return a list of:
    users,
    amount of how much price exceeded the limit.
    """
    queryset = None  # this is just for properly swagger work

    def get_queryset(self):
        limit = str(self.kwargs.get('limit'))
        query = f"""select id,user_id ,(S-{limit}) price from(
        select id,user_id, sum(price) S, usage_date from  aggregateusage_aggregateddatausage group by user_id)
        where price<=0"""
        queryset = AggregatedDataUsage.objects.raw(query)
        return queryset

    serializer_class = UserPriceDataLimitSerializer


class UsageMetricsBySubscrAndUsageType(viewsets.ReadOnlyModelViewSet):
    """ API accepts a price limit, from /to_dates, and usage type request parameters
    use date format as 'dd.mm.yyyy'
    type format as: 'voice' or 'data'
    Return a list of the:
    subscription id,
    total price of usage for the given dates,
    and total usage for any subscriptions that had usage during the given from and to dates
    """
    queryset = None  # this is just for properly swagger work

    def get_queryset(self):
        limit = str(self.kwargs.get('limit'))
        sd = str(self.kwargs.get('startdate'))
        ed = str(self.kwargs.get('enddate'))
        type = str(self.kwargs.get('type'))
        startdate = getDateFormatted(sd)
        enddate = getDateFormatted(ed)

        if type == 'data':
            query = f"""select id,(prc-{limit})price, kilobytes_used,sprint_subscription_id_id,att_subscription_id_id from(
            select id, sum(D.price)prc, sum(D.kilobytes_used)kilobytes_used, D.sprint_subscription_id_id, D.att_subscription_id_id
            from aggregateusage_aggregateddatausage D
            where usage_date between '{startdate}' and '{enddate}'
            group by D.sprint_subscription_id_id,D.att_subscription_id_id)
            Where price < 0"""
            queryset = AggregatedDataUsage.objects.raw(query)
        elif type == 'voice':
            query = f"""select id, (prc-{limit})price, seconds_used,sprint_subscription_id_id,att_subscription_id_id from(
            select id, sum(D.price)prc, sum(D.seconds_used)seconds_used, D.sprint_subscription_id_id, D.att_subscription_id_id
            from aggregateusage_aggregatedvoiceusage D
            where usage_date between '{startdate}' and '{enddate}'
            group by D.sprint_subscription_id_id,D.att_subscription_id_id)
            Where price < 0"""
            queryset = AggregatedVoiceUsage.objects.raw(query)
        return queryset

    def get_serializer_class(self):
        if self.kwargs.get('type') == 'data':
            return DataUsageBySubscrSerializer
        return VoiceUsageBySubscrSerializer


class SubscrExceedingUsagePriceLimit(viewsets.ReadOnlyModelViewSet):
    """  that API accepts a price limit as a request parameter.
    Return a list of the subscription id, type(s) of usage
    that exceeded the price limit, and by how much it's exceeded the limit.
    """
    queryset = None  # this is just for properly swagger work

    def get_queryset(self):
        limit = str(self.kwargs.get('limit'))
        querydata = f"""select id, sprint_subscription_id_id, att_subscription_id_id, (S-{limit}) price, 'data_usage' usage_type from(
        select id, sum(price) S, sprint_subscription_id_id, att_subscription_id_id 
        from  aggregateusage_aggregateddatausage 
        group by sprint_subscription_id_id,att_subscription_id_id)D
        where price<=0"""
        querysetdata = AggregatedDataUsage.objects.raw(querydata)

        queryvoice = f"""select id, sprint_subscription_id_id, att_subscription_id_id, (S-{limit}) price, 'voice_usage' usage_type from(
        select id, sum(price) S, sprint_subscription_id_id, att_subscription_id_id 
        from  aggregateusage_aggregatedvoiceusage 
        group by sprint_subscription_id_id,att_subscription_id_id)D
        where price<=0"""
        querysetvoice = AggregatedVoiceUsage.objects.raw(queryvoice)
        result_list = list(chain(querysetdata, querysetvoice))
        return result_list

    serializer_class = SubscriptionExceededLimitSerializer
