# Generated by Django 3.0.8 on 2020-08-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogpost_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='introduction',
            field=models.TextField(max_length=400),
        ),
    ]
