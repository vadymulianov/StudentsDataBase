from django.contrib import admin


from .models import students, groups


admin.site.register(students.Student)
admin.site.register(groups.Group)
