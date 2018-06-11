# Generated by Django 2.0.3 on 2018-05-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_character_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='max_status',
            field=models.CharField(choices=[('0', ''), ('1', 'Maxed'), ('2', 'Bi-maxed'), ('3', 'Tri-maxed'), ('4', 'Quad-maxed'), ('5', 'Penta-maxed'), ('6', 'Rainbow-maxed')], default=0, max_length=13),
            preserve_default=False,
        ),
    ]
