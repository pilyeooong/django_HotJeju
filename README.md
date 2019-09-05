Hot Jeju(핫 제주ㅋ)
===================
---------

#### <i class="icon-pencil"></i> 190719
to 'slugify' at the form -> from django.utils.text import slugify 
파일 업로드를 위해 form 양식에 enctype="multipart/form-data" 추가


로그인폼 커스터마이징 과정에서 소셜로그인 불러올때,

{% load account socialaccount %}
{% providers_media_js %} 
을통해 로드

"{% provider_login_url '' %}" 템플릿태그로 출력