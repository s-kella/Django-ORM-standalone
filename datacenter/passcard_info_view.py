from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


def passcard_info_view(request, passcode):
    person = get_object_or_404(Passcard, passcode=passcode)
    #person = Passcard.objects.get_object_or_404(passcode=passcode)
    visits = Visit.objects.filter(passcard=person)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': visit.get_duration,
            'is_strange': visit.is_visit_long
        })

    context = {
        'passcard': person,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
