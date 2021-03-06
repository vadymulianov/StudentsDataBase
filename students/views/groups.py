# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def groups_list(request):
    groups = Group.objects.all()

    # Try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # Paginate groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If Page is not an integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # If Page is out of range (e.g. 9999), deliver last page of results
        groups = paginator.page(paginator.num_pages)

    return render(request, 'groups/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)