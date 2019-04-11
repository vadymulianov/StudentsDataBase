# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models.students import Student
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


def students_list(request):

    students = Student.objects.all()

    # Try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # Paginate students
    paginator = Paginator(students, 5)
    page = request.GET.get('page')

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If Page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If Page is out of range (e.g. 9999), deliver last page of results
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    # Was form posted
    if request.method == "POST":
        # Was form add button clicked?
        if request.POST.get('add_button') is not None:

            # Errors collection
            errors = {}

            # Data for Student object
            data = {
                'middle_name': request.POST.get('middle_name'),
                'notes': request.POST.get('notes')
            }

            # Validate user input
            first_name =request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not first_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, "%Y-%m-%d")
                except Exception:
                    errors['birthday'] = u'Введіть коректний формат дати (напр. 1988-11-14)'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u'Оберіть коректну групу'
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                # Create Student object
                student = Student(**data)
                # Save it to DataBase
                student.save()
                # Redirect user to students list
                return HttpResponseRedirect(u'%s?status_message=Студента успішно додано!' % reverse('home'))
            else:
                # Render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # Redirect to Home Page on Cancel button
            return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!' % reverse('home'))
    else:
        return render(request, 'students/students_add.html',
                  {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)