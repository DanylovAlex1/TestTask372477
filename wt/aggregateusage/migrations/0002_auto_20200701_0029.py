from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprint_subscriptions', '0001_initial'),
        ('att_subscriptions', '0001_initial'),
        ('aggregateusage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregateddatausage',
            name='att_subscription_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='att_subscriptions.ATTSubscription'),
        ),
        migrations.AddField(
            model_name='aggregateddatausage',
            name='sprint_subscription_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sprint_subscriptions.SprintSubscription'),
        ),
        migrations.AddField(
            model_name='aggregatedvoiceusage',
            name='att_subscription_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='att_subscriptions.ATTSubscription'),
        ),
        migrations.AddField(
            model_name='aggregatedvoiceusage',
            name='sprint_subscription_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sprint_subscriptions.SprintSubscription'),
        ),
        migrations.AlterField(
            model_name='aggregateddatausage',
            name='usage_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='aggregatedvoiceusage',
            name='usage_date',
            field=models.DateField(),
        ),
    ]
