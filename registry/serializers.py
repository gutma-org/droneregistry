from rest_framework import serializers
from registry.models import Activity, Authorization, Operator, Contact, Aircraft, Pilot, Address, Person, Test, TypeCertificate


class AddressSerializer(serializers.ModelSerializer):


    class Meta:
        model = Address
        fields = ('id', 'address_line_1','address_line_2', 'address_line_3', 'postcode','city', 'country','created_at','updated_at')

class TypeCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeCertificate
        fields = ('id', 'type_certificate_id','type_certificate_issuing_country', 'type_certificate_holder','type_certificate_holder_country', )

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'first_name','middle_name', 'last_name', 'email','created_at','updated_at')

class TestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'test_type','taken_at', 'name','created_at','updated_at')

class OperatorSerializer(serializers.ModelSerializer):
    ''' This is the default serializer for Operator '''
    class Meta:
        model = Operator
        fields = ('id', 'company_name', 'website', 'email',
                  'phone_number', )


class PrivilagedOperatorSerializer(serializers.ModelSerializer):
    ''' This is the privilaged serializer for Operator specially for law enforcement and other privilaged operators '''
    authorized_activities = serializers.SerializerMethodField()
    operational_authorizations = serializers.SerializerMethodField()
    address = AddressSerializer(read_only=True)
   
    def get_authorized_activities(self, response):
        activities = []
        o = Operator.objects.get(id=response.id)
        oa = o.authorized_activities.all()
        for activity in oa: 
            activities.append(activity.name)
        return activities

    def get_operational_authorizations(self, response):
        authorizations = []
        o = Operator.objects.get(id=response.id)
        oa = o.operational_authorizations.all()
        for authorization in oa: 
            authorizations.append(authorization.title)
        return authorizations


    class Meta:
        model = Operator
        fields = ('id', 'company_name', 'website', 'email', 'operator_type', 'address', 'operational_authorizations', 'authorized_activities', 'created_at', 'updated_at')


class ContactSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    operator = OperatorSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = ('id', 'operator','person','role_type', 'updated_at')

class PilotSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    operator = OperatorSerializer(read_only=True)
    tests = TestsSerializer(read_only=True)
    class Meta:
        model = Pilot
        fields = ('id', 'operator','is_active','tests', 'person','updated_at')

class AircraftSerializer(serializers.ModelSerializer):
    type_certificate = TypeCertificateSerializer(read_only= True)
    class Meta:
        model = Aircraft
        fields = ('id', 'mass', 'manufacturer', 'model','esn','maci_number','status','registration_mark', 'sub_category','type_certificate', 'created_at','master_series', 'series','popular_name','manufacturer','registration_mark','sub_category', 'icao_aircraft_type_designator', 'max_certified_takeoff_weight','updated_at')
        
        

class AircraftESNSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = ('id', 'mass', 'manufacturer', 'model','esn','maci_number','status','created_at','updated_at')
        lookup_field = 'esn'
        
        
class PrivilagedPilotSerializer(serializers.ModelSerializer):
    ''' This is the privilaged serializer for Pilot specially for law enforcement and other privilaged interested parties '''
    tests = serializers.SerializerMethodField()
    operator_id = serializers.SerializerMethodField()
	
    def get_tests(self, response):
        tests = []
        p = Pilot.objects.get(id=response.id)
        all_tests = p.tests.all()
        for test in all_tests: 
            tests.append(test.name)
        return tests

    class Meta:
        model = Pilot
        fields = ('id',  'operator', 'first_name','is_active', 'last_name', 'email','phone_number','tests', 'updated_at')


class PrivilagedContactSerializer(serializers.ModelSerializer):
    ''' This is the privilaged serializer for Contact model specially for law enforcement and other privilaged interested parties '''

    authorized_activities = serializers.SerializerMethodField()
    operational_authorizations = serializers.SerializerMethodField()

    def get_authorized_activities(self, response):
        activities = []
        c = Contact.objects.get(id =response.id)
        o = c.operator
        oa = o.authorized_activities.all()
        for activity in oa: 
            activities.append(activity.name)
        return activities

    def get_operational_authorizations(self, response):
        authorizations = []
        c = Contact.objects.get(id =response.id)
        o = c.operator
        oa = o.operational_authorizations.all()
        for authorization in oa: 
            authorizations.append(authorization.title)
        return authorizations

    class Meta:
        model = Contact
        fields = ('id', 'company_name', 'operator','website', 'email', 'operator_type', 'phone_number', 'address',
                  'postcode', 'city', 'operational_authorizations', 'authorized_activities', 'created_at', 'updated_at')
