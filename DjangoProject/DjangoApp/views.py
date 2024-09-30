from django.shortcuts import render
from .models import DjangoVarity,subjects
from django.shortcuts import get_object_or_404
from .forms import DjangoVarityForm
def all_django(request):
    Djangos=DjangoVarity.objects.all()
    return render(request,'DjangoApp/all_django.html',{'Djangos':Djangos})


def details(request, Django_id):
    Django_details=get_object_or_404(DjangoVarity, pk=Django_id)
    return render(request,'DjangoApp/django_detail.html',{'Django_details':Django_details})


def college_loc(request):
    locations=None
    if request.method=='POST':
        form=DjangoVarityForm(request.POST)
        if form.is_valid():
            Django_variety=form.cleaned_data['Dj_Var']
            locations=subjects.objects.filter(sub_variety=Django_variety)
    else:
        form=DjangoVarityForm()
    return render (request,'DjangoApp/College_Locations.html',{'locations':locations, 'form':form})