from rest_framework import serializers
from registry.models import Activity, Authorization, Operator, Contact, Rpas


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
        fields = ('id', 'contact_id', 'first_name', 'last_name', 'email','phone_number','address','postcode','city','updated_at')

class RpasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rpas
        fields = ('id', 'mass', 'manufacturer', 'model','serial_number','maci_number','status','created_at','updated_at')



class PrivilagedContactSerializer(serializers.ModelSerializer):
    ''' This is the privilaged serializer for Contact model specially for law enforcement and other privilaged operators '''
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
        fields = ('id', 'company_name', 'website', 'email', 'operator_type', 'phone_number', 'address',
                  'postcode', 'city', 'operational_authorizations', 'authorized_activities', 'created_at', 'updated_at')
