from django.shortcuts import render
from .serializers import zomatoapi_ser,zomatoapi_form
from .models import zomatoapitable

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def zomato_form(r):
    if r.method == "POST":
        form = zomatoapi_form(r.POST)
        if form.is_valid():
            form.save()
    return render(r,'signup/formindex.html',{'form':zomatoapi_form})

class zomatoapi_cls(APIView):
    mytable = zomatoapitable.objects.all()
    myser = zomatoapi_ser(mytable,many=True)
    def get(self,r):
        return Response(zomatoapi_cls.myser.data)

    def post(self,r):
        serobj = zomatoapi_ser(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(zomatoapi_cls.myser.data)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

class updatedelete_api(APIView):
    def put(self,r,pk):
        record = zomatoapitable.objects.get(pk=pk)
        recordobj = zomatoapi_ser(record, data=r.data)
        if recordobj.is_valid():
            recordobj.save()
            return Response(zomatoapi_cls.myser.data)
        return Response(recordobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r, pk):
        record = zomatoapitable.objects.get(pk=pk)
        record.delete()
        return Response(zomatoapi_ser(zomatoapitable.objects.all(),many=True).data)



