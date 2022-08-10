from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from crud_class.serializers import StudnetSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
# Create your views here.




#================================ USING BASIC API VIEW IN CLASSED BASED VIEW =======================

# class AddRetrive(APIView):
#     def get(self,request):
#         all_student = Student.objects.all()
#         data=StudnetSerializer(all_student,many=True)
#         return Response(data.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         form_data =StudnetSerializer(data=request.data)
#         if form_data.is_valid():
#             form_data.save()
#             return Response({'message':'added successfully!!'},status=status.HTTP_200_OK)
#         return Response({'error':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


# class UpdateDelete(APIView):
#     def get_student(self,id):
#         try :
#             student = Student.objects.get(id=id)
#             return student
#         except Student.DoesNotExist:
#             raise Http404

#     def put(self,request,id):
#         student = self.get_student(id)
#         form_data = StudnetSerializer(instance=student,data=request.data,partial=True)
#         if form_data.is_valid():
#             form_data.save()
#             return Response({'message':'Successully updated!!'},status=status.HTTP_200_OK)
#         return Response({'error':'oops something went wrong!!'},status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         student = self.get_student(id)
#         student.delete()
#         return Response({'message':'Deleted !!'},status=status.HTTP_200_OK)

        
# ============================= USING GNERIC API VIEWS WITH MODEL MIXIN  ====================================

# class AddRetrive(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudnetSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class UpdateDelete(mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudnetSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,*kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,partial=True,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)









#===================================== USING GENERIC API VIEW ===========================================

class AddRetrive(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudnetSerializer

class UpdateDelete(generics.RetrieveUpdateDestroyAPIView,mixins.UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudnetSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,partial=True,*args,**kwargs)

    