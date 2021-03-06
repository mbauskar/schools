from profiles.models import Parent
from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.models.user import access_teacher
from profiles.forms.parent_form import ParentForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def get_parent_list(request):
	rows = Parent.objects.all()
	return render(request, "layout/base_list.html", {
		'title': 'Parent List',
        'list_template': "parent/parent_list.html",
        'new_url': 'new-parent',
		'rows': rows
	})

@login_required
def get_parent_profile(request, id):
	parent = Parent.objects.get(id=id)
	return render(request, "parent/parent_profile.html", {
		'doc': parent,
	})

@login_required
@access_teacher()
def save_parent(request, id=None):
	# save or create new parent
	form = ParentForm(data=request.POST, instance=Parent.objects.get(id=id) if id else None)
	if form.is_valid():
		form.save()
		return redirect('parent-list')
	else:
		return HttpResponse("Error")

@login_required
@access_teacher()
def delete_parent(request, id):
	# delete parent from the database
	Parent.objects.filter(id=id).delete()
	return redirect('parent-list')

# create new parent
def save_update_parent(request, id=None):
	if request.method == "POST":
		return save_parent(request, id=id)
	else:
		parent = Parent.objects.get(id=id) if id else None
		form = ParentForm(instance=parent)

	return render(request, "parent/parent_form.html", {
		"form": form,
		"title": "Update Parent" if id else "Create New",
		"id": id
	})
