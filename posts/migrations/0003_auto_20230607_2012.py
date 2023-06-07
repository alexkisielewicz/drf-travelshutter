# Generated by Django 3.2.19 on 2023-06-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_exif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hashtags',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('adventure', 'Adventure'), ('travel', 'Travel'), ('nature', 'Nature'), ('landscape', 'Landscape'), ('aerial', 'Aerial'), ('wildlife', 'Wildlife'), ('street', 'Street'), ('architecture', 'Architecture')], max_length=20),
        ),
    ]