from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject


def subject_list(request):
    subject = Subject.objects.all()
    ctx = {'subjects': subject}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_form(request):
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        if nomi:
            Subject.objects.create(
                nomi = nomi,
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
        if nomi:
            subjects.nomi = nomi
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
