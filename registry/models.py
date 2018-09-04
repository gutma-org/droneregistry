from django.db import models
import uuid
# Create your models here.
from datetime import date
from datetime import datetime
from datetime import timezone
from dateutil.relativedelta import relativedelta
from django.utils.translation import ugettext_lazy as _
import string, random 
from django.core.validators import RegexValidator

# Create your models here.
class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=140)

    def __unicode__(self):
       return self.name

    def __str__(self):
        return self.name

class Authorization(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=140)

    end_date = models.DateTimeField(default = datetime.combine( date.today() + relativedelta(months=+24), datetime.min.time()).replace(tzinfo=timezone.utc))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
       return self.title

    def __str__(self):
        return self.title

class Operator(models.Model):
    OPTYPE_CHOICES = ((0, _('Open')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=280)
    website = models.URLField()
    email = models.EmailField()
    operator_type = models.IntegerField(choices=OPTYPE_CHOICES, default = 0)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list)
    address = models.TextField()
    postcode = models.CharField(_("post code"), max_length=10, default="0")
    city = models.CharField(max_length=50)
    operational_authorizations = models.ManyToManyField(Authorization, related_name = 'operational_authorizations')
    authorized_activities = models.ManyToManyField(Activity, related_name = 'authorized_activities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.company_name

    def __str__(self):
        return self.company_name

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null = True, blank = True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField()
    postcode = models.CharField(_("post code"), max_length=10, default="0")
    city = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.email

    def __str__(self):
        return self.email

class Rpas(models.Model):
    STATUS_CHOICES = ((0, _('Inactive')),(1, _('Active')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, models.CASCADE)
    mass = models.IntegerField()
    manufacturer = models.CharField(max_length = 280)
    model = models.CharField(max_length = 280)
    serial_number = models.CharField(max_length = 280)
    maci_number = models.CharField(max_length = 280)
    status = models.IntegerField(choices=STATUS_CHOICES, default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
       return self.model

    def __str__(self):
        return self.model
