from django.shortcuts import render, HttpResponseRedirect
from .serializer import womenapi
from .forms import womenform
from .models import womenmodel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class womenapi_view(APIView):
    def get(self, r):
        apiobj = womenmodel.objects.all()
        storage = womenapi(apiobj, many=True)
        return Response(storage.data)



# Create your views here.
def womenhome(r):
    return render(r, 'women/women.html')


def women_form(r):
    if r.method == "POST":
        form = womenform(r.POST, r.FILES)
        if form.is_valid():
            form.save()
    return render(r, 'women/womenform.html', {'form':womenform, 'data':womenmodel.objects.all})


def womendata(r):
    return render(r, 'women/womendata.html', {'data':womenmodel.objects.all()})

def women_update(r, id):
    obj = womenmodel.objects.get(id=id)
    if r.method == "POST":
        form = womenform(r.POST, r.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/women/data')
    return render(r, 'women/womenupdate.html', {'obj':obj})

def women_delete(r, id):
    obj = womenmodel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/women/data')

