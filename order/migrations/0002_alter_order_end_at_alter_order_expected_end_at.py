# Generated by Django 4.1 on 2023-01-05 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='expected_end_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 14, 49, 19, 132852, tzinfo=datetime.timezone.utc)),
        ),
    ]
