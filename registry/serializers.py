from rest_framework import serializers
from registry.models import Activity, Authorization, Operator, Contact, Rpas, Pilot


class OperatorSerializer(serializers.ModelSerializer):
    ''' This is the default serializer for Operator '''
    class Meta:
        model = Operator
        fields = ('id', 'company_name', 'website', 'email',
                  'phone_number', 'address', 'postcode', 'city')


class PrivilagedOperatorSerializer(serializers.ModelSerializer):
    ''' This is the privilaged serializer for Operator specially for law enforcement and other privilaged operators '''
    authorized_activities = serializers.SerializerMethodField()
    operational_authorizations = serializers.SerializerMethodField()
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
        fields = ('id', 'company_name', 'website', 'email', 'operator_type', 'phone_number', 'address',
                  'postcode', 'city', 'operational_authorizations', 'authorized_activities', 'created_at', 'updated_at')


class ContactSerializer(serializers.ModelSerializer):
    contact_id = serializers.SerializerMethodField()
	
    def get_contact_id(self, response):
        c = Contact.objects.get(id=response.id)
        contact_id = c.id
        return contact_id

    class Meta:
        model = Contact
        fields = ('id', 'operator', 'contact_id', 'first_name', 'last_name', 'email','phone_number','address','postcode','city','updated_at')

class PilotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pilot
        fields = ('id', 'operator','is_active', 'first_name', 'last_name', 'email','phone_number','updated_at')

class RpasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rpas
        fields = ('id', 'mass', 'manufacturer', 'model','esn','maci_number','status','created_at','updated_at')
        
        

class RpasESNSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rpas
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
