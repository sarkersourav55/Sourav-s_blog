# Generated by Django 3.0.7 on 2020-06-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
