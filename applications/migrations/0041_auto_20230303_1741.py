# Generated by Django 3.2.7 on 2023-03-03 16:41

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0040_auto_20230225_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerapplication',
            name='pronouns',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hackerapplication',
            name='diet',
            field=models.CharField(choices=[('None', 'No requirements'), ('Vegetarian', 'Vegeterian'), ('Vegan', 'Vegan'), ('No pork', 'No pork'), ('Gluten-free', 'Gluten-free'), ('Others', 'Others')], default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='diet',
            field=models.CharField(choices=[('None', 'No requirements'), ('Vegetarian', 'Vegeterian'), ('Vegan', 'Vegan'), ('No pork', 'No pork'), ('Gluten-free', 'Gluten-free'), ('Others', 'Others')], default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='which_hack',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'HackUPC 2016 Fall'), (1, 'HackUPC 2016 Winter'), (2, 'HackUPC 2017 Fall'), (3, 'HackUPC 2017 Winter'), (4, 'HackUPC 2018'), (5, 'HackUPC 2019'), (6, 'HackUPC 2021'), (7, 'HackUPC 2022')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sponsorapplication',
            name='diet',
            field=models.CharField(choices=[('None', 'No requirements'), ('Vegetarian', 'Vegeterian'), ('Vegan', 'Vegan'), ('No pork', 'No pork'), ('Gluten-free', 'Gluten-free'), ('Others', 'Others')], default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='diet',
            field=models.CharField(choices=[('None', 'No requirements'), ('Vegetarian', 'Vegeterian'), ('Vegan', 'Vegan'), ('No pork', 'No pork'), ('Gluten-free', 'Gluten-free'), ('Others', 'Others')], default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='which_hack',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'HackUPC 2016 Fall'), (1, 'HackUPC 2016 Winter'), (2, 'HackUPC 2017 Fall'), (3, 'HackUPC 2017 Winter'), (4, 'HackUPC 2018'), (5, 'HackUPC 2019'), (6, 'HackUPC 2021'), (7, 'HackUPC 2022')], max_length=15, null=True),
        ),
    ]
