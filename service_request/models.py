from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create your models here.
STATUS_CHOICES = (
  ('InProcess','InProcess'),
  ('Verified','Verified'),
  ('Resolving','Resolving'),
  ('Resolved','Resolved')
)

class ServiceRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20,blank=False,null=False)
    brief = models.TextField(blank=False,null=False)
    attachment = models.FileField(upload_to='service_attachments',blank=True,null=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=20,default='Pending')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    date_of_issue_resolved = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Check if the status changed to 'Resolved' and update date_of_issue_resolved
        if self.status == 'Resolved' and not self.date_of_issue_resolved:
            self.date_of_issue_resolved = timezone.now()
        super().save(*args, **kwargs)