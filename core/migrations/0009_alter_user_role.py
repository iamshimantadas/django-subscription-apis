# Generated by Django 5.0 on 2023-12-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_contactus_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('customer', 'customer')], default='customer', max_length=20, null=True),
        ),
    ]
