# Generated by Django 3.2.19 on 2023-06-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='exif',
            field=models.CharField(max_length=150),
        ),
    ]
