# Generated by Django 3.2.7 on 2023-12-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0043_auto_20240119_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackerapplication',
            name='discover',
            field=models.IntegerField(default=False),
        ),
    ]
