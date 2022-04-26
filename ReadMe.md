# Django Instagram CloneCoding

## 1. 목적

Django 클론 코딩을 통해 Django의 로직과 CRUD, 파일업로드 ,회원가입, postgresql를 공부하기 위해 클론코딩을 하고 개인 프로젝트인 OCR을 해당 Project에 연동시켰다.

## 2. 개발스택

> - Backend : Django/Python
> - Frontend : JavaScript, Booststarp4
> - DB : Postgresql
> - 서버 : Linux, Nginx
> - 버전관리 : Git

## 3. 개발환경

> - OS : Ubuntu 18.04
> - IDE : VsCode
> - Python : 3.6.9
> - Django : 2.0.13
> - Postgresql : 10.19

## 4. 프로젝트 소개

Django를 공부하면서 Instagram 클론코딩 실습으로 직접 구현을 해보면서 언제 뭐가 쓰이는지 무슨 기능을 구현할땐 어떤 라이브러리가 쓰이는지 Django는 어떤 로직으로 돌아가는지에 대해 공부를 하고 배포까지 하는 ToyProject 입니다.

## 5. 프로젝트 기능

![스크린샷 2022-04-26 오후 5.00.07](/Users/wonbin/Library/Application Support/typora-user-images/스크린샷 2022-04-26 오후 5.00.07.png)

- accounts

  > 사용자 정보 App입니다. 기본적인 로그인, 회원가입 기능을 구현하였습니다.

- coocr

  > 인공지능 프로젝트로 kakao ocr을 통해 이미지 객체인식을 구현한 페이지 입니다.

- media

  > 사진을 업로드하면 저장되는 폴더입니다.

- photo

  > 게시글 작성 App입니다. 로그인한 사용자만 게시글 작성을 할수있고 사진을 업로드 할 수 있습니다. 게시글에 좋아요, 저장 기능을 추가하였고 자신이 좋아요 및 저장한 게시글을 모아서 보여주는 기능도 구현했습니다.

- static

  > Project내의 static파일을 관리하는 폴더입니다.

## 6. 느낀점

 Django 프레임워크를 선택한 이유는 Django는 ORM기능을 지원하고 Django자체적으로 보안이 좋고 python을 기반으로 개발을 하여 언어에 대한 부담감이 없어 Django을 선택했습니다,

해당 프로젝트를 하면서 Django의 MVT에 대한 로직을 공부할수 있었으며 postgresql데이터베이스를 사용하면서 장고의 orm이 얼마나 편하고 좋은것인지에 대해 알수있었습니다. 처음 웹 공부를 할때 사용한 순수 Servlet과 달리 수정을 할때마다 서버를 재가동할 필요없이 수정이 되고 오류가 뜨면 해당 오류가 어디서 난것인지 Console창이든 html쪽에서든 잘 보였습니다.

다만 아쉬웠던 점은 아직 Froent쪽에 대한 지식이 없어 디자인을 꾸미지 못하였고 Django에대해 많이 알지 못해 RestAPI, 잘짜여진 로직에 대해서 부족한점을 많이 느꼇습니다.

더 많은 공부를 통해 다음번엔 제대로 된 프로젝트를 해볼것입니다.

Froent쪽에 대한 문제는 BootStrap을 통해 더욱 잘짜여진 디자인을 사용할 예정입니다.