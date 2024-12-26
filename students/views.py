from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Students


def home(request):
    return render(request,'index.html')

def student_list(request):
    students = Students.objects.all()
    ctx = {'students': students}
    return render(request,'students/students-list.html', ctx)

def student_form(request):
    if request.method == 'POST':
        ismi = request.POST.get('ismi')
        familiya = request.POST.get('familiya')
        manzil = request.POST.get('manzil')
        telefon = request.POST.get('telefon')
        guruh = request.POST.get('guruh')
        dob = request.POST.get('dob')
        rasm = request.FILES.get('rasm')
        if ismi and familiya and guruh and dob and rasm and manzil and telefon:
            Students.objects.create(
                ismi = ismi,
                familiya = familiya,
                guruh = guruh,
                dob = dob,
                rasm = rasm,
                manzil = manzil,
                telefon = telefon,
            )
            return redirect('students:list')
    return render(request,'students/student-add.html')

def student_detail(request, pk):
    students = get_object_or_404(Students, pk=pk)
    ctx = {'students': students}
    return render(request,'students/student-detail.html', ctx)

def student_update(request, pk):
    students = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        ismi = request.POST.get('ismi')
        familiya = request.POST.get('familiya')
        manzil = request.POST.get('manzil')
        telefon = request.POST.get('telefon')
        guruh = request.POST.get('guruh')
        dob = request.POST.get('dob')
        rasm = request.FILES.get('rasm')
        if ismi and familiya and guruh and dob and rasm and manzil and telefon:
            students.ismi = ismi
            students.familiya = familiya
            students.manzil = manzil
            students.telefon = telefon
            students.guruh = guruh
            students.dob = dob
            if rasm:
                students.rasm = rasm
            students.save()
            return redirect('students:list')
    ctx = {'students': students}
    return render(request,'students/student-add.html', ctx)

def student_delete(request, pk):
    students = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        students.delete()
        return redirect('students:list')
    ctx = {'students': students}
    return render(request, 'students/student-delete.html', ctx)



