# Generated by Django 4.1.1 on 2023-01-06 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_artist_post_tags_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name']},
        ),
    ]
