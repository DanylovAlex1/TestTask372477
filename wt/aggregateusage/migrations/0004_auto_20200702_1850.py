from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('aggregateusage', '0003_auto_20200701_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregateddatausage',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='aggregatedvoiceusage',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
