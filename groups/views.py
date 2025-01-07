from django.shortcuts import render, redirect, get_object_or_404
from teachers.models import Teachers
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request,'groups/groups-list.html', ctx)

def group_form(request):
    teachers = Teachers.objects.all()
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        sinf = request.POST.get('sinf')
        if nomi and sinf:
            sinf_obj = Teachers.objects.get(id=sinf)
            Group.objects.create(
                nomi=nomi,
                sinf=sinf_obj,
            )
            return redirect('groups:list')
    ctx = {'teachers': teachers}
    return render(request, 'groups/group-add.html', ctx)


def group_detail(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    ctx = {'groups': groups}
    return render(request,'groups/group-detail.html', ctx)

def group_update(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    teachers = Teachers.objects.all()
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        sinf = request.POST.get('sinf')
        if nomi and sinf:
            sinf_obj = Teachers.objects.get(id=sinf)
            groups.nomi = nomi
            groups.sinf = sinf_obj
            groups.save()
            return redirect('groups:list')
    ctx = {'groups': groups, 'teachers': teachers}
    return render(request, 'groups/group-add.html', ctx)


def group_delete(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        groups.delete()
        return redirect('groups:list')
    ctx = {'groups': groups}
    return render(request, 'groups/group-delete.html', ctx)




