from django.shortcuts import render
from django.http import HttpResponse
from .models import Character
from .models import CharacterLog
from .models import Box
from .models import Island
from .models import Drop
from django.template import loader
from django.http import HttpResponseRedirect
import datetime
import pytz
from itertools import chain


def viewbox(request, boxID):
    user_check = Box.objects.filter(id=boxID).values('user_id')[0].get('user_id')
    if request.user.is_authenticated:
        if request.user.id == user_check:
            character_list = CharacterLog.objects.filter(box__id=boxID).order_by('character')
            box = Box.objects.get(id=boxID)
            template = loader.get_template('planner/viewbox.html')
            context = {
                'character_list': character_list,
                'box': box,
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("The box you're trying to view is not yours!")
    else:
        return HttpResponseRedirect('/login')


def updateCharacter(request, clID):
    character_details = CharacterLog.objects.get(id=clID)
    context = {
        'character': character_details
    }
    template = loader.get_template('planner/update_character.html')
    if request.method == 'POST':
        if request.POST.getlist('owned'):
            character_details.owned = 1
        else:
            character_details.owned = 0
        if request.POST.get('current_level'):
            character_details.current_level = request.POST.get('current_level')
        if request.POST.get('special_cd'):
            character_details.special_cd = request.POST.get('special_cd')
        if request.POST.get('assigned_sockets'):
            character_details.assigned_sockets = request.POST.get('assigned_sockets')
        if request.POST.get('cc_atk'):
            character_details.cc_atk = request.POST.get('cc_atk')
        if request.POST.get('cc_hp'):
            character_details.cc_hp = request.POST.get('cc_hp')
        if request.POST.get('cc_rcv'):
            character_details.cc_rcv = request.POST.get('cc_rcv')
        if request.POST.getlist('toMax'):
            selected = request.POST.getlist('toMax')
            if "level" in selected:
                character_details.level = 1
            else:
                character_details.level = 0
            if "special" in selected:
                character_details.special = 1
            else:
                character_details.special = 0
            if "sockets" in selected:
                character_details.sockets = 1
            else:
                character_details.sockets = 0
            if "cotton" in selected:
                character_details.cotton = 1
            else:
                character_details.cotton = 0
            if "limit_break" in selected:
                character_details.limit_break = 1
            else:
                character_details.limit_break = 0
            if "limit_abilities" in selected:
                character_details.limit_abilities = 1
            else:
                character_details.limit_abilities = 0
        else:
            character_details.level = 0
            character_details.special = 0
            character_details.sockets = 0
            character_details.cotton = 0
            character_details.limit_break = 0
            character_details.limit_abilities = 0
        if request.POST.get('status'):
            character_details.status = request.POST.get('status')
        if request.POST.get('max_status'):
            character_details.max_status = request.POST.get('max_status')
        if request.POST.get('farmed_copies'):
            character_details.farmed_copies = request.POST.get('farmed_copies')
        character_details.save()
        return HttpResponseRedirect('/planner/viewbox'+str(character_details.box.id))
    return HttpResponse(template.render(context, request))


def newbox(request):
    if request.method == 'POST':
        if request.POST.get('box_name'):
            if request.POST.get('japan'):
                if request.POST.get('japan') == "False":
                    jap = False
                else:
                    jap = True
            box = Box(name=request.POST.get('box_name'), user=request.user, japan=jap)
            box.save()
            return HttpResponseRedirect('/planner/boxlist')
    else:
        return render(request, 'planner/create_box.html')


def index(request):
        return render(request, 'index.html')


def boxList(request):
    template = loader.get_template('planner/box_list.html')
    boxes = Box.objects.filter(user_id=request.user.id).order_by('id')
    context = {
        'boxes': boxes
    }
    return HttpResponse(template.render(context, request))


def deletebox(request):
    template = loader.get_template('planner/delete_box.html')
    boxes = Box.objects.filter(user_id=request.user.id)
    context = {
        'boxes': boxes
    }
    if request.method == 'POST':
        if request.POST.getlist('toDelete'):
            for box in request.POST.getlist('toDelete'):
                b = Box.objects.get(id=box)
                b.delete()
            return HttpResponseRedirect('boxlist')
    return HttpResponse(template.render(context, request))


def addCharacter(request, boxID):
    box = Box.objects.get(id=boxID)
    available_characters = Character.objects.all().order_by('id')
    template = loader.get_template('planner/add_character.html')
    in_box = CharacterLog.objects.filter(box=boxID).values_list('character', flat=True)
    hide = False
    filter = ""
    context = {
        'available_characters': available_characters,
        'box': box,
        'in_box': in_box,
        'hide': hide,
        'filter': filter,
    }
    if request.method == 'POST':
        # Add character to box
        if request.POST.getlist('selected'):
            selected = request.POST.getlist('selected')
            if len(selected) == 1:
                for character in selected:
                    character = Character.objects.get(id=character)
                    cl = CharacterLog(box=Box.objects.get(id=boxID), character=character, special_cd =character.starting_special_cd, level=0, special=0, sockets=0, cotton=0, limit_break=0, limit_abilities=0, cc_atk=0, cc_hp=0, cc_rcv=0, status=0, max_status=0)
                    cl.save()
                return HttpResponseRedirect('../' + str(cl.id))
            else:
                for character in selected:
                    character = Character.objects.get(id=character)
                    cl = CharacterLog(box=Box.objects.get(id=boxID), character=character, special_cd =character.starting_special_cd, level=0, special=0, sockets=0, cotton=0, limit_break=0, limit_abilities=0, cc_atk=0, cc_hp=0, cc_rcv=0, status=0, max_status=0)
                    cl.save()
                return HttpResponseRedirect('../viewbox' + str(box.id))
        # Filter character by name
        if request.POST.get('filter_name'):
            filter = request.POST.get('filter_name')
            available_characters = available_characters.filter(name__icontains=filter)
        # Hide already owned characters
        if request.POST.get('hide_owned'):
            hide = request.POST.get('hide_owned')
            if hide == "1":
                available_characters = available_characters.exclude(id__in=in_box)
        context = {
            'available_characters': available_characters,
            'box': box,
            'in_box': in_box,
            'hide': hide,
            'filter': filter,
        }
        HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))


