from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import JsonResponse

# Create your views here.

class UserAPIView(APIView):
	permission_classes=(permissions.AllowAny,)
	
	def post(self, request, *args, **kwargs):
		return JsonResponse({"data":"data"},status=200)