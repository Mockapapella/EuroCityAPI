# Generated by Django 3.2.7 on 2021-09-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_country_request_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='request_number',
            field=models.IntegerField(default=1),
        ),
    ]
