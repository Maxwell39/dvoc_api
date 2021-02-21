from django.db import models
from datetime import datetime, timedelta

class Voucher(models.Model):
    code = models.CharField(max_length=70, blank=False, default='')
    generate_date = models.DateTimeField(default=datetime.now())
    expired_date = models.DateTimeField(default=datetime.now() + timedelta(days=20))
    used = models.BooleanField(default=False)