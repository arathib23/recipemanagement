# Generated by Django 5.0.3 on 2024-03-11 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('review', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='recipe.recipes')),
            ],
            options={
                'ordering': ['Recipes'],
            },
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
