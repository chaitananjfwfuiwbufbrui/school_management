from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home.models import Custouser,leave_report_student,staff,course,subject,students,attendence,attendence_report,leave_report_staff,leave_report_staff,feed_back_staff,feed_back_student,notification_for_staff,notification_for_student

# Register your models here.
class  UserModel(UserAdmin):
    pass




admin.site.register(staff)
admin.site.register(course)
admin.site.register(Custouser)

admin.site.register(subject)
admin.site.register(students)
admin.site.register(attendence)
admin.site.register(attendence_report)
admin.site.register(leave_report_staff)
admin.site.register(leave_report_student)
admin.site.register(feed_back_staff)
admin.site.register(feed_back_student)
admin.site.register(notification_for_staff)
admin.site.register(notification_for_student)

