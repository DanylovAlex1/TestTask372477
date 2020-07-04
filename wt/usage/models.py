from django.db import models

from wt.att_subscriptions.models import ATTSubscription
from wt.sprint_subscriptions.models import SprintSubscription


class DataUsageRecord(models.Model):
    """Raw data usage record for a subscription"""
    att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateField(null=False)
    kilobytes_used = models.IntegerField(null=False)

    def save(self, *args, **kwargs):
        if self.sprint_subscription_id:
            self.price = SprintSubscription.ONE_KILOBYTE_PRICE * self.kilobytes_used
        elif self.att_subscription_id:
            self.price = ATTSubscription.ONE_KILOBYTE_PRICE * self.kilobytes_used
        super(DataUsageRecord, self).save(*args, **kwargs)


class VoiceUsageRecord(models.Model):
    """Raw voice usage record for a subscription"""
    att_subscription_id = models.ForeignKey(ATTSubscription, null=True, on_delete=models.PROTECT)
    sprint_subscription_id = models.ForeignKey(SprintSubscription, null=True, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateField(null=False)
    seconds_used = models.IntegerField(null=False)

    def save(self, *args, **kwargs):
        if self.sprint_subscription_id:
            self.price = SprintSubscription.ONE_SECOND_PRICE * self.seconds_used
        elif self.att_subscription_id:
            self.price = ATTSubscription.ONE_SECOND_PRICE * self.seconds_used
        super(VoiceUsageRecord, self).save(*args, **kwargs)
