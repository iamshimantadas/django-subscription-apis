# Generated by Django 5.0 on 2023-12-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_carousel_carousel_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='carousel_img',
            field=models.ImageField(null=True, upload_to='media/core'),
        ),
    ]
