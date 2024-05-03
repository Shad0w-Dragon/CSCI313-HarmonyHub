# Generated by Django 5.0.3 on 2024-05-03 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_artist_remove_book_author_remove_book_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('common_genre', models.CharField(max_length=100)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.artist')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
