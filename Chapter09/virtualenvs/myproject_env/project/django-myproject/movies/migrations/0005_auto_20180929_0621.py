# Generated by Django 2.1.1 on 2018-09-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20180924_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='commercial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='independent',
            field=models.BooleanField(default=False),
        ),
    ]
