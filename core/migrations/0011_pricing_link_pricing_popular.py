# Generated by Django 5.0 on 2023-12-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pricing_detail_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='link',
            field=models.CharField(default='/', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='popular',
            field=models.BooleanField(null=True),
        ),
    ]
