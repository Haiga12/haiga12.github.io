# Generated by Django 4.2.7 on 2023-11-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('mainImage', models.TextField()),
                ('secondaryImage', models.TextField()),
                ('description', models.TextField()),
                ('maxGuests', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
