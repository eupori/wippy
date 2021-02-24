# NRISE 온라인 코딩 인터뷰 - 이채민

이 프로젝트는 (주)엔라이즈 채용을 하기 위한  백엔드 온라인 코딩 인터뷰용 프로젝트입니다.  
해당 프로젝트는 인터뷰를 위한 프로젝트이기 때문에 작성자 본인과 (주)엔라이즈 인터뷰 관계자만 열람 및 사용할 수 있습니다.  
이 프로젝트는 사용자 관리 API를 구현한 내용이 있습니다.
----
#### API 문서 확인
API 문서는 SWAGGER로 확인할 수 있습니다.
해당 프로젝트를 실행시킨 후 `localhost/swagger` 로 접속하면 API 문서 확인 및 테스트를 진행할 수 있습니다.  
이 뮨서의 하단에도 API에 대한 설명이 추가되어 있습니다.

## 목차 
* [일반 정보] (# general-info) 
* [기술] (# 기술) 
* [설정] (# 설정)
* [예시] (# 예시)

## General-Info
### 프로젝트 기본정보
* 프로젝트 명 : nrise_cmlee
* django app 명 : nrise_app
* 개발자 : 이채민
* 프로젝트 시작일 : 2021.02.22
* 프로젝트 종료일 : 2021.02.24

### 프로젝트 환경
* python - 3.8.8
* django - 3.1.1
* djangorestframework - 3.12.2
* drf-yasg - 1.20.0
* anaconda -4.8.3 (env)
* database - sqlite3

## 기술
* 웹 프레임워크 - django
* 웹 API - django Rest Framework
* API 문서 - SWAGGER
* Serializers - ModelSerializer

## 설정
### 프로젝트 install
1. project 압축 해제  `nrise_cmlee`
2. 터미널(혹은 cmd)에서 설정하고자 하는 가상환경 활성화
3. python 3.8 이상 버전 설치
4. `pip install requirement.txt` 명령어 실행
5. `nrise_cmlee` 디렉토리 안으로 접근
6. `python manage.py migrate` 명령어 실행
7. `python manage.py runserver` 명령어 실행 (포트 충돌 시 변경 필요)
8. 열린 서버로 api 요청 후 결과값 확인

### 프로젝트 구조
* nrise_cmlee : 해당 프로젝트의 루트
* requirement.txt : 프로젝트 실행을 위한 패키지(라이브러리) 목록
* readme.md : 프로젝트 설명을 위한 markdown 설명서
* db.sqlite3 : 해당 프로젝트의 DataBase
* nrise_app : 해당 프로젝트의 장고 앱

### API 구조
해당 API는 사용자를 관리하기 위한 RestFul API입니다.
#### 회원가입 (POST /api/user)
* parameters
  * user_id - String
  * password - String
 * response
   * success : api 호출 성공 여부 (True/False)
   * message : api 호출 결과에 대한 메시지
   * status_code : 상태값 (성공시 200)

#### 로그인 (PUT /api/user)
* parameters
  * user_id - String
  * password - String
 * response
   * success : api 호출 성공 여부 (True/False)
   * message : api 호출 결과에 대한 메시지
   * session_id : 로그인 사용자의 세션 id
   * user_pk : 로그인 사용자의 고유 pk (회원 조회때 사용)
   * status_code : 상태값 (성공시 200)


#### 로그아웃 (DELETE /api/session/{id})
* id :  session의 고유값
 * response
   * success : api 호출 성공 여부 (True/False)
   * message : api 호출 결과에 대한 메시지
   * status_code : 상태값 (성공시 200)

#### 회원조회 (GET /api/user/{id})
* id :  사용자의 고유값 (로그인용 id가 아닌 pk값)
 * response
   * success : api 호출 성공 여부 (True/False)
   * message : api 호출 결과에 대한 메시지
   * data : 조회한 사용자의 고유값, 아이디, 생성일, (탈퇴시)탈퇴 시간
   * status_code : 상태값 (성공시 200)


#### 회원탈퇴 (DELETE /api/user/{id})
* id :  session의 고유값 (사용자의 고유값이 아닌 세션 고유값)
 * response
   * success : api 호출 성공 여부 (True/False)
   * message : api 호출 결과에 대한 메시지
   * status_code : 상태값 (성공시 200)

