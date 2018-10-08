from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.models import Teacher
from profiles.forms.teacher_form import TeacherForm

def get_teacher_list(request):
	teachers = Teacher.objects.all()
	return render(request, "teacher/teacher_list.html", {
		'title': 'Teacher List',
		'rows': teachers
	})

def get_teacher_profile(request, id):
	teacher = Teacher.objects.get(id=id)
	return render(request, "teacher/teacher_profile.html", {
		'doc': teacher,
	})

def save_teacher(request, id=None):
	# save or create new teacher
	form = TeacherForm(data=request.POST, instance=Teacher.objects.get(id=id) if id else None)
	if form.is_valid():
		form.save()
		return redirect('teacher-list')
	else:
		return HttpResponse("Error")

def delete_teacher(request, id):
	# delete teacher from the database
	Teacher.objects.filter(id=id).delete()

	return redirect('teacher-list')

# create new teacher
def save_update_teacher(request, id=None):
	if request.method == "POST":
		return save_teacher(request, id=id)
	else:
		teacher = Teacher.objects.get(id=id) if id else None
		form = TeacherForm(instance=teacher)

	return render(request, "teacher/teacher_form.html", {
		"form": form,
		"title": "Update teacher" if id else "Create New",
		"id": id
	})