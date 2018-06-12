from django.contrib import admin
from .models import Character
from .models import Island
from .models import Drop
from .models import Box
from .models import CharacterLog


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kind', 'family', 'family2')
    list_filter = ['kind', 'family']
    search_fields = ['name']
    fields = ('id', 'name', 'type', 'type2', 'stars', 'kind', 'max_level', 'max_sockets', 'starting_special_cd', 'maxed_special_cd', 'family', 'family2')


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
    list_display = ('island__id', 'island', 'character')
    search_fields = ['island__name']


class IslandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kind', 'start_time', 'end_time', 'start_timeJ', 'end_timeJ')
    search_fields = ['id', 'name']
    list_filter = ['kind']


admin.site.register(Character, CharacterAdmin)
admin.site.register(Island, IslandAdmin)
admin.site.register(Drop, DropAdmin)
admin.site.register(Box)
admin.site.register(CharacterLog, CharacterLogAdmin)
