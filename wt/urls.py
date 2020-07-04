"""wt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from wt.att_subscriptions.views import ATTSubscriptionViewSet
from wt.plans.views import PlanViewSet
from wt.purchases.views import PurchaseViewSet
from wt.sprint_subscriptions.views import SprintSubscriptionViewSet
from wt.aggregateusage.views import AggregatedDataViewSet, AggregatedVoiceViewSet, UsageMetricsBySubscrAndUsageType
from wt.aggregateusage.views import UserPriceDataLimitReached

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

router.register(r'att_subscriptions', ATTSubscriptionViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sprint_subscriptions', SprintSubscriptionViewSet)

# router.register('aggregateddata/', AggregatedDataViewSet)
# router.register('aggregatedvoice/', AggregatedVoiceViewSet)

# router.register('users-outoflimit/', UserPriceDataLimitReached)
# router.register('users-outoflimit/<int:limit>/', UserPriceDataLimitReached)
# router.register('subscr-out-oflimit/<int:limit>/<str:startdate>/<str:enddate>/<str:type>',
#                 UsageMetricsBySubscrAndUsageType)

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^api/', include((router.urls, 'api'), namespace='api')),
    path('aggregatedusage/', include('wt.aggregateusage.urls')),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
