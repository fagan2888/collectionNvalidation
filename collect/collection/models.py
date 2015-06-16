from django.db import models
class profile(models.Model):
    email=models.EmailField(null=False,blank=False,primary_key=True)
    name=models.CharField(max_length=150)
    level=models.IntegerField(max_length=1)
    dept_name=models.CharField(max_length=150)

class professor(models.Model):
    prof_id=models.AutoField(primary_key=True)
    prof_name=models.CharField(max_length=150)
    email=models.EmailField(blank=False,null=False)

class approved_course_list(models.Model):
    course_code=models.CharField(max_length=10,primary_key=True)
    course_name=models.CharField(max_length=150)
    syllabus=models.CharField(max_length=2500)
    level_0=models.ForeignKey(profile,null=True,blank=True)
    level_1=models.ForeignKey(profile,null=True,blank=True)
    level_2=models.ForeignKey(profile,null=True,blank=True)

class proposed_course_list(models.Model):
    course_code=models.CharField(max_length=10,primary_key=True)
    course_name=models.CharField(max_length=150)
    syllabus=models.CharField(max_length=2500)
    level_0=models.ForeignKey(profile,null=True,blank=True)
    level_1=models.ForeignKey(profile,null=True,blank=True)
    level_2=models.ForeignKey(profile,null=True,blank=True)
    level_0_sign=models.IntegerField(max_length=1)
    level_1_sign=models.IntegerField(max_length=1)
    level_2_sign=models.IntegerField(max_length=1)

class approved_course_teaching(models.Model):
    application_no=models.AutoField(primary_key=True)
    course_code=models.ForeignKey(approved_course_list)
    prof_id=models.ForeignKey(professor)
    semester=models.IntegerField(max_length=2)
    branch=models.CharField(max_length=3)
    course=models.CharField(max_length=10)

class approved_course_teaching(models.Model):
    application_no=models.AutoField(primary_key=True)
    course_code=models.ForeignKey(approved_course_list)
    prof_id=models.ForeignKey(professor)
    semester=models.IntegerField(max_length=2)
    branch=models.CharField(max_length=3)
    course=models.CharField(max_length=10)
    level_0=models.ForeignKey(profile,null=True,blank=True)
    level_1=models.ForeignKey(profile,null=True,blank=True)
    level_2=models.ForeignKey(profile,null=True,blank=True)

class proposed_course_teaching(models.Model):
    application_no=models.AutoField(primary_key=True)
    course_code=models.ForeignKey(approved_course_list)
    prof_id=models.ForeignKey(professor)
    semester=models.IntegerField(max_length=2)
    branch=models.CharField(max_length=3)
    course=models.CharField(max_length=10)
    level_0=models.ForeignKey(profile,null=True,blank=True)
    level_1=models.ForeignKey(profile,null=True,blank=True)
    level_2=models.ForeignKey(profile,null=True,blank=True)
    level_0_sign=models.IntegerField(max_length=1)
    level_1_sign=models.IntegerField(max_length=1)
    level_2_sign=models.IntegerField(max_length=1)