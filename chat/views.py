from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from courses.models import Course


@login_required
def course_chat_room(request, course_id):
    try:
        # retrieve course  with given id joined by the current user

        # solution 1
        course = request.user.courses_joined.get(id=course_id)

        # solution 3
        # course = Course.objects.filter(id=course_id).get()
        # course=course.students.get(id=request.user.id)

        # solution 4
        # course = Course.objects.filter(id=course_id).filter(students__in=[request.user]).get()

        # solution 2
        #course = Course.objects.filter(id=course_id, students__in=[request.user]).get()
    except:
        # user is not a student of the course or course does not exist

        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
