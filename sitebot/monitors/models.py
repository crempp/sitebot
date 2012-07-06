from django.db import models

class Monitor(models.Model):
    name        = models.CharField(max_length=256)
    uri         = models.CharField(max_length=256)
    ip_addr     = models.IPAddressField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
