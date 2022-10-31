import os

import django
import datetime
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402


def format_duration(duration):
    return f'{int(duration.total_seconds() // 3600)}h {int((duration.total_seconds() // 60)  % 60)}min'


if __name__ == '__main__':
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    # passcards = Passcard.objects.all()
    # print(passcards[0].owner_name)
    # print(passcards[0].passcode)
    # print(passcards[0].created_at)
    # print(passcards[0].is_active)
    # active_passcards = []
    # for passcard in passcards:
    #     if passcard.is_active:
    #         active_passcards.append(passcard)
    # print('Активных пропусков', len(active_passcards))
    # active_passcards = Passcard.objects.filter(is_active=True)
    # print('Активных пропусков', len(active_passcards))

    # visitors = Visit.objects.all()
    # print(visitors)
    still_there = Visit.objects.filter(leaved_at=None)
    #print(still_there[0].passcard.owner_name)
    # print(still_there[0].entered_at)
    # print(timezone.localtime(still_there[0].entered_at))
    # print(timezone.now())
    # for person in still_there:
    #     print(person.passcard.owner_name)
    #     print('Зашёл в хранилище, время по Москве:')
    #     print(timezone.localtime(person.entered_at))
    #     print('Находится в хранилище:')
    #     print(timezone.now() - timezone.localtime(person.entered_at))
    #     print(person.get_duration().total_seconds())
    #     dur = person.get_duration()
    #     dur_sec = dur.total_seconds()
    #     print(dur_sec)
    #     print(round(dur_sec))
    #     print(format_duration(dur))

    # passcards = Passcard.objects.all()
    # passcard = Passcard.objects.filter(passcode='ceb148a6-fb27-4106-890c-89dc8cedfe83')[0]
    # print(passcard)
    # print(passcards[0].passcode)
    # print(passcards)
    # print(Visit.objects.all())
    # person = Passcard.objects.filter(owner_name='Jennifer Martin')[0]
    # print(person)
    # print(Visit.objects.filter(passcard=person))

    # visits = Visit.objects.all()
    # print(len(visits))
    # c = 0
    # for visit in visits:
    #     print(visit.is_visit_long())
    #     if visit.get_duration() > datetime.timedelta(minutes=50):
    #         print('suspicious')
    #         c +=1
    # print(c)

    #print(Passcard.objects.all())
    for person in Passcard.objects.all():
        #print(person)
        visits = Visit.objects.filter(passcard=person)
        print(len(visits))
        if len(visits) == 0:
            print(person)



