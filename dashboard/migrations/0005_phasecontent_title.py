# Generated by Django 3.1 on 2020-08-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200813_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='phasecontent',
            name='title',
            field=models.CharField(default='introduction to marketing strategies', max_length=200),
            preserve_default=False,
        ),
    ]
