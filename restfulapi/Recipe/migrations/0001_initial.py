# Generated by Django 5.0.3 on 2024-03-11 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipe_name', models.CharField(max_length=20)),
                ('Ingredients', models.TextField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuisines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipe.cuisine')),
            ],
        ),
    ]
