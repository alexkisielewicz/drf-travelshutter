# Generated by Django 3.2.19 on 2023-06-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='tag', max_length=100),
            preserve_default=False,
        ),
    ]
