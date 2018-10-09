from django.http import HttpResponse
from django.shortcuts import render, redirect
from academic.models import Subject
from academic.forms.subject_form import SubjectForm
from schools.views import render_base_form

def get_subject_list(request):
	subjects = Subject.objects.all()
	return render(request, "subject/subject_list.html", {
		'title': 'Subject List',
		'rows': subjects
	})

def save_subject(request, subject=None):
	# save or create new subject
	form = SubjectForm(data=request.POST, instance=Subject.objects.get(subject=subject) if subject else None)

	if form.is_valid():
		form.save()
		return redirect('subject-list')
	else:
		return HttpResponse("Error")

def delete_subject(request, subject):
	# delete subject from the database
	Subject.objects.filter(subject=subject).delete()
	return redirect('subject-list')

# create new subject
def save_update_subject(request, subject=None):
	if request.method == "POST":
		return save_subject(request, subject=subject)
	else:
		subject = Subject.objects.get(subject=subject) if subject else None
		form = SubjectForm(instance=subject)

	return render_base_form(request, form, subject, id_field="subject", new_url="new-subject",
        update_url="update-subject")
