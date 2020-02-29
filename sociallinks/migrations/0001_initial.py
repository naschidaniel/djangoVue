# Generated by Django 3.0.2 on 2020-02-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialMediaPlatform', models.CharField(max_length=250)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'SocialMediaLink',
                'ordering': ['socialMediaPlatform', 'url'],
                'unique_together': {('socialMediaPlatform', 'url')},
            },
        ),
    ]
