# Generated by Django 5.0.1 on 2024-01-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('thumbimg', models.ImageField(upload_to='media/core')),
                ('about_descp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_heading', models.CharField(max_length=200)),
                ('carousel_img', models.ImageField(null=True, upload_to='media/core')),
                ('carousel_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otpmail', models.EmailField(max_length=254)),
                ('otp_value', models.CharField(max_length=50, null=True, unique=True)),
                ('user_otp', models.CharField(max_length=50, null=True)),
                ('new_password', models.CharField(max_length=250, null=True)),
                ('reenter_new_password', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('profileimg', models.ImageField(null=True, upload_to='media/core')),
            ],
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chooseus_heading', models.CharField(max_length=250)),
                ('chooseus_descp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('address', models.TextField(null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('profile', models.ImageField(null=True, upload_to='media/core')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('customer', 'customer')], default='customer', max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
