# Generated by Django 3.2.2 on 2021-05-15 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('raiting', models.CharField(max_length=5)),
                ('date_release', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=10)),
                ('file_image', models.ImageField(upload_to='media/images')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.genre')),
            ],
        ),
    ]
