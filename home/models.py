from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Custouser(AbstractUser):
    user_type_dataa = ((1,"hod"),(2,"staff"),(3,"student"))
    user_type = models.CharField(default=1,choices=user_type_dataa,max_length=10)
    
    



# Create your models here.
class admin(models.Model):
     id = models.AutoField(primary_key=True)
     
     admin = models.OneToOneField(Custouser,on_delete=models.CASCADE )
    
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at =  models.DateTimeField(auto_now=True)
     objects = models.Manager()
# Create your models here.
class staff(models.Model):
     id = models.AutoField(primary_key=True)
     
     admin = models.OneToOneField(Custouser,on_delete=models.CASCADE )
    
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     objects = models.Manager()
     
class course(models.Model):
     id = models.AutoField(primary_key=True)
     course = models.CharField(max_length=252)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at =  models.DateTimeField(auto_now=True)
     
     objects = models.Manager()
     
class subject(models.Model):
     id = models.AutoField(primary_key=True)
     subject_name = models.CharField(max_length=252)
     course_name = models.ForeignKey(course,on_delete=models.CASCADE)
     staff_name = models.ForeignKey(staff,on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     objects = models.Manager()

class students(models.Model):
     id = models.AutoField(primary_key=True)
    
     admin = models.OneToOneField(Custouser,on_delete=models.CASCADE )
     
     gender = models.CharField(max_length=250)
     profile = models.FileField()
     address = models.TextField()
     course_id = models.ForeignKey(course,on_delete=models.DO_NOTHING)
     session_strat_year = models.DateTimeField()
     session_end_year = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     objects = models.Manager()

class attendence(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(subject,on_delete=models.DO_NOTHING)
    attendence = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class attendence_report(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students,on_delete=models.DO_NOTHING)
    attendence_id = models.ForeignKey(attendence,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class leave_report_student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students,on_delete=models.DO_NOTHING)
    leave_date = models.CharField(max_length=125)
    leave_messege = models.TextField()
    leave_status= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class leave_report_staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(staff,on_delete=models.DO_NOTHING)
    leave_date = models.CharField(max_length=125)
    leave_messege = models.TextField()
    leave_status= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class feed_back_staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(staff,on_delete=models.CASCADE)
    feed_back =  models.TextField()
    feedback_reply  = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class feed_back_student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students,on_delete=models.CASCADE)
    feed_back =  models.TextField()
    feedback_reply  = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class notification_for_student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students,on_delete=models.CASCADE)
    message=  models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class notification_for_staff(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(staff,on_delete=models.CASCADE)
    message=  models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



@receiver(post_save,sender=Custouser)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        if instance.user_type == 1:
            admin.objects.create(admin=instance)
        if instance.user_type == 2:
            staff.objects.create(admin=instance)
        if instance.user_type == 3:
            students.objects.create(admin=instance)


@receiver(post_save, sender=Custouser)
def save_user_profile(sender,instance, **kwargs):
        if instance.user_type == 1:
            instance.admin.save()
        if instance.user_type == 2:
            instance.staff.save()
        if instance.user_type == 3:
            instance.student.save()

    




    
