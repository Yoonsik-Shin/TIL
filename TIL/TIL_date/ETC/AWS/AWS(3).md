# AWS (3)

​    

## 확장성 / 고가용성

확장성 (Scalability)

- 애플리케이션 시스템이 조정을 통해 더 많은 양을 처리할 수 있다는 의미
- 수직 확장성 (Vertical Scalability)
  - 인스턴스의 크기를 확장
  - 하위 인스턴스의 유형을 업그레이드 (t2.micro에서 t2.large로 전환)
  - DB같은 분산되지 않은 시스템에서 사용
  - 하드웨어 제한같은 한계가 존재
- 수평 확장성 = 탄력성 (Horizontal Scalability = elasticity)
  - 애플리케이션에서 인스턴스, 시스템 수를 늘리는 방법
  - 대부분의 어플리케이션에서 사용 

고가용성 (High Availability)

- 애플리케이션 or 시스템이 적어도 둘 이상의 AZ나 데이터 센터에서 가동 중인 것을 의미
- 한 곳이 문제가 생겨도 다른 곳에서 처리할 수 있음



EC2에서의 확장성 / 고가용성

- 수직 확장 : 인스턴스의 크기 늘림 (scale up/down)
- 수평 확장 : 인스턴스의 수 늘림 (scale out/in)
  - Auto Scailing Group
  - Load Balancer
- 고가용성 : 동일 애플리케이션의 동일 인스턴스를 다수의 AZ에 걸쳐 실행
  - Auto Scailing Group
  - Load Balancer

​     

## Load Balancing

- 트래픽을 다운스트림의 여러 서버(EC2 인스턴스)로 전달하는 서버
- 애플리케이션의 단일 액세스 지점(DNS)만을 공개
- 어떤 인스턴스로 트래픽을 보낼 수 없는지 확인하여(health check) 다운스트림 인스턴스의 장애를 원할히 처리 가능
- 웹사이트의 SSL Termination 제공하여 암호화된 HTTPS 트래픽을 가질 수 있음
- 쿠키의 고정도를 강화할 수 있음
- 고가용성을 가짐
- 클라우드 내에서 개인 트래픽과 공공 트래픽을 분리할 수 있음

Elastic Load Balancer

- 관리형 로드 밸런서
- AWS가 관리하며, 어떤 경우에도 작동할 것을 보장
- 업그레이드와 유지 관리 및 고가용성을 책임짐
- 작동 방식을 수정할 수 있게끔 일부 구성 놉(knob) 제공
- 다수의 AWS 서비스들과 통합되어 있음 (EC2, EC2 Auto Scaling Groups, ECS, ACM, CloudWatch, Route53, WAF, Global Accelerator)

Health Check (상태확인)

- ELB가 EC2 인스턴스의 작동이 올바르게 되고 있는지 여부를 확인하기 위해 사용됨
- 제대로 동작하지 않으면 해당 인스턴스로 트래픽을 보낼 수 없음
- 포트와 라우트에서 이루어짐 (프로토콜: HTTP, Port: 4567, Endpoint: /health)
- EC2 인스턴스가 괜찮다면 HTTP 상태코드 200을 반환함
- 그렇지 않다면 인스턴스 상태가 좋지 않다고 기록하고 트래픽을 보내지 않음

4가지 종류의 관리형 로드밸런서

1. Classic Load Balancer (CLB)
   - 구세대, V1, 2009년에 만들어짐
   - HTTP, HTTPS, TCP, SSL, secure TCP 지원
   - 사라짐, 아예 안씀
2. Application Load Balancer (ALB)
   - 신세대, V2, 2016년 출시
   - HTTP/2, WebSocket 지원
   - 리다이렉트를 지원함 (HTTP > HTTPS)
   - 7계층, HTTP 전용
   - Target groups(대상 그룹)으로 묶인 머신간의 다수 HTTP 애플리케이션의 라우팅에 사용
   - 동일 EC2 인스턴스상의 여러 애플리케이션에 부하를 분산 (컨테이너, ECS 사용)
   - target groups에 따른 경로 라우팅 지원 
     - URL 대상 경로에 기반한 라우팅 가능 (/users, /posts)
     - URL 호스트이름에 기반한 라우팅 가능 (yoon.shin.com, sik.shin.com)
     - 퀴리 문자열과 헤더 기반 라우팅 가능 (yoonsik.com?id=123&used=false)
   - 마이크로 서비스나 컨테이너 기반 애플리케이션에 가장 좋은 로드 밸런서 (ECS, Docker)
   - 포트 매핑 기능이 있어 ECS 인스턴스의 동적포트로의 리다이렉션이 가능함
   - 고정 호스트 이름이 부여됨
   - 애플리케이션 서버는 클라이언트의 IP를 직접 보지 못함
     - 클라이언트의 실제 IP는 X-Forwarded-For이라는 헤더에 삽입됨
     - X-Forwarded-Port에는 사용하는 포트, X-Forwarded-Proto에는 사용되는 프로토콜 정보가 들어있음
3. Network Load Balancer (NLB)
   - 신세대, V2, 2017년 출시
   - TCP, TLS, UDP, secure TCP 지원
4. Gateway Load Balancer (GWLB)
   - 2020년 출시
   - 네트워크층 (layer3) IP 프로토콜에서 작동

Target Groups (대상 그룹)이 될 수 있는 것들

- EC2 인스턴스
- ECS
- Lambda Functions
- 사설(private) IP 주소