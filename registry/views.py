import datetime
import json
import jwt
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.utils import translation
from django.views.generic import TemplateView
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from registry.models import Activity, Authorization, Contact, Operator, Rpas, Pilot, RpasTest, RpasTestValidity
from registry.serializers import (ContactSerializer, OperatorSerializer, PilotSerializer, 
                                  PrivilagedContactSerializer, PrivilagedPilotSerializer,
                                  PrivilagedOperatorSerializer, RpasSerializer, RpasESNSerializer)
from django.http import JsonResponse
from rest_framework.decorators import api_view
from six.moves.urllib import request as req
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from functools import wraps


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
  
    
    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the access token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            AUTH0_DOMAIN ='testflight.eu.auth0.com'
            API_IDENTIFIER = 'https://basic/testflights'
            jsonurl = req.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
            jwks = json.loads(jsonurl.read())
            cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
            certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
            public_key = certificate.public_key()
            decoded = jwt.decode(token, public_key, audience=API_IDENTIFIER, algorithms=['RS256'])
            
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                print(token_scopes)
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope



class OperatorList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	"""
	List all operators, or create a new operator.
	"""

	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Operator.objects.all()
	serializer_class = OperatorSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)



@api_view(['GET'])
@requires_scope('read:operator')
class OperatorDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Operator instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Operator.objects.all()
	serializer_class = OperatorSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)



@api_view(['GET'])
@requires_scope('read:operator')
@requires_scope('read:privilaged')
class OperatorDetailPrivilaged(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Operator instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Operator.objects.all()
	serializer_class = PrivilagedOperatorSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
		
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)


@api_view(['GET'])
@requires_scope('read:operator')
class OperatorRpas(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,    
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Operator instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Rpas.objects.all()
	serializer_class = RpasSerializer

	def get_Rpas(self, pk):
		try:
			o =  Operator.objects.get(id=pk)
		except Operator.DoesNotExist:
			raise Http404
		else: 
			return Rpas.objects.filter(operator = o)

	def get(self, request, pk,format=None):
		rpas = self.get_Rpas(pk)
		serializer = RpasSerializer(rpas, many=True)

		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	    
	def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)



@api_view(['GET'])
@requires_scope('read:operator')
class RpasESNDetails(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Rpas.objects.all()
    serializer_class = RpasESNSerializer
    lookup_field = 'esn'
	
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@api_view(['GET','POST'])
@requires_scope('read:contact')
class ContactList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	"""
	List all contacts in the database
	"""

	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


@api_view(['GET','POST'])
@requires_scope('read:contact')
class ContactDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Contact instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)

@api_view(['GET','POST'])
@requires_scope('read:contact')
@requires_scope('read:privilaged')
class ContactDetailPrivilaged(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,    
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Contact instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Contact.objects.all()
	serializer_class = PrivilagedContactSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)

@api_view(['GET','POST'])
@requires_scope('read:pilot')
class PilotList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	"""
	List all pilots in the database
	"""

	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


@api_view(['GET','POST'])
@requires_scope('read:pilot')
class PilotDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Pilot instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)


@api_view(['GET','POST'])
@requires_scope('read:pilot')
@requires_scope('read:privilaged')
class PilotDetailPrivilaged(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,    
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Pilot instance.
	"""
	# authentication_classes = (SessionAuthentication,TokenAuthentication)
	# permission_classes = (IsAuthenticated,)

	queryset = Pilot.objects.all()
	serializer_class = PrivilagedPilotSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)



class HomeView(TemplateView):
    template_name ='registry/index.html'

class APIView(TemplateView):
    template_name ='registry/api.html'
