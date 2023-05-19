# from django.db import models
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(default=18)
#     father_name = models.CharField(max_length=100)

# class Category(models.Model):
#     category_name = models.CharField(max_length=100)

# class Book(models.Model):
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     book_title = models.CharField(max_length=100)


#///////////////////   recruiter    /////////////////////////////

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from . manager import UserManager


class User(AbstractUser):

    """docstring"""
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14,default='')
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_admin= models.BooleanField('Is admin', default=False)
    is_jobseeker = models.BooleanField('Is jobseeker', default=False)
    is_recruiter = models.BooleanField('Is recruiter', default=False)


CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

# adamya
EDUCATION = (
    ('Diploma', 'Diploma'),
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
    ('Phd', 'Phd'),
)


class Job(models.Model):
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='abc@gmail.com')     # adamya
    address = models.CharField(max_length=200, null=True, blank=True)   # adamya
    salary = models.CharField(max_length=100, null=True, blank=True)    # adamya
    company = models.CharField(max_length=200)
    experience = models.CharField(max_length=30, default='Fresher')     # adamya
    location = models.CharField(max_length=255)
    description = models.TextField()
    education = models.CharField(max_length=50, choices=EDUCATION, default='Bachelors', null=True)  # adamya
    skills_req = models.CharField(max_length=200)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.title


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.applicant





class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.applicant
    






















#candidate


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    full_name = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    skill = models.CharField(max_length=200,default='None')
    grad_year = models.IntegerField(blank=True)
    looking_for = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    slug = AutoSlugField(populate_from='user', unique=True)
    image = models.ImageField(upload_to="profile_images", default='')       # adamya

    def get_absolute_url(self):
        return "/profile/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


# class Skill(models.Model):
#     skill = models.CharField(max_length=200)
#     user = models.ForeignKey(
#         User, related_name='skills', on_delete=models.CASCADE)


class SavedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.job.title


class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.job.title






