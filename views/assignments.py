from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main import models, forms

HTML_TEMPLATE = 'main/user_page/assignments.html'


@login_required
def get_assignments(request, class_id=None, user_id=None):
    return render(request, HTML_TEMPLATE, {'grouped_assignments': get_grouped_assignments(request, class_id, user_id)})


def request_assignment(request, class_id):
    if request.method == 'POST':
        form_assignment_request = forms.AssignmentRequestForm(request.POST)
        if form_assignment_request.is_valid():
            assignment = form_assignment_request.save()
            models.Class.objects.get(id=class_id).assignments.add(assignment)
    return redirect(request.META['HTTP_REFERER'])


def update_assignment(request, assignment_id):
    if request.method == 'POST':
        assignment = models.Assignment.objects.get(id=assignment_id)
        form_assignment_update = forms.AssignmentUpdateCoachForm(request.POST, instance=assignment) \
            if is_coach(request) else forms.AssignmentUpdateStudentForm(request.POST, instance=assignment)
        if form_assignment_update.is_valid():
            form_assignment_update.save()
    return redirect(request.META['HTTP_REFERER'])


def get_grouped_assignments(request, class_id, user_id):
    assignments = {}
    current_user_id = user_id or request.user.id
    for cls in models.Class.objects.all():
        if not class_id or class_id == cls.id:
            if current_user_id in [usr.id for usr in cls.users.all()]:
                offer_category = cls.offer.category
                offer_type = cls.offer.type
                assignments.setdefault(offer_category, {})
                assignments[offer_category].setdefault(offer_type, {'class_id': cls.id})
                assignments[offer_category][offer_type]['form_assignment_request'] = \
                    forms.AssignmentRequestForm(initial={'offer': cls.offer})
                for assignment in cls.assignments.all().order_by('-id'):
                    assignment.__dict__['form_assignment_update'] = \
                        forms.AssignmentUpdateCoachForm(instance=assignment) \
                        if is_coach(request) else forms.AssignmentUpdateStudentForm(instance=assignment)
                    assignments[offer_category][offer_type].setdefault('assignments', []).append(assignment)
    return dict(sorted(assignments.items()))


def is_coach(request):
    return str(request.user.groups.all()[0]).lower() == 'coaches'
