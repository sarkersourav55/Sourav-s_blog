# Generated by Django 3.0.7 on 2020-06-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(null=True),
        ),
    ]
