# Generated by Django 2.0.3 on 2018-05-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_auto_20180529_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterlog',
            name='current_level',
            field=models.IntegerField(default=1),
        ),
    ]
