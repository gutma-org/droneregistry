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
    ACTIVITYTYPE_CHOICES = ((0, _('NA')),(1, _('Open')),(2, _('Specific')),(3, _('Specific')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=140)
    activity_type = models.IntegerField(choices=ACTIVITYTYPE_CHOICES, default = 0)

    def __unicode__(self):
       return self.name

    def __str__(self):
        return self.name

class Authorization(models.Model):
    AREATYPE_CHOICES = ((0, _('Unpopulated')),(1, _('Sparsely Populated')),(2, _('Densely Populated')),)
    RISKCLASS_CHOICES = ((0, _('NA')),(1, _('SAIL 1')),(2, _('SAIL 2')),(3, _('SAIL 3')),(4, _('SAIL 4')),(5, _('SAIL 5')),(6, _('SAIL 6')),)
    AUTHTYPE_CHOICES = ((0, _('NA')),(1, _('Light UAS Operator Certificate')),(2, _('Standard Scenario Authorization')),)
    AIRSPACE_CHOICES = ((0, _('NA')),(1, _('Green')),(2, _('Amber')),(3, _('Red')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=140)
    operation_max_height = models.IntegerField(default = 0)
    airspace_type = models.IntegerField(choices = AIRSPACE_CHOICES, default =0)
    permit_to_fly_above_crowd = models.BooleanField(default = 0)
    area_type = models.IntegerField(choices=AREATYPE_CHOICES, default = 0)
    risk_type = models.IntegerField(choices= RISKCLASS_CHOICES, default =0)
    authorization_type = models.IntegerField(choices= AUTHTYPE_CHOICES, default =0)
    end_date = models.DateTimeField(default = datetime.combine( date.today() + relativedelta(months=+24), datetime.min.time()).replace(tzinfo=timezone.utc))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
       return self.title

    def __str__(self):
        return self.title

class Operator(models.Model):
    OPTYPE_CHOICES = ((0, _('NA')),(1, _('LUC')),(2, _('Non-LUC')),)
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
    vat_number = models.CharField(max_length=25, blank=True, null=True)
    insurance_number = models.CharField(max_length=25, blank=True, null=True)
    company_number = models.CharField(max_length=25, blank=True, null=True)

    def __unicode__(self):
       return self.company_name

    def __str__(self):
        return self.company_name

class Contact(models.Model):
    ROLE_CHOICES = ((0, _('Other')),(1, _('Responsible')))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null = True, blank = True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField()
    role_type = models.IntegerField(choices=ROLE_CHOICES, default = 0)
    postcode = models.CharField(_("post code"), max_length=10, default="0")
    city = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_security_number = models.CharField(max_length=25, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __unicode__(self):
       return self.email

    def __str__(self):
        return self.email

class RpasTest(models.Model):
    TESTTYPE_CHOICES = ((0, _('Online Test')),(1, _('In Authorized Test Center')),(2, _('Other')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test_type = models.IntegerField(choices = TESTTYPE_CHOICES, default =0)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
       return self.name

class Pilot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null = True, blank = True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) #
    tests = models.ManyToManyField(RpasTest, through ='RPASTestValidity')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default =0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(blank=True, null=True)



class RpasTestValidity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test = models.ForeignKey(RpasTest, models.CASCADE)
    pilot = models.ForeignKey(Pilot, models.CASCADE)
    taken_at = models.DateTimeField(blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)

class RpasTypeCertificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_certificate_id = models.CharField(max_length = 280)
    type_certificate_issuing_country = models.CharField(max_length = 280)
    type_certificate_holder = models.CharField(max_length = 140)
    type_certificate_holder_country = models.CharField(max_length = 140)

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length = 140)
    common_name = models.CharField(max_length = 140)
    acronym = models.CharField(max_length =10)
    role = models.CharField(max_length = 140)
    country = models.CharField(max_length =140)


  
class Rpas(models.Model):
    AIRCRAFT_CATEGORY = ((0, _('Other')),(1, _('FIXED WING')),(2, _('ROTORCRAFT')),(3, _('LIGHTER-THAN-AIR')),(4, _('HYBRID LIFT')),)
    AIRCRAFT_SUB_CATEGORY = ((0, _('Other')),(1, _('AIRPLANE')),(2, _('NONPOWERED GLIDER')),(3, _('POWERED GLIDER')),(4, _('HELICOPTER')),(5, _('GYROPLANE')),(6, _('BALLOON')),(6, _('AIRSHIP')),(7, _('UAV')),)
    STATUS_CHOICES = ((0, _('Inactive')),(1, _('Active')),)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, models.CASCADE)
    mass = models.IntegerField()
    is_airworthy = models.BooleanField(default = 0)
    manufacturer = models.CharField(max_length = 280)    
    make = models.CharField(max_length = 280)    
    master_series = models.CharField(max_length = 280)    
    series = models.CharField(max_length = 280)
    popular_name = models.CharField(max_length = 280)    
    manufacturer = models.ForeignKey(Organization)
    category = models.IntegerField(choices=AIRCRAFT_CATEGORY, default = 0)
    sub_category = models.IntegerField(choices=AIRCRAFT_SUB_CATEGORY, default = 7)
    icao_aircraft_type_designator = models.CharField(max_length =4)
    max_certified_takeoff_weight = models.DecimalField(decimal_places = 3)
    begin_date = models.DateTimeField()
    type_certificate = models.ForeignKey(RpasTypeCertificate, models.CASCADE)
    model = models.CharField(max_length = 280)
    esn = models.CharField(max_length = 48, default='000000000000000000000000000000000000000000000000')
    maci_number = models.CharField(max_length = 280)
    status = models.IntegerField(choices=STATUS_CHOICES, default = 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
       return self.model

    def __str__(self):
        return self.model
