from django.urls import path
from .views import AggregatedDataViewSet, AggregatedVoiceViewSet, \
    UserPriceDataLimitReached, UsageMetricsBySubscrAndUsageType, SubscrExceedingUsagePriceLimit

urlpatterns = [

    path('data/', AggregatedDataViewSet.as_view({'get': 'list'})),
    path('voice/', AggregatedVoiceViewSet.as_view({'get': 'list'})),

    path('user-outoflimit/<int:limit>/', UserPriceDataLimitReached.as_view({'get': 'list'})),

    path('subscr-outoflimit/<int:limit>/<str:startdate>/<str:enddate>/<str:type>',
         UsageMetricsBySubscrAndUsageType.as_view({'get': 'list'})),

    path('subscr-outoflimit/<int:limit>/', SubscrExceedingUsagePriceLimit.as_view({'get': 'list'})),


]
