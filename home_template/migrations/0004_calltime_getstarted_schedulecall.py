# Generated by Django 3.1 on 2020-08-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_template', '0003_leader_pioneer_successstory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GetStarted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=400)),
                ('how_to_start', models.TextField()),
                ('webinar_image', models.ImageField(upload_to='get_started/images')),
                ('get_started_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=400)),
                ('phone_no', models.CharField(max_length=20)),
                ('call_time', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home_template.calltime')),
            ],
        ),
    ]
