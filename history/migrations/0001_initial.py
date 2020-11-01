# Generated by Django 3.1.2 on 2020-11-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Prefer Not to Say')])),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('heart_beat_rate', models.IntegerField()),
                ('eye_blink_rate', models.IntegerField()),
                ('emotion_speech_rate', models.IntegerField()),
            ],
        ),
    ]