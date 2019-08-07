from django.shortcuts import render
from rest_framework.views import APIView
from myapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from myapp.models import Employee
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

class EmployeeMixinAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeDetailMixinAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,*kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class EmployeeGenericsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="id"
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__icontains=name)
    #     return qs
class EmployeeGenericsAPIView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


class EmployeeList(APIView):
    def get(self,request,format=None):
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer =EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_Created)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        qs=self.get_object(pk)
        serializer=EmployeeSerializer(qs)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        emp=self.get_object(pk)
        serializer=EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'successfully updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        emp=self.get_object(pk)
        emp.delete()
        return Response({"message":"emp deleted"},status=204)
