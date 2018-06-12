# Generated by Django 2.0.6 on 2018-06-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0027_auto_20180608_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='kind',
            field=models.CharField(choices=[('R', 'Raid'), ('FN', 'Fortnight'), ('RR', 'Rare Recruit'), ('S', 'Story'), ('C', 'Colosseum'), ('SP', 'Special'), ('TM', 'Treasure Map'), ('RAY', 'Rayleigh Bazar')], max_length=15),
        ),
    ]
