# Generated by Django 5.0.3 on 2024-04-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('is_published', models.BooleanField(default=False)),
                ('content', models.TextField()),
            ],
        ),
    ]
