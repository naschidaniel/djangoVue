# Generated by Django 3.0.2 on 2020-02-10 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.BlogCategory')),
            ],
            options={
                'verbose_name_plural': 'BlogCategory',
                'ordering': ['category', 'parent__category'],
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('abstract', models.TextField()),
                ('content', models.TextField()),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('mainImage', models.ImageField(upload_to='')),
                ('subImage1', models.ImageField(blank=True, null=True, upload_to='')),
                ('subImage2', models.ImageField(blank=True, null=True, upload_to='')),
                ('subImage3', models.ImageField(blank=True, null=True, upload_to='')),
                ('subImage4', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogCategory')),
            ],
            options={
                'ordering': ['-datePosted'],
            },
        ),
    ]
