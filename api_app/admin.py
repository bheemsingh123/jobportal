from django.contrib import admin
from . models import *
admin.site.register(User)


admin.site.register(Job)
admin.site.register(Applicants)
admin.site.register(Selected)





admin.site.register(Profile)
# admin.site.register(Skill)
admin.site.register(SavedJobs)
admin.site.register(AppliedJobs)
