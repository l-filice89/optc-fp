# Generated by Django 2.0.6 on 2018-06-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0019_auto_20180604_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='island',
            name='kind',
            field=models.CharField(choices=[('R', 'Raid'), ('FN', 'Fortnight'), ('C', 'Colosseum'), ('SP', 'Special'), ('TM', 'Treasure Map')], max_length=15),
        ),
    ]
