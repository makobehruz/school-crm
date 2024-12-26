from django.shortcuts import render, redirect, get_object_or_404
from .models import Teachers


def teachers_list(request):
    teachers = Teachers.objects.all()
    ctx = {'teachers': teachers}
    return render(request,'teachers/teachers-list.html', ctx)

def teachers_create(request):
    if request.method == 'POST':
        ismi = request.POST.get('ismi')
        familiya = request.POST.get('familiya')
        fan = request.POST.get('fan')
        telefon = request.POST.get('telefon')
        email = request.POST.get('email')
        ish = request.POST.get('ish')
        rasm = request.FILES.get('rasm')
        if ismi and familiya and fan and telefon and email and ish and rasm:
            Teachers.objects.create(
                ismi = ismi,
                familiya = familiya,
                fan = fan,
                telefon = telefon,
                email = email,
                ish = ish,
                rasm = rasm,
            )
            return redirect('teachers:list')
    return render(request,'teachers/teacher-add.html')

def teachers_detail(request, pk):
    teachers = get_object_or_404(Teachers, pk=pk)
    ctx = {'teachers': teachers}
    return render(request,'teachers/teacher-detail.html', ctx)

def teachers_update(request, pk):
    teachers = get_object_or_404(Teachers, pk=pk)
    if request.method == 'POST':
        ismi = request.POST.get('ismi')
        familiya = request.POST.get('familiya')
        fan = request.POST.get('fan')
        telefon = request.POST.get('telefon')
        email = request.POST.get('email')
        ish = request.POST.get('ish')
        rasm = request.FILES.get('rasm')
        if ismi and familiya and fan and telefon and email and ish and rasm:
            teachers.ismi = ismi
            teachers.familiya = familiya
            teachers.fan = fan
            teachers.telefon = telefon
            teachers.email = email
            teachers.ish = ish
            teachers.rasm = rasm
            teachers.save()
            return redirect('teachers:list')
    ctx = {'teachers': teachers}
    return render(request,'teachers/teacher-add.html', ctx)

def teachers_delete(request, pk):
    teachers = get_object_or_404(Teachers, pk=pk)
    if request.method == 'POST':
        teachers.delete()
        return redirect('teachers:list')
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-delete.html', ctx)


