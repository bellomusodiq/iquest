# Generated by Django 3.1 on 2020-08-08 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_template', '0002_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pioneer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=400)),
                ('schedule_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pioneers/images')),
                ('pioneer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_template.pioneer')),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='pioneers/images')),
                ('description', models.CharField(max_length=400)),
                ('pioneer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_template.pioneer')),
            ],
        ),
    ]
