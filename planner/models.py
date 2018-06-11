from django.db import models
from django.contrib.auth.models import User
import datetime

status_values = (
    ('0', 'Nothing maxed'),
    ('1', 'Maxed'),
    ('2', 'Bi-maxed'),
    ('3', 'Tri-maxed'),
    ('4', 'Quad-maxed'),
    ('5', 'Penta-maxed'),
    ('6', 'Rainbow-maxed')
)


class Character(models.Model):
    stars_values = (
        ('1', u'\u2605'),
        ('2', u'\u2605' u'\u2605'),
        ('3', u'\u2605' u'\u2605' u'\u2605'),
        ('4', u'\u2605' u'\u2605' u'\u2605' u'\u2605'),
        ('5', u'\u2605' u'\u2605' u'\u2605' u'\u2605' u'\u2605'),
        ('5+', u'\u2605' u'\u2605' u'\u2605' u'\u2605' u'\u2605+' ),
        ('6', u'\u2605' u'\u2605' u'\u2605' u'\u2605' u'\u2605' u'\u2605'),
        ('6+', u'\u2605' u'\u2605' u'\u2605' u'\u2605' u'\u2605' u'\u2605+')
    )
    type_values = (
        ('STR', 'STR'),
        ('DEX', 'DEX'),
        ('QCK', 'QCK'),
        ('PSY', 'PSY'),
        ('INT', 'INT')
    )
    kind_values = (
        ('R', 'Raid'),
        ('FN', 'Fortnight'),
        ('RR', 'Rare Recruit'),
        ('S', 'Story'),
        ('C', 'Colosseum'),
        ('SP', 'Special'),
        ('TM', 'Treasure Map')
    )
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=70)
    type = models.TextField(choices=type_values)
    stars = models.CharField(max_length=2, choices=stars_values)
    kind = models.CharField(max_length=15, choices=kind_values)
    max_level = models.IntegerField()
    starting_special_cd = models.IntegerField()
    maxed_special_cd = models.IntegerField()
    max_sockets = models.IntegerField()
    family = models.CharField(max_length=70)

    def __str__(self):
        return str(self.id) + " - " + self.name


class Island(models.Model):
    kind_values = (
        ('R', 'Raid'),
        ('FN', 'Fortnight'),
        ('SP', 'Special'),
        ('TM', 'Treasure Map'),
        ('C', 'Colosseum'),
        ('SK', 'Skill'),
        ('SS', 'Success'),
    )
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=15, choices=kind_values)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

    def on_today(self):
        if self.start_time < datetime.datetime.now() < self.end_time:
            return True


class Drop(models.Model):
    island = models.ForeignKey(Island, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    special = models.BooleanField(default=True)
    sockets = models.BooleanField()
    limit_break = models.BooleanField()

    def __str__(self):
        return self.island.name + " - " + self.character.name


class Box(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " - " + self.name


class CharacterLog(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    current_level = models.IntegerField(default=1)
    special_cd = models.IntegerField()
    assigned_sockets = models.IntegerField(default=0)
    level = models.BooleanField()
    special = models.BooleanField()
    sockets = models.BooleanField()
    cotton = models.BooleanField()
    limit_break = models.BooleanField()
    limit_abilities = models.BooleanField()
    status = models.CharField(max_length=13, choices=status_values)
    max_status = models.CharField(max_length=13, choices=status_values)
    farmed_copies = models.IntegerField(default=0)
    owned = models.BooleanField(default=True)
    cc_hp = models.IntegerField(default=0)
    cc_atk = models.IntegerField(default=0)
    cc_rcv = models.IntegerField(default=0)

    def __str__(self):
        return self.box.__str__() + " : " + str(self.character.id) + " - " + self.character.name
