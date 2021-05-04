**REST : Representational State Transfer**

- 물리적인 것과 상관없는 디자인적 개념
- HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)를 명시하고 HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD 적용
- REST 규칙
    - Uniform Interface
    - Client - Server
    - Stateless 클라이언트 정보를 서버에 저장하지 않고 각 요청을 개별적으로 인식하여 단순하게 처리
    - Cacheable
    - Layered System : 중간매체 사용 가능
    - Self-Descriptiveness : JSON 형태, 메시지로 해당 요청 파악 가능

**REST API** 

- API : Applicatioin Programming Interface

    → REST + API : REST기반으로 서비스 api를 구현한 것

- 확장성과 재사용성 → 유지보수 및 운영 편리
- HTTP 표준 기반으로 Server-Client 구조 구현

**RESTful** : REST 원리를 따르는 시스템

ex)  REST API를 제공하는 웹서비스

**참고**

[https://velog.io/@dnjscksdn98/REST-REST-API-RESTful에-대하여](https://velog.io/@dnjscksdn98/REST-REST-API-RESTful%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)

[https://jy-tblog.tistory.com/24](https://jy-tblog.tistory.com/24)