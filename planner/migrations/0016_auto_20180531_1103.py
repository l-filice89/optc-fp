# Generated by Django 2.0.3 on 2018-05-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0015_character_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='kind',
            field=models.CharField(choices=[('R', 'Raid'), ('FN', 'Fortnight'), ('RR', 'Rare Recruit'), ('S', 'Story'), ('C', 'Colosseum'), ('SP', 'Special')], max_length=15),
        ),
        migrations.AlterField(
            model_name='island',
            name='kind',
            field=models.CharField(choices=[('R', 'Raid'), ('FN', 'Fortnight'), ('RR', 'Rare Recruit'), ('S', 'Story'), ('C', 'Colosseum'), ('SP', 'Special')], max_length=15),
        ),
    ]
