from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Subject


def subject_list(request):
    subject = Subject.objects.all()
    ctx = {'subjects': subject}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_form(request):
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        rahbar = request.POST.get('rahbar')
        if nomi and rahbar:
            Subject.objects.create(
                nomi = nomi,
                rahbar = rahbar,
            )
            return redirect('subjects:list')
    return render(request,'subjects/subject-add.html')

def subject_detail(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_update(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        rahbar = request.POST.get('rahbar')
        if nomi and rahbar:
            subjects.nomi = nomi
            subjects.rahbar = rahbar
            subjects.save()
            return redirect('subjects:list')
    ctx = {'subjects': subjects}
    return render(request,'subjects/subject-add.html', ctx)

def subject_delete(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subjects.delete()
        return redirect('subjects:list')
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subject-delete.html', ctx)