def removeCharacter(request, boxID):
    box = Box.objects.get(id=boxID)
    available_characters = CharacterLog.objects.filter(box_id=boxID).order_by('character_id')
    template = loader.get_template('planner/remove_character.html')
    context = {
        'available_characters': available_characters,
        'box': box,
    }
    if request.method == 'POST':
        if request.POST.getlist('selected'):
            selected = request.POST.getlist('selected')
            for character in selected:
                cl = CharacterLog.objects.get(id=character)
                cl.delete()
            return HttpResponseRedirect('../viewbox' + str(box.id))
    return HttpResponse(template.render(context, request))


def activeEventsGlobal(request):
    # Load template
    template = loader.get_template('planner/active_events.html')

    # EVENT RELATED QUERIES
    # Get current events
    events = Island.objects.filter(start_time__lte=datetime.datetime.now(), end_time__gte=datetime.datetime.now()).exclude(kind='SS').exclude(kind='SK').order_by('end_time')
    events_id = events.values_list('id', flat=True)
    # Get current drops
    drops = Drop.objects.filter(island__in=events_id).order_by('character')
    # Get character with same family for sockets drop
    families = drops.filter(sockets=True).values_list('character__family', flat=True)
    families2 = drops.filter(sockets=True).exclude(character__family2="None").exclude(character__family2__in=families).values_list('character__family2', flat=True)
    families = list(chain(families, families2))
    sockets_only = Character.objects.filter(family__in=families).order_by('family')

    # SKILL UP AND SUPER SUCCESS QUERIES
    # Get skill up and supersuccess datas
    skill_up = Island.objects.get(kind='SK')
    super_success = Island.objects.get(kind='SS')
    sk_status = 0
    ss_status = 0
    now = datetime.datetime.now(skill_up.start_time.tzinfo)
    # Get skill up state
    if skill_up.start_time > now:
        sk_status = 0
    elif skill_up.start_time <= now <= skill_up.end_time:
        sk_status = 1
    elif skill_up.end_time < now:
        sk_status = 2
    # Get supersuccess state
    if super_success.start_time > now:
        ss_status = 0
    elif super_success.start_time <= now <= super_success.end_time:
        ss_status = 1
    elif super_success.end_time < now:
        ss_status = 2

    # USER BOX INFORMATION QUERIES
    # Get user boxes and select the first one
    boxes = Box.objects.filter(user=request.user.id, japan=False).order_by('id')
    if len(boxes) > 0:
        selected_box = boxes[0]
    else:
        selected_box = ""
    if request.method == 'POST':
        if request.POST.get('selected_box'):
            selection = request.POST.get('selected_box')
            selected_box = Box.objects.get(id=selection)
    # Get characters owned for greyout option
    if len(boxes) >0 or request.POST.get('selected_box'):
        not_owned_characters = CharacterLog.objects.filter(box=selected_box.id, owned=False).values_list('character', flat=True)
        owned_characters = CharacterLog.objects.filter(box=selected_box.id)
        in_box_characters = owned_characters.values_list('character', flat=True)
    else:
        not_owned_characters = []
        owned_characters = []
        in_box_characters = []

    context = {
        'active_events': events,
        'events_id': events_id,
        'drops': drops,
        'not_owned_characters': not_owned_characters,
        'in_box_characters': in_box_characters,
        'sockets_only': sockets_only,
        'skill_up': skill_up,
        'super_success': super_success,
        'sk_status': sk_status,
        'ss_status': ss_status,
        'boxes': boxes,
        'selected_box': selected_box,
        'owned_characters': owned_characters,
    }
    return HttpResponse(template.render(context, request))


