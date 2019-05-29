from rest_framework import serializers
from registry.models import Activity, Authorization, Operator, Contact, Aircraft, Pilot, Address, Person, Test, TypeCertificate, Manufacturer, TestValidity


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_line_1','address_line_2', 'address_line_3', 'postcode','city', 'country','created_at','updated_at')
   

class GUTMADemoAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address_line_1','address_line_2', 'address_line_3', 'postcode','city', 'country')


class ManufacturerSerializer(serializers.ModelSerializer):
    
    address = GUTMADemoAddressSerializer(read_only=True)
    class Meta:
        model = Manufacturer
        fields = ('id', 'full_name','common_name', 'address', 'role')
   
        


class GUTMADemoAuthorizationSerializer(serializers.ModelSerializer):
    risk_type =  serializers.SerializerMethodField()
    authorization_type =  serializers.SerializerMethodField()
    operation_area_type =  serializers.SerializerMethodField()
    def get_risk_type(self, obj):
        return obj.get_risk_type_display()

    def get_authorization_type(self, obj):
        return obj.get_authorization_type_display()
    def get_operation_area_type(self, obj):
        return obj.get_operation_area_type_display()
    
    class Meta:
        model = Authorization
        fields = ( 'title','risk_type', 'authorization_type', 'operation_area_type', 'end_date')
          

class TypeCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeCertificate
        fields = ('id', 'type_certificate_id','type_certificate_issuing_country', 'type_certificate_holder','type_certificate_holder_country', )

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'first_name','middle_name', 'last_name', 'email','created_at','updated_at')

class GUTMADemoPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('first_name','middle_name', 'last_name', 'email')

class TestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'test_type','taken_at', 'name','created_at','updated_at')

class GutmaDemoTestsSerializer(serializers.ModelSerializer):

    test_type =  serializers.SerializerMethodField()
    taken_at =  serializers.SerializerMethodField()

    def get_test_type(self, obj):
        return obj.get_test_type_display()
    def get_taken_at(self, obj):
        return obj.get_taken_at_display()
    class Meta:
        model = Test
        fields = ('id', 'test_type','taken_at', 'name')

class GutmaDemoTestsValiditySerializer(serializers.ModelSerializer):
    
    tests = GutmaDemoTestsSerializer(read_only=True, many=True)
    class Meta:
        model = TestValidity
        fields = ('id', 'test' ,'name','created_at','updated_at')


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
        fields = ('id', 'company_name','country', 'website', 'email', 'operator_type', 'address', 'operational_authorizations', 'authorized_activities', 'created_at', 'updated_at')


class GUTMADemoOperatorSerializer(serializers.ModelSerializer):
    ''' This is the privilaged serializer for Operator specially for law enforcement and other privilaged operators '''
    authorized_activities = serializers.SerializerMethodField()
    operational_authorizations = serializers.SerializerMethodField()
    contacts = serializers.SerializerMethodField()
    address = GUTMADemoAddressSerializer(read_only=True)
    pilots = serializers.SerializerMethodField()
    aircrafts = serializers.SerializerMethodField()


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
            authorization_serializer = GUTMADemoAuthorizationSerializer(authorization)
            authorizations.append(authorization_serializer.data)
        return authorizations

    def get_contacts(self, response):
        all_contacts = []
        o = Operator.objects.get(id=response.id)
        contacts = Contact.objects.filter(operator = o)
        for contact in contacts:
            contact_serializer = GUTMADemoPersonSerializer(contact.person)
            address_serializer = GUTMADemoAddressSerializer(contact.address)
            contact_data = contact_serializer.data
            address_data = address_serializer.data
            contact_data.update(address_data)
            
            all_contacts.append(contact_data)
        return all_contacts
        
    def get_aircrafts(self, response):
        all_aircrafts = []
        o = Operator.objects.get(id=response.id)
        aircrafts = Aircraft.objects.filter(operator = o)
        for aircraft in aircrafts:
            aircraft_serializer = GUTMADemoAircraftSerializer(aircraft)

            all_aircrafts.append(aircraft_serializer.data)
        return all_aircrafts


    def get_pilots(self, response):
        all_pilots = []
        o = Operator.objects.get(id=response.id)
        pilots = Pilot.objects.filter(operator = o)
        for pilot in pilots:
            contact_serializer = GUTMADemoPersonSerializer(pilot.person)
            address_serializer = GUTMADemoAddressSerializer(pilot.address)
            pilot_data = contact_serializer.data
            address_data = address_serializer.data
            pilot_data.update(address_data)
            pilot_data.update({'id':pilot.id})
            all_pilots.append(pilot_data)

        return all_pilots

    class Meta:
        model = Operator
        fields = ('id', 'company_name','country', 'website', 'email', 'operator_type', 'address', 'operational_authorizations', 'authorized_activities','contacts','phone_number', 'company_number','country','pilots', 'aircrafts','created_at', 'updated_at')


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

class GUTMADemoPilotSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    operator = OperatorSerializer(read_only=True)
    tests = serializers.SerializerMethodField()
    def get_tests(self, response):
        p = Pilot.objects.get(id=response.id)
        tests_validity = TestValidity.objects.filter(pilot=p)
        all_tests = []
        for cur_test_validity in tests_validity:
            test_serializer = GutmaDemoTestsSerializer(cur_test_validity.test)
            all_tests.append({'expiration': cur_test_validity.expiration, 'test_details': test_serializer.data})
        return all_tests

    class Meta:
        model = Pilot
        fields = ('id', 'operator','is_active','tests', 'address', 'person','updated_at','created_at')



class AircraftSerializer(serializers.ModelSerializer):
    type_certificate = TypeCertificateSerializer(read_only= True)
    class Meta:
        model = Aircraft
        fields = ('id', 'mass', 'manufacturer', 'model','esn','maci_number','status','registration_mark', '','type_certificate', 'created_at','master_series', 'series','popular_name','manufacturer','registration_mark','sub_category', 'icao_aircraft_type_designator', 'max_certified_takeoff_weight','updated_at')
        
        
class GUTMADemoAircraftSerializer(serializers.ModelSerializer):
    type_certificate = TypeCertificateSerializer(read_only= True)
    
    category = serializers.SerializerMethodField()    
    sub_category = serializers.SerializerMethodField()
    def get_category(self, obj):
        return obj.get_category_display()

    def get_sub_category(self, obj):
        return obj.get_sub_category_display()

    class Meta:
        model = Aircraft
        fields = ('id', 'mass', 'manufacturer', 'model','esn','maci_number','status','registration_mark', 'category','type_certificate', 'created_at','master_series', 'series','popular_name','manufacturer','registration_mark','sub_category', 'icao_aircraft_type_designator', 'max_certified_takeoff_weight','updated_at')
     
class GUTMADemoAircraftDetailSerializer(serializers.ModelSerializer):
    type_certificate = TypeCertificateSerializer(read_only= True)
    manufacturer = ManufacturerSerializer(read_only=True)
    category = serializers.SerializerMethodField()    
    sub_category = serializers.SerializerMethodField()
    def get_category(self, obj):
        return obj.get_category_display()

    def get_sub_category(self, obj):
        return obj.get_sub_category_display()

    class Meta:
        model = Aircraft
        fields = ('id', 'mass', 'manufacturer', 'model','esn','maci_number','status','registration_mark', 'category','type_certificate', 'created_at','master_series', 'series','popular_name','manufacturer','registration_mark','sub_category', 'icao_aircraft_type_designator', 'max_certified_takeoff_weight','updated_at')
           

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
