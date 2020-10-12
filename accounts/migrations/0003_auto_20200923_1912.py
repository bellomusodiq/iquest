# Generated by Django 3.1.1 on 2020-09-23 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_planemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='planemail',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.plan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planemail',
            name='email',
            field=models.EmailField(max_length=400, unique=True),
        ),
    ]