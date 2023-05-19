from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
            model = Profile
            fields ='__all__'

# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Skill
#             fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
            model = User
            fields ='__all__'
            # include = ['profile']
            # exclude = ['profile']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
            model = Job
            fields ='__all__' 

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
            model = Applicants
            fields ='__all__' 


class SelectedSerializer(serializers.ModelSerializer):
    class Meta:
            model = Selected
            fields ='__all__' 


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Profile
#             fields ='__all__' 


# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Skill
#             fields ='__all__' 


class SavedJobsSerializer(serializers.ModelSerializer):
    class Meta:
            model = SavedJobs
            fields ='__all__' 


class AppliedJobsSerializer(serializers.ModelSerializer):
    class Meta:
            model = AppliedJobs
            fields ='__all__' 
        