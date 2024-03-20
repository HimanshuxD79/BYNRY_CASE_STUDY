from django.contrib import admin
from  .models  import ServiceRequest
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','user','request_type', 'status', 'created_at', 'date_of_issue_resolved')
admin.site.register(ServiceRequest,ServiceAdmin)