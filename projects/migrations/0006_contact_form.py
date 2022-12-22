# Generated by Django 4.1.1 on 2022-12-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
