from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics

# ----------------------------------------------------------------------
class UserGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer

class UserGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer
       lookup_field = 'id'
  
# ----------------------------------------------------------------------



class JobGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = Job.objects.all()
       serializer_class = JobSerializer

class JobGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = Job.objects.all()
       serializer_class = JobSerializer
       lookup_field = 'id'



# ----------------------------------------------------------------------

class ApplicantGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = Applicants.objects.all()
       serializer_class = ApplicantSerializer

class ApplicantGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = Applicants.objects.all()
       serializer_class = ApplicantSerializer
       lookup_field = 'id'

# ----------------------------------------------------------------------


class SelectedGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = Selected.objects.all()
       serializer_class = ApplicantSerializer

class SelectedGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = Selected.objects.all()
       serializer_class = ApplicantSerializer
       lookup_field = 'id'

# ----------------------------------------------------------------------

class ProfileGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = Profile.objects.all()
       serializer_class = ProfileSerializer

class ProfileGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = Profile.objects.all()
       serializer_class = ProfileSerializer
       lookup_field = 'id'
# ----------------------------------------------------------------------

# class SkillGeneric(generics.ListAPIView,generics.CreateAPIView):
#        queryset = Skill.objects.all()
#        serializer_class = SkillSerializer

# class SkillGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
#        queryset = Skill.objects.all()
#        serializer_class = SkillSerializer
#        lookup_field = 'id'

# ----------------------------------------------------------------------



class SavedJobsGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = SavedJobs.objects.all()
       serializer_class = SavedJobsSerializer

class SavedJobsGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = SavedJobs.objects.all()
       serializer_class = SavedJobsSerializer
       lookup_field = 'id'


class AppliedJobsGeneric(generics.ListAPIView,generics.CreateAPIView):
       queryset = AppliedJobs.objects.all()
       serializer_class = AppliedJobsSerializer

class AppliedJobsGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
       queryset = AppliedJobs.objects.all()
       serializer_class = AppliedJobsSerializer
       lookup_field = 'id'


  







# @api_view(['GET'])
# def home(request):
#     objs = Job.objects.all()
#     print(objs)
#     serializer = JobSeekerSerializer(objs, many=True)
#     print(serializer.data)
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['GET'])
# def user(request):
#     objs = User.objects.all()
#     print(objs)
#     serializer = UserSerializer(objs, many=True)
#     print(serializer.data)
#     return Response({'status': 200, 'payload': serializer.data})