def activeEventsJapan(request):
    # Load template
    template = loader.get_template('planner/active_events_japan.html')

    # EVENT RELATED QUERIES
    # Get current events
    events = Island.objects.filter(start_timeJ__lte=datetime.datetime.now(), end_timeJ__gte=datetime.datetime.now()).exclude(kind='SS').exclude(kind='SK').order_by('end_time')
    events_id = events.values_list('id', flat=True)
    # Get current drops
    drops = Drop.objects.filter(island__in=events_id).order_by('character')
    # Get character with same family for sockets drop
    families = drops.filter(sockets=True).values_list('character__family', flat=True)
    families2 = drops.filter(sockets=True).exclude(character__family2="None").exclude(character__family2__in=families).values_list('character__family2', flat=True)
    families = list(chain(families, families2))
    sockets_only = Character.objects.filter(family__in=families).order_by('family')

    # SKILL UP AND SUPER SUCCESS QUERIES
    # Get skill up and supersuccess datas
    skill_up = Island.objects.get(kind='SKJ')
    super_success = Island.objects.get(kind='SSJ')
    sk_status = 0
    ss_status = 0
    now = datetime.datetime.now(skill_up.start_timeJ.tzinfo)
    # Get skill up state
    if skill_up.start_timeJ > now:
        sk_status = 0
    elif skill_up.start_timeJ <= now <= skill_up.end_timeJ:
        sk_status = 1
    elif skill_up.end_timeJ < now:
        sk_status = 2
    # Get supersuccess state
    if super_success.start_timeJ > now:
        ss_status = 0
    elif super_success.start_timeJ <= now <= super_success.end_timeJ:
        ss_status = 1
    elif super_success.end_timeJ < now:
        ss_status = 2

    # USER BOX INFORMATION QUERIES
    # Get user boxes and select the first one
    boxes = Box.objects.filter(user=request.user.id, japan=True).order_by('id')
    if len(boxes) > 0:
        selected_box = boxes[0]
    else:
        selected_box = ""
    if request.method == 'POST':
        if request.POST.get('selected_box'):
            selection = request.POST.get('selected_box')
            selected_box = Box.objects.get(id=selection)
    # Get characters owned for greyout option
    if len(boxes) >0 or request.POST.get('selected_box'):
        not_owned_characters = CharacterLog.objects.filter(box=selected_box.id, owned=False).values_list('character', flat=True)
        owned_characters = CharacterLog.objects.filter(box=selected_box.id)
        in_box_characters = owned_characters.values_list('character', flat=True)
    else:
        not_owned_characters = []
        owned_characters = []
        in_box_characters = []

    context = {
        'active_events': events,
        'events_id': events_id,
        'drops': drops,
        'not_owned_characters': not_owned_characters,
        'in_box_characters': in_box_characters,
        'sockets_only': sockets_only,
        'skill_up': skill_up,
        'super_success': super_success,
        'sk_status': sk_status,
        'ss_status': ss_status,
        'boxes': boxes,
        'selected_box': selected_box,
        'owned_characters': owned_characters,
    }
    return HttpResponse(template.render(context, request))


def settings(request):
    context = {
        'timezones': pytz.common_timezones,
    }
    template = loader.get_template('settings.html')
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return HttpResponseRedirect('/')
    return HttpResponse(template.render(context, request))
