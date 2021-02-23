from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import JsonResponse
from nrise_app.models import (
	User,
	Session,
)

import hashlib

# Create your views here.

class UserAPIView(APIView):
	permission_classes=(permissions.AllowAny,)
	
	def post(self, request, *args, **kwargs):
		user_id = request.POST.get("user_id")
		password = request.POST.get("password")

		#비밀번호 해싱
		hash_pwd = hashlib.sha256(password.encode()) 

		#사용자 생성
		User.objects.create(user_id=user_id, password=hash_pwd.hexdigest())

		return JsonResponse({"data":"data"},status=200)


class UserLoginAPIView(APIView):
	permission_classes=(permissions.AllowAny,)

	def post(self, request, *args, **kwargs):
		user_id = request.POST.get("user_id")
		password = request.POST.get("password")
		login_status = False

		#비밀번호 해싱
		hash_pwd = hashlib.sha256(password.encode()) 

		#사용자 생성
		user = User.objects.get(user_id=user_id)

		#사용자 비밀번호 확인
		if user.password.equals(hash_pwd.hexdigest()):
			login_status = True
			Session.objects.create()

		return JsonResponse({"data":"data"},status=200)