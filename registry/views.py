import datetime
import json

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

from registry.models import Activity, Authorization, Contact, Operator, Aircraft, Pilot, Test, TestValidity
from registry.serializers import (ContactSerializer, OperatorSerializer, PilotSerializer, 
                                  PrivilagedContactSerializer, PrivilagedPilotSerializer,
                                  PrivilagedOperatorSerializer, AircraftSerializer, AircraftESNSerializer)
from django.http import JsonResponse
from rest_framework.decorators import api_view
from six.moves.urllib import request as req
from functools import wraps

class OperatorList(mixins.ListModelMixin,
				  generics.GenericAPIView):
	"""
	List all operators, or create a new operator.
	"""

	queryset = Operator.objects.all()
	serializer_class = OperatorSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)



class OperatorDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Operator instance.
	"""
	

	queryset = Operator.objects.all()
	serializer_class = OperatorSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
	    return self.destroy(request, *args, **kwargs)

class OperatorDetailPrivilaged(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Operator instance.
	"""
	
	queryset = Operator.objects.all()
	serializer_class = PrivilagedOperatorSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)


class OperatorAircraft(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Operator instance.
	"""
	
	queryset = Aircraft.objects.all()
	serializer_class = AircraftSerializer

	def get_Aircraft(self, pk):
		try:
			o =  Operator.objects.get(id=pk)
		except Operator.DoesNotExist:
			raise Http404
		else: 
			return Aircraft.objects.filter(operator = o)

	def get(self, request, pk,format=None):
		aircraft = self.get_Aircraft(pk)
		serializer = AircraftSerializer(aircraft, many=True)

		return Response(serializer.data)

class AircraftESNDetails(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Aircraft.objects.all()
    serializer_class = AircraftESNSerializer
    lookup_field = 'esn'
	
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ContactList(mixins.ListModelMixin,
				  generics.GenericAPIView):
	"""
	List all contacts in the database
	"""

	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


class ContactDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Contact instance.
	"""
	

	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

class ContactDetailPrivilaged(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Contact instance.
	"""
	
	queryset = Contact.objects.all()
	serializer_class = PrivilagedContactSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)

class PilotList(mixins.ListModelMixin,
				  generics.GenericAPIView):
	"""
	List all pilots in the database
	"""
	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)



class PilotDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Pilot instance.
	"""
	
	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)


class PilotDetailPrivilaged(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
	"""
	Retrieve, update or delete a Pilot instance.
	"""
	

	queryset = Pilot.objects.all()
	serializer_class = PrivilagedPilotSerializer

	def get(self, request, *args, **kwargs):
	    return self.retrieve(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name ='registry/index.html'

class APIView(TemplateView):
    template_name ='registry/api.html'
