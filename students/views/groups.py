# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    groups = (
        {
            'id': 1,
            'name': u'МтМ-21',
            'leader': u'Ульянов'
        },
        {
            'id': 2,
            'name': u'МтМ-22',
            'leader': u'Ульянов'
        },
        {
            'id': 3,
            'name': u'МтМ-23',
            'leader': u'Ульянов'
        }
    )

    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)