from django.contrib import admin
from .models import Character
from .models import Island
from .models import Drop
from .models import Box
from .models import CharacterLog


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kind', 'family')
    list_filter = ['kind', 'family']
    search_fields = ['name']


class CharacterLogAdmin(admin.ModelAdmin):
    list_display = ('box', 'character')
    list_filter = ['box']
    search_fields = ['box']
    fieldsets = [
        (None, {'fields': ['box', 'character', 'owned', 'farmed_copies', 'current_level', 'special_cd', 'assigned_sockets']}),
        ('Targets', {'fields': ['level', 'special', 'sockets', 'cotton', 'limit_break', 'limit_abilities']}),
        ('Status', {'fields': ['status', 'max_status']}),
        ('Cotton candies', {'fields': ['cc_hp', 'cc_atk', 'cc_rcv']}),
    ]


class DropAdmin(admin.ModelAdmin):
    list_display = ('island', 'character')
    search_fields = ['island__name']


class IslandAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'start_time', 'end_time')
    search_fields = ['name']
    list_filter = ['kind']


admin.site.register(Character, CharacterAdmin)
admin.site.register(Island, IslandAdmin)
admin.site.register(Drop, DropAdmin)
admin.site.register(Box)
admin.site.register(CharacterLog, CharacterLogAdmin)
