from django.db import models


class Profile(models.Model):
    email = models.EmailField(null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=150)
    level = models.IntegerField(max_length=1)
    dept_name = models.CharField(max_length=150)


class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    prof_name = models.CharField(max_length=150)
    email = models.EmailField(blank=False, null=False)


class ApprovedCourseList(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=150)
    syllabus = models.CharField(max_length=2500)
    level_0 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_0_list')
    level_1 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_1_list')
    level_2 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_2_list')


class ProposedCourseList(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=150)
    syllabus = models.CharField(max_length=2500)
    level_0 = models.ForeignKey(Profile, null=True, blank=True,related_name='%(class)_level_0_list')
    level_1 = models.ForeignKey(Profile, null=True, blank=True,related_name='%(class)_level_1_list')
    level_2 = models.ForeignKey(Profile, null=True, blank=True,related_name='%(class)_level_2_list')
    level_0_sign = models.IntegerField(max_length=1)
    level_1_sign = models.IntegerField(max_length=1)
    level_2_sign = models.IntegerField(max_length=1)

class ApprovedCourseTeaching(models.Model):
    application_no = models.AutoField(primary_key=True)
    course_code = models.ForeignKey(ApprovedCourseList)
    prof_id = models.ForeignKey(Professor)
    semester = models.IntegerField(max_length=2)
    branch = models.CharField(max_length=3)
    course = models.CharField(max_length=10)
    level_0 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_0_teaching')
    level_1 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_1_teaching')
    level_2 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_2_teaching')


class ProposedCourseTeaching(models.Model):
    application_no = models.AutoField(primary_key=True)
    course_code = models.ForeignKey(ApprovedCourseList)
    prof_id = models.ForeignKey(Professor)
    semester = models.IntegerField(max_length=2)
    branch = models.CharField(max_length=3)
    course = models.CharField(max_length=10)
    level_0 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_0_teaching')
    level_1 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_0_teaching')
    level_2 = models.ForeignKey(Profile, null=True, blank=True, related_name='%(class)_level_0_teaching')
    level_0_sign = models.IntegerField(max_length=1)
    level_1_sign = models.IntegerField(max_length=1)
    level_2_sign = models.IntegerField(max_length=1)