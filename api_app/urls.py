from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.UserGeneric.as_view(),name="user"),
    path('user/<id>/',views.UserGeneric1.as_view()),


    path('profile/',views.ProfileGeneric.as_view(),name="profile"),
    path('profile/<id>/',views.ProfileGeneric1.as_view()),

    path('job/',views.JobGeneric.as_view(),name="job"),
    path('job/<id>/',views.JobGeneric1.as_view()),
    
    path('applicant/',views.ApplicantGeneric.as_view(),name="job"),
    path('applicant/<id>/',views.ApplicantGeneric1.as_view()),
    
    path('selected/',views.SelectedGeneric.as_view(),name="selected"),
    path('selected/<id>/',views.SelectedGeneric1.as_view()),
    
    
    
    # path('skill/',views.SkillGeneric.as_view(),name="skill"),
    # path('skill/<id>/',views.SkillGeneric1.as_view()),
    
    path('savedjobs/',views.SavedJobsGeneric.as_view(),name="savedjobs"),
    path('savedjobs/<id>/',views.SavedJobsGeneric1.as_view()),
    
    path('appliedjobs/',views.AppliedJobsGeneric.as_view(),name="appliedjobs"),
    path('appliedjobs/<id>/',views.AppliedJobsGeneric1.as_view()),
    
]