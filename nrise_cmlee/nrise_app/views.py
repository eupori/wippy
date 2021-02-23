from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,serializers
from django.http import JsonResponse
from nrise_app.models import (
	User,
	Session,
)

import hashlib
import datetime

# Create your views here.

class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = (
            "id",
			"logout_at",
			"created_at",
        )

class UserAPIView(APIView):
	"""
	# api/user
	## Request type - POST (회원가입)
	### data-type : form-data
	### Body
	* user_id : 회원가입을 하고자 하는 사용자의 ID
	* password : 회원가입을 하고자 하는 사용자의 password
	----
	## Request type - PUT (로그인)
	### data-type : form-data
	### Body
	* user_id : 로그인을 하고자 하는 사용자의 ID
	* password : 로그인을 하고자 하는 사용자의 password
	"""

	permission_classes=(permissions.AllowAny,)

	def post(self, request, *args, **kwargs):
		user_id = request.POST.get("user_id")
		password = request.POST.get("password")

		#비밀번호 해싱
		hash_pwd = hashlib.sha256(password.encode()) 

		#사용자 생성
		if not User.objects.filter(user_id=user_id, is_active=True).exists():
			User.objects.create(user_id=user_id, password=hash_pwd.hexdigest())
			return JsonResponse({"success":True, "message":"user create success."}, status=200)
		else:
			return JsonResponse({"success":False, "message":"already exists user."}, status=409)	

	def put(self, request, *args, **kwargs):
		user_id = request.POST.get("user_id")
		password = request.POST.get("password")
		login_status = False

		#비밀번호 해싱
		hash_pwd = hashlib.sha256(password.encode()) 

		#사용자 생성
		user = User.objects.get(user_id=user_id, is_active=True)

		#사용자 비밀번호 확인
		if user.password == hash_pwd.hexdigest():
			login_status = True
			ip = ""

			#ip 주소 받아오기
			x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
			if x_forwarded_for:
				ip = x_forwarded_for.split(',')[0]
			else:
				ip = request.META.get('REMOTE_ADDR')

			#세션 로그 생성
			session = Session.objects.create(
				user=user, 
				ip_address=ip,
				)

		return JsonResponse({"success":True, "message":"user login success.", "session_id":session.id, "user_pk":user.id},status=200)


class UserDetailAPIView(APIView):
	"""
	# api/user/id
	## Request type - GET (사용자 조회)
	### data-type : Slug
	### URL Slug Parameter
	* id : 조회하고자 하는 사용자의 고유 id
	  * 해당 id는 로그인 시 사용하는 id가 아닌 사용자 모델의 고유 pk 값입니다.
	----
	## Request type - DELETE (회원 탈퇴)
	### type : Slug
	### URL Slug Parameter
	* id : 탈퇴하고자 하는 사용자의 고유 세션 id
	  * 해당 id는 사용자 모델의 고유 id가 아닌 세션 모델의 고유 pk 값입니다.
	"""

	permission_classes=(permissions.AllowAny,)

	def get(self, request, id, format=None):

		#사용자
		user = User.objects.get(id=id)
		#세션
		session = Session.objects.filter(user__id=id).order_by("-id")

		user_deleted_at = ""
		if user.is_active == False:
			user_deleted_at = user.lastest_logout

		data = {
			"user_pk":user.id,
			"user_id":user.user_id,
			"created_at":user.created_at,
			"deleted_at":user_deleted_at,
			"session":SessionSerializer(session, many=True).data
		}

		return JsonResponse({"success":True, "data":data, "message":"user get success."}, status=200)

	def delete(self, request, id, format=None):

		#세션
		session = Session.objects.get(id=id)

		#세션 로그아웃 시간 지정
		session.logout_at = datetime.datetime.now()
		user = session.user

		#사용자 로그아웃 시간 지정
		user.lastest_logout = datetime.datetime.now()

		#회원 활성화 여부 설정
		user.is_active = False

		#변경사항 저장
		session.save()
		user.save()

		return JsonResponse({"success":True, "message":"user delete success."},status=200)

class SessionAPIView(APIView):
	"""
	# api/session/id
	## Request type - GET (사용자 조회)
	### data-type : Slug
	### URL Slug Parameter
	* id : 로그아웃을 하고자 하는 사용자의 고유 id
	  * 해당 id는 사용자 모델의 고유 id가 아닌 세션 모델의 고유 pk 값입니다.
	"""
	permission_classes=(permissions.AllowAny,)
	def delete(self, request, id, format=None):

		#세션
		session = Session.objects.get(id=id)

		#세션 로그아웃 시간 지정
		session.logout_at = datetime.datetime.now()
		user = session.user

		#사용자 로그아웃 시간
		user.lastest_logout = datetime.datetime.now()

		#변경사항 저장
		session.save()
		user.save()

		return JsonResponse({"success":True, "message":"user logout success."},status=200)