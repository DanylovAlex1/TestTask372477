from django.db import models
from django.contrib.auth.models import User
from wt.att_subscriptions.models import ATTSubscription
from wt.sprint_subscriptions.models import SprintSubscription


class AggregatedDataUsage(models.Model):
    """
    this model will use the data from DataUsageRecord
     and store aggregated kilobytes_used segmented by date
    """
    user = models.ForeignKey(User,null=False, on_delete=models.PROTECT)
    att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    usage_date = models.DateField(null=False)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    kilobytes_used = models.IntegerField(null=False)


class AggregatedVoiceUsage(models.Model):
    """
    this model will use the data from VoiceUsageRecord
     and store aggregated seconds_used segmented by date
    """
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    usage_date = models.DateField(null=False)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    seconds_used = models.IntegerField(null=False)

