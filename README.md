Hot Jeju(핫 제주ㅋ)
===================
# velog

> velog is a blog platform for developers. It provides compfy markdown editor with syntax highlighter enabled. Currently, the service is only available in Korean.

https://velog.io

The whole process of project development is recorded in my [Youtube Channel](https://www.youtube.com/watch?v=WEC6ATuP9Vo&list=PL9FpF_z-xR_FEhguHXMOvCErayV2Huezy&ab_channel=MinjunKim). Live stream is held at 11:00 PM KST everyday.

## Project Stack

### Client

Following items are core frontend technologies used in this project:

- React
- React Router v4
- Sass
- Flow
- Redux
- Redux-pender
- Immer
- Marked
- Prismjs
- CodeMirror

### Server

Following items are core backend technologies used in this project:

- Node.js
- Koa
- Sequelize
- Sequelize-cockroachdb
- Serverless (with AWS Lambda)
- Flow (on Service API)
- TypeScript (on SSR)

## Project Architecture

![](https://i.imgur.com/wkdqu2r.png)
(Image above is created with [Cloudcraft](https://cloudcraft.co/view/00817b35-3c91-4435-be19-8757825e8c5f?key=5UWE37gAvfR4Yfe5THMV9g))

This service heavily relies on AWS Lambda. Its server side rendering function and every service API are hosted on AWS Lambda.

## Run on your machine

If you want to run velog on your machine, please check [Guidelines document](GUIDELINES.md).

## Contributions

Any kinds of contributions are welecomed. Since the test codes of the project is not completed yet, pull requests might take a while.

#### <i class="icon-pencil"></i> 190719
to 'slugify' at the form -> from django.utils.text import slugify 
파일 업로드를 위해 form 양식에 enctype="multipart/form-data" 추가


로그인폼 커스터마이징 과정에서 소셜로그인 불러올때,

{% load account socialaccount %}
{% providers_media_js %} 
을통해 로드

"{% provider_login_url '' %}" 템플릿태그로 출력

python code styleguide / pep8
