# Generated by Django 4.2.7 on 2023-11-12 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('time', models.IntegerField()),
                ('imdb', models.FloatField()),
                ('votes', models.IntegerField()),
                ('meta_score', models.FloatField(null=True)),
                ('gross', models.FloatField(null=True)),
                ('description', models.TextField()),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movies.certification')),
            ],
            options={
                'ordering': ('name', 'year'),
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MovieStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_stars', to='movies.movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_movies', to='movies.star')),
            ],
            options={
                'unique_together': {('movie', 'star')},
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_movies', to='movies.genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_genres', to='movies.movie')),
            ],
            options={
                'unique_together': {('movie', 'genre')},
            },
        ),
        migrations.CreateModel(
            name='MovieDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_movies', to='movies.director')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_directors', to='movies.movie')),
            ],
            options={
                'unique_together': {('movie', 'director')},
            },
        ),
    ]
