from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def format_duration(duration):
    return f'{int(duration.total_seconds() // 3600)}h {int((duration.total_seconds() // 60)  % 60)}min'


def storage_information_view(request):
    still_there = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for person in still_there:
        non_closed_visits.append({
            'who_entered': person.passcard.owner_name,
            'entered_at': timezone.localtime(person.entered_at),
            'duration': format_duration(person.get_duration()),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
