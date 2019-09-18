#Hot Jeju

> 핫제주는 제주도민 입장에서 본 제주관광명소 및 맛집,카페 등을 정리 및 공유하고자 시작한 프로젝트

## Project Stack

### Client

 Following items are core frontend technologies used in this project:

- HTML
- CSS
- BootStrap

### Server

 Following items are core backend technologies used in this project:

- Django

## Run on your machine

requirements.txt를 참고하여 모듈 install 후 , ./manage.py runserver (Django)

## Contributions

모든 피드백은 환영하고 감사합니다 . (190918 기준 프로젝트 진행중이며 , 떠오르는 아이디어나 컨텐츠가 있으면 반영하는중 입니다.) 

## Issues

- to 'slugify' at the form -> from django.utils.text import slugify 

- 로그인폼 커스터마이징 과정에서 소셜로그인 불러올때,

- {% load account socialaccount %}
  {% providers_media_js %} 을통해 로드
 "{% provider_login_url '' %}" 템플릿태그로 출력

- python code styleguide / pep8
