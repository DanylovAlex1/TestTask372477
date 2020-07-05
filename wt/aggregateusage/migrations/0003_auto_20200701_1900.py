from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateusage', '0002_auto_20200701_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aggregateddatausage',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='aggregatedvoiceusage',
            name='plan',
        ),
    ]
