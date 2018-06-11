# Generated by Django 2.0.3 on 2018-05-28 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50)),
                ('stars', models.CharField(choices=[('3', 'Three'), ('4', 'Four'), ('5', 'Five'), ('5+', 'Five +'), ('6', 'Six'), ('6+', 'Six +')], max_length=2)),
                ('kind', models.CharField(choices=[('R', 'Raid'), ('FN', 'Fortnight'), ('RR', 'Rare Recruite'), ('S', 'Story'), ('C', 'Colosseum')], max_length=15)),
                ('max_level', models.IntegerField()),
                ('starting_special_cd', models.IntegerField()),
                ('maxed_special_cd', models.IntegerField()),
                ('max_sockets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special', models.BooleanField()),
                ('sockets', models.BooleanField()),
                ('limit_break', models.BooleanField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Island',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='drop',
            name='island',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Island'),
        ),
    ]
