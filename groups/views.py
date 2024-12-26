from django.shortcuts import render, redirect, get_object_or_404
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request,'groups/groups-list.html', ctx)

def group_form(request):
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        sinf = request.POST.get('sinf')
        bolalar = request.POST.get('bolalar')
        if nomi and sinf and bolalar:
            Group.objects.create(
                nomi = nomi,
                sinf = sinf,
                bolalar = bolalar,
            )
            return redirect('groups:list')
    return render(request,'groups/group-add.html')

def group_detail(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    ctx = {'groups': groups}
    return render(request,'groups/group-detail.html', ctx)

def group_update(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        sinf = request.POST.get('sinf')
        bolalar = request.POST.get('bolalar')
        if nomi and sinf and bolalar:
            groups.nomi = nomi
            groups.sinf = sinf
            groups.bolalar = bolalar
            groups.save()
            return redirect('groups:list')
    ctx = {'groups': groups}
    return render(request,'groups/group-add.html', ctx)

def group_delete(request, pk):
    groups = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        groups.delete()
        return redirect('groups:list')
    ctx = {'groups': groups}
    return render(request, 'groups/group-delete.html', ctx)




