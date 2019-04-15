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
    ACTIVITYTYPE_CHOICES = ((0, _('NA')),(1, _('Open')),(2, _('Specific')),)
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
    ALTITUDE_SYSTEM = ((0, _('wgs84')),(1, _('amsl')),(2, _('agl')),(3, _('sps')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=140)
    operation_max_height = models.IntegerField(default = 0)
    operation_altitude_system = models.IntegerField(default =0, choices = ALTITUDE_SYSTEM)
    airspace_type = models.IntegerField(choices = AIRSPACE_CHOICES, default =0)
    permit_to_fly_above_crowd = models.BooleanField(default = 0)
    operation_area_type = models.IntegerField(choices=AREATYPE_CHOICES, default = 0)
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
    COUNTRY_CHOICES_ISO3166=(('AF','AFGHANISTAN'),('AX','ÅLAND ISLANDS'),('AL','ALBANIA'),('DZ','ALGERIA'),('AS','AMERICAN SAMOA'),('AD','ANDORRA'),('AO','ANGOLA'),('AI','ANGUILLA'),('AQ','ANTARCTICA'),('AG','ANTIGUA AND BARBUDA'),('AR','ARGENTINA'),('AM','ARMENIA'),('AW','ARUBA'),('AU','AUSTRALIA'),('AT','AUSTRIA'),('AZ','AZERBAIJAN'),('BS','BAHAMAS'),('BH','BAHRAIN'),('BD','BANGLADESH'),('BB','BARBADOS'),('BY','BELARUS'),('BE','BELGIUM'),('BZ','BELIZE'),('BJ','BENIN'),('BM','BERMUDA'),('BT','BHUTAN'),('BO','BOLIVIA, PLURINATIONAL STATE OF'),('BQ','BONAIRE, SINT EUSTATIUS AND SABA'),('BA','BOSNIA AND HERZEGOVINA'),('BW','BOTSWANA'),('BV','BOUVET ISLAND'),('BR','BRAZIL'),('IO','BRITISH INDIAN OCEAN TERRITORY'),('BN','BRUNEI DARUSSALAM'),('BG','BULGARIA'),('BF','BURKINA FASO'),('BI','BURUNDI'),('KH','CAMBODIA'),('CM','CAMEROON'),('CA','CANADA'),('CV','CAPE VERDE'),('KY','CAYMAN ISLANDS'),('CF','CENTRAL AFRICAN REPUBLIC'),('TD','CHAD'),('CL','CHILE'),('CN','CHINA'),('CX','CHRISTMAS ISLAND'),('CC','COCOS (KEELING) ISLANDS'),('CO','COLOMBIA'),('KM','COMOROS'),('CG','CONGO'),('CD','CONGO, THE DEMOCRATIC REPUBLIC OF THE'),('CK','COOK ISLANDS'),('CR','COSTA RICA'),('CI','CÔTE D\'IVOIRE'),('HR','CROATIA'),('CU','CUBA'),('CW','CURAÇAO'),('CY','CYPRUS'),('CZ','CZECH REPUBLIC'),('DK','DENMARK'),('DJ','DJIBOUTI'),('DM','DOMINICA'),('DO','DOMINICAN REPUBLIC'),('EC','ECUADOR'),('EG','EGYPT'),('SV','EL SALVADOR'),('GQ','EQUATORIAL GUINEA'),('ER','ERITREA'),('EE','ESTONIA'),('ET','ETHIOPIA'),('FK','FALKLAND ISLANDS (MALVINAS)'),('FO','FAROE ISLANDS'),('FJ','FIJI'),('FI','FINLAND'),('FR','FRANCE'),('GF','FRENCH GUIANA'),('PF','FRENCH POLYNESIA'),('TF','FRENCH SOUTHERN TERRITORIES'),('GA','GABON'),('GM','GAMBIA'),('GE','GEORGIA'),('DE','GERMANY'),('GH','GHANA'),('GI','GIBRALTAR'),('GR','GREECE'),('GL','GREENLAND'),('GD','GRENADA'),('GP','GUADELOUPE'),('GU','GUAM'),('GT','GUATEMALA'),('GG','GUERNSEY'),('GN','GUINEA'),('GW','GUINEA-BISSAU'),('GY','GUYANA'),('HT','HAITI'),('HM','HEARD ISLAND AND MCDONALD ISLANDS'),('VA','HOLY SEE (VATICAN CITY STATE)'),('HN','HONDURAS'),('HK','HONG KONG'),('HU','HUNGARY'),('IS','ICELAND'),('IN','INDIA'),('ID','INDONESIA'),('IR','IRAN, ISLAMIC REPUBLIC OF'),('IQ','IRAQ'),('IE','IRELAND'),('IM','ISLE OF MAN'),('IL','ISRAEL'),('IT','ITALY'),('JM','JAMAICA'),('JP','JAPAN'),('JE','JERSEY'),('JO','JORDAN'),('KZ','KAZAKHSTAN'),('KE','KENYA'),('KI','KIRIBATI'),('KP','KOREA, DEMOCRATIC PEOPLE\'S REPUBLIC OF'),('KR','KOREA, REPUBLIC OF'),('KW','KUWAIT'),('KG','KYRGYZSTAN'),('LA','LAO PEOPLE\'S DEMOCRATIC REPUBLIC'),('LV','LATVIA'),('LB','LEBANON'),('LS','LESOTHO'),('LR','LIBERIA'),('LY','LIBYAN ARAB JAMAHIRIYA'),('LI','LIECHTENSTEIN'),('LT','LITHUANIA'),('LU','LUXEMBOURG'),('MO','MACAO'),('MK','MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),('MG','MADAGASCAR'),('MW','MALAWI'),('MY','MALAYSIA'),('MV','MALDIVES'),('ML','MALI'),('MT','MALTA'),('MH','MARSHALL ISLANDS'),('MQ','MARTINIQUE'),('MR','MAURITANIA'),('MU','MAURITIUS'),('YT','MAYOTTE'),('MX','MEXICO'),('FM','MICRONESIA, FEDERATED STATES OF'),('MD','MOLDOVA, REPUBLIC OF'),('MC','MONACO'),('MN','MONGOLIA'),('ME','MONTENEGRO'),('MS','MONTSERRAT'),('MA','MOROCCO'),('MZ','MOZAMBIQUE'),('MM','MYANMAR'),('NA','NAMIBIA'),('NR','NAURU'),('NP','NEPAL'),('NL','NETHERLANDS'),('NC','NEW CALEDONIA'),('NZ','NEW ZEALAND'),('NI','NICARAGUA'),('NE','NIGER'),('NG','NIGERIA'),('NU','NIUE'),('NF','NORFOLK ISLAND'),('MP','NORTHERN MARIANA ISLANDS'),('NO','NORWAY'),('OM','OMAN'),('PK','PAKISTAN'),('PW','PALAU'),('PS','PALESTINIAN TERRITORY, OCCUPIED'),('PA','PANAMA'),('PG','PAPUA NEW GUINEA'),('PY','PARAGUAY'),('PE','PERU'),('PH','PHILIPPINES'),('PN','PITCAIRN'),('PL','POLAND'),('PT','PORTUGAL'),('PR','PUERTO RICO'),('QA','QATAR'),('RE','RÉUNION'),('RO','ROMANIA'),('RU','RUSSIAN FEDERATION'),('RW','RWANDA'),('BL','SAINT BARTHÉLEMY'),('SH','SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA'),('KN','SAINT KITTS AND NEVIS'),('LC','SAINT LUCIA'),('MF','SAINT MARTIN (FRENCH PART)'),('PM','SAINT PIERRE AND MIQUELON'),('VC','SAINT VINCENT AND THE GRENADINES'),('WS','SAMOA'),('SM','SAN MARINO'),('ST','SAO TOME AND PRINCIPE'),('SA','SAUDI ARABIA'),('SN','SENEGAL'),('RS','SERBIA'),('SC','SEYCHELLES'),('SL','SIERRA LEONE'),('SG','SINGAPORE'),('SX','SINT MAARTEN (DUTCH PART)'),('SK','SLOVAKIA'),('SI','SLOVENIA'),('SB','SOLOMON ISLANDS'),('SO','SOMALIA'),('ZA','SOUTH AFRICA'),('GS','SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS'),('SS','SOUTH SUDAN'),('ES','SPAIN'),('LK','SRI LANKA'),('SD','SUDAN'),('SR','SURINAME'),('SJ','SVALBARD AND JAN MAYEN'),('SZ','SWAZILAND'),('SE','SWEDEN'),('CH','SWITZERLAND'),('SY','SYRIAN ARAB REPUBLIC'),('TW','TAIWAN, PROVINCE OF CHINA'),('TJ','TAJIKISTAN'),('TZ','TANZANIA, UNITED REPUBLIC OF'),('TH','THAILAND'),('TL','TIMOR-LESTE'),('TG','TOGO'),('TK','TOKELAU'),('TO','TONGA'),('TT','TRINIDAD AND TOBAGO'),('TN','TUNISIA'),('TR','TURKEY'),('TM','TURKMENISTAN'),('TC','TURKS AND CAICOS ISLANDS'),('TV','TUVALU'),('UG','UGANDA'),('UA','UKRAINE'),('AE','UNITED ARAB EMIRATES'),('GB','UNITED KINGDOM'),('US','UNITED STATES'),('UM','UNITED STATES MINOR OUTLYING ISLANDS'),('UY','URUGUAY'),('UZ','UZBEKISTAN'),('VU','VANUATU'),('VE','VENEZUELA, BOLIVARIAN REPUBLIC OF'),('VN','VIET NAM'),('VG','VIRGIN ISLANDS, BRITISH'),('VI','VIRGIN ISLANDS, U.S.'),('WF','WALLIS AND FUTUNA'),('EH','WESTERN SAHARA'),('YE','YEMEN'),('ZM','ZAMBIA'),('ZW','ZIMBABWE'),)    
    OPTYPE_CHOICES = ((0, _('NA')),(1, _('LUC')),(2, _('Non-LUC')),(3, _('AUTH')),(4, _('DEC')),)
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
    country = models.CharField(max_length = 2, choices=COUNTRY_CHOICES_ISO3166, default = 'NA')

    def __unicode__(self):
       return self.company_name

    def __str__(self):
        return self.company_name

class Contact(models.Model):
    COUNTRY_CHOICES_ISO3166=(('AF','AFGHANISTAN'),('AX','ÅLAND ISLANDS'),('AL','ALBANIA'),('DZ','ALGERIA'),('AS','AMERICAN SAMOA'),('AD','ANDORRA'),('AO','ANGOLA'),('AI','ANGUILLA'),('AQ','ANTARCTICA'),('AG','ANTIGUA AND BARBUDA'),('AR','ARGENTINA'),('AM','ARMENIA'),('AW','ARUBA'),('AU','AUSTRALIA'),('AT','AUSTRIA'),('AZ','AZERBAIJAN'),('BS','BAHAMAS'),('BH','BAHRAIN'),('BD','BANGLADESH'),('BB','BARBADOS'),('BY','BELARUS'),('BE','BELGIUM'),('BZ','BELIZE'),('BJ','BENIN'),('BM','BERMUDA'),('BT','BHUTAN'),('BO','BOLIVIA, PLURINATIONAL STATE OF'),('BQ','BONAIRE, SINT EUSTATIUS AND SABA'),('BA','BOSNIA AND HERZEGOVINA'),('BW','BOTSWANA'),('BV','BOUVET ISLAND'),('BR','BRAZIL'),('IO','BRITISH INDIAN OCEAN TERRITORY'),('BN','BRUNEI DARUSSALAM'),('BG','BULGARIA'),('BF','BURKINA FASO'),('BI','BURUNDI'),('KH','CAMBODIA'),('CM','CAMEROON'),('CA','CANADA'),('CV','CAPE VERDE'),('KY','CAYMAN ISLANDS'),('CF','CENTRAL AFRICAN REPUBLIC'),('TD','CHAD'),('CL','CHILE'),('CN','CHINA'),('CX','CHRISTMAS ISLAND'),('CC','COCOS (KEELING) ISLANDS'),('CO','COLOMBIA'),('KM','COMOROS'),('CG','CONGO'),('CD','CONGO, THE DEMOCRATIC REPUBLIC OF THE'),('CK','COOK ISLANDS'),('CR','COSTA RICA'),('CI','CÔTE D\'IVOIRE'),('HR','CROATIA'),('CU','CUBA'),('CW','CURAÇAO'),('CY','CYPRUS'),('CZ','CZECH REPUBLIC'),('DK','DENMARK'),('DJ','DJIBOUTI'),('DM','DOMINICA'),('DO','DOMINICAN REPUBLIC'),('EC','ECUADOR'),('EG','EGYPT'),('SV','EL SALVADOR'),('GQ','EQUATORIAL GUINEA'),('ER','ERITREA'),('EE','ESTONIA'),('ET','ETHIOPIA'),('FK','FALKLAND ISLANDS (MALVINAS)'),('FO','FAROE ISLANDS'),('FJ','FIJI'),('FI','FINLAND'),('FR','FRANCE'),('GF','FRENCH GUIANA'),('PF','FRENCH POLYNESIA'),('TF','FRENCH SOUTHERN TERRITORIES'),('GA','GABON'),('GM','GAMBIA'),('GE','GEORGIA'),('DE','GERMANY'),('GH','GHANA'),('GI','GIBRALTAR'),('GR','GREECE'),('GL','GREENLAND'),('GD','GRENADA'),('GP','GUADELOUPE'),('GU','GUAM'),('GT','GUATEMALA'),('GG','GUERNSEY'),('GN','GUINEA'),('GW','GUINEA-BISSAU'),('GY','GUYANA'),('HT','HAITI'),('HM','HEARD ISLAND AND MCDONALD ISLANDS'),('VA','HOLY SEE (VATICAN CITY STATE)'),('HN','HONDURAS'),('HK','HONG KONG'),('HU','HUNGARY'),('IS','ICELAND'),('IN','INDIA'),('ID','INDONESIA'),('IR','IRAN, ISLAMIC REPUBLIC OF'),('IQ','IRAQ'),('IE','IRELAND'),('IM','ISLE OF MAN'),('IL','ISRAEL'),('IT','ITALY'),('JM','JAMAICA'),('JP','JAPAN'),('JE','JERSEY'),('JO','JORDAN'),('KZ','KAZAKHSTAN'),('KE','KENYA'),('KI','KIRIBATI'),('KP','KOREA, DEMOCRATIC PEOPLE\'S REPUBLIC OF'),('KR','KOREA, REPUBLIC OF'),('KW','KUWAIT'),('KG','KYRGYZSTAN'),('LA','LAO PEOPLE\'S DEMOCRATIC REPUBLIC'),('LV','LATVIA'),('LB','LEBANON'),('LS','LESOTHO'),('LR','LIBERIA'),('LY','LIBYAN ARAB JAMAHIRIYA'),('LI','LIECHTENSTEIN'),('LT','LITHUANIA'),('LU','LUXEMBOURG'),('MO','MACAO'),('MK','MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),('MG','MADAGASCAR'),('MW','MALAWI'),('MY','MALAYSIA'),('MV','MALDIVES'),('ML','MALI'),('MT','MALTA'),('MH','MARSHALL ISLANDS'),('MQ','MARTINIQUE'),('MR','MAURITANIA'),('MU','MAURITIUS'),('YT','MAYOTTE'),('MX','MEXICO'),('FM','MICRONESIA, FEDERATED STATES OF'),('MD','MOLDOVA, REPUBLIC OF'),('MC','MONACO'),('MN','MONGOLIA'),('ME','MONTENEGRO'),('MS','MONTSERRAT'),('MA','MOROCCO'),('MZ','MOZAMBIQUE'),('MM','MYANMAR'),('NA','NAMIBIA'),('NR','NAURU'),('NP','NEPAL'),('NL','NETHERLANDS'),('NC','NEW CALEDONIA'),('NZ','NEW ZEALAND'),('NI','NICARAGUA'),('NE','NIGER'),('NG','NIGERIA'),('NU','NIUE'),('NF','NORFOLK ISLAND'),('MP','NORTHERN MARIANA ISLANDS'),('NO','NORWAY'),('OM','OMAN'),('PK','PAKISTAN'),('PW','PALAU'),('PS','PALESTINIAN TERRITORY, OCCUPIED'),('PA','PANAMA'),('PG','PAPUA NEW GUINEA'),('PY','PARAGUAY'),('PE','PERU'),('PH','PHILIPPINES'),('PN','PITCAIRN'),('PL','POLAND'),('PT','PORTUGAL'),('PR','PUERTO RICO'),('QA','QATAR'),('RE','RÉUNION'),('RO','ROMANIA'),('RU','RUSSIAN FEDERATION'),('RW','RWANDA'),('BL','SAINT BARTHÉLEMY'),('SH','SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA'),('KN','SAINT KITTS AND NEVIS'),('LC','SAINT LUCIA'),('MF','SAINT MARTIN (FRENCH PART)'),('PM','SAINT PIERRE AND MIQUELON'),('VC','SAINT VINCENT AND THE GRENADINES'),('WS','SAMOA'),('SM','SAN MARINO'),('ST','SAO TOME AND PRINCIPE'),('SA','SAUDI ARABIA'),('SN','SENEGAL'),('RS','SERBIA'),('SC','SEYCHELLES'),('SL','SIERRA LEONE'),('SG','SINGAPORE'),('SX','SINT MAARTEN (DUTCH PART)'),('SK','SLOVAKIA'),('SI','SLOVENIA'),('SB','SOLOMON ISLANDS'),('SO','SOMALIA'),('ZA','SOUTH AFRICA'),('GS','SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS'),('SS','SOUTH SUDAN'),('ES','SPAIN'),('LK','SRI LANKA'),('SD','SUDAN'),('SR','SURINAME'),('SJ','SVALBARD AND JAN MAYEN'),('SZ','SWAZILAND'),('SE','SWEDEN'),('CH','SWITZERLAND'),('SY','SYRIAN ARAB REPUBLIC'),('TW','TAIWAN, PROVINCE OF CHINA'),('TJ','TAJIKISTAN'),('TZ','TANZANIA, UNITED REPUBLIC OF'),('TH','THAILAND'),('TL','TIMOR-LESTE'),('TG','TOGO'),('TK','TOKELAU'),('TO','TONGA'),('TT','TRINIDAD AND TOBAGO'),('TN','TUNISIA'),('TR','TURKEY'),('TM','TURKMENISTAN'),('TC','TURKS AND CAICOS ISLANDS'),('TV','TUVALU'),('UG','UGANDA'),('UA','UKRAINE'),('AE','UNITED ARAB EMIRATES'),('GB','UNITED KINGDOM'),('US','UNITED STATES'),('UM','UNITED STATES MINOR OUTLYING ISLANDS'),('UY','URUGUAY'),('UZ','UZBEKISTAN'),('VU','VANUATU'),('VE','VENEZUELA, BOLIVARIAN REPUBLIC OF'),('VN','VIET NAM'),('VG','VIRGIN ISLANDS, BRITISH'),('VI','VIRGIN ISLANDS, U.S.'),('WF','WALLIS AND FUTUNA'),('EH','WESTERN SAHARA'),('YE','YEMEN'),('ZM','ZAMBIA'),('ZW','ZIMBABWE'),)  
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
    country = models.CharField(max_length = 2, choices=COUNTRY_CHOICES_ISO3166, default = 'NA')
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

class Test(models.Model):
    TESTTYPE_CHOICES = ((0, _('Remote pilot online theoretical competency')),(1, _('Certificate of remote pilot competency')),(2, _('Other')),)
    TAKEN_AT_CHOICES = ((0, _('Online Test')),(1, _('In Authorized Test Center')),(2, _('Other')),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test_type = models.IntegerField(choices = TESTTYPE_CHOICES, default =0)
    taken_at = models.IntegerField(choices = TAKEN_AT_CHOICES, default =0)
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
    tests = models.ManyToManyField(Test, through ='TestValidity')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default =0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(blank=True, null=True)


class TestValidity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test = models.ForeignKey(Test, models.CASCADE)
    pilot = models.ForeignKey(Pilot, models.CASCADE)
    taken_at = models.DateTimeField(blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)

class TypeCertificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_certificate_id = models.CharField(max_length = 280)
    type_certificate_issuing_country = models.CharField(max_length = 280)
    type_certificate_holder = models.CharField(max_length = 140)
    type_certificate_holder_country = models.CharField(max_length = 140)

class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    full_name = models.CharField(max_length = 140, default = 'NA')
    common_name = models.CharField(max_length = 140, default = 'NA')
    acronym = models.CharField(max_length =10, default = 'NA')
    role = models.CharField(max_length = 140, default = 'NA')
    country = models.CharField(max_length =3, default = 'NA')

  
class Aircraft(models.Model):
    AIRCRAFT_CATEGORY = ((0, _('Other')),(1, _('FIXED WING')),(2, _('ROTORCRAFT')),(3, _('LIGHTER-THAN-AIR')),(4, _('HYBRID LIFT')),)
    AIRCRAFT_SUB_CATEGORY = ((0, _('Other')),(1, _('AIRPLANE')),(2, _('NONPOWERED GLIDER')),(3, _('POWERED GLIDER')),(4, _('HELICOPTER')),(5, _('GYROPLANE')),(6, _('BALLOON')),(6, _('AIRSHIP')),(7, _('UAV')),)
    STATUS_CHOICES = ((0, _('Inactive')),(1, _('Active')),)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operator = models.ForeignKey(Operator, models.CASCADE)
    mass = models.IntegerField()
    is_airworthy = models.BooleanField(default = 0)    
    make = models.CharField(max_length = 280, blank= True, null=True)    
    master_series = models.CharField(max_length = 280, blank= True, null=True)    
    series = models.CharField(max_length = 280, blank= True, null=True)
    popular_name = models.CharField(max_length = 280, blank= True, null=True)    
    manufacturer = models.ForeignKey(Manufacturer, models.CASCADE)
    category = models.IntegerField(choices=AIRCRAFT_CATEGORY, default = 0)
    registration_mark = models.CharField(max_length= 10, blank= True, null=True)
    sub_category = models.IntegerField(choices=AIRCRAFT_SUB_CATEGORY, default = 7)
    icao_aircraft_type_designator = models.CharField(max_length =4, default = '0000')
    max_certified_takeoff_weight = models.DecimalField(decimal_places = 3, max_digits=10, default = 0.00)
    begin_date = models.DateTimeField(blank= True, null= True)
    type_certificate = models.ForeignKey(TypeCertificate, models.CASCADE, blank= True, null= True)
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
