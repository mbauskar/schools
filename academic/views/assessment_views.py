from django.http import HttpResponse
from academic.models import Assessment
from schools.views import render_base_form
from django.shortcuts import render, redirect
from profiles.models.user import access_teacher
from academic.forms.assessment_form import AssessmentForm
from django.contrib.auth.decorators import login_required

@login_required
def get_assessment_list(request):
	rows = Assessment.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Assessment List',
        'list_template': "assessment/assessment_list.html",
        'new_url': 'new-assessment',
		'rows': rows
	})

def save_assessment(request, id=None):
	# save or create new assessment
	form = AssessmentForm(data=request.POST, instance=Assessment.objects.get(id=id) if id else None)

	if form.is_valid():
		form.save()
		return redirect('assessment-list')
	else:
		return HttpResponse("Error")

@login_required
@access_teacher()
def delete_assessment(request, id):
	# delete assessment from the database
	Assessment.objects.filter(id=id).delete()
	return redirect('assessment-list')

# create new assessment
@login_required
@access_teacher()
def save_update_assessment(request, id=None):
	if request.method == "POST":
		return save_assessment(request, id=id)
	else:
		assessment = Assessment.objects.get(id=id) if id else None
		form = AssessmentForm(instance=assessment)

	return render_base_form(request, form, id, new_url="new-assessment",
        update_url="update-assessment")
