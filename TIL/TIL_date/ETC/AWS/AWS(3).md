# AWS (3)

## 0️⃣ 확장성 / 고가용성

>  확장성 (Scalability)

- 애플리케이션 시스템이 조정을 통해 더 많은 양을 처리할 수 있다는 의미
- 수직 확장성 (Vertical Scalability)
  - 인스턴스의 크기를 확장
  - 하위 인스턴스의 유형을 업그레이드 (t2.micro에서 t2.large로 전환)
  - DB같은 분산되지 않은 시스템에서 사용
  - 하드웨어 제한같은 한계가 존재
- 수평 확장성 = 탄력성 (Horizontal Scalability = elasticity)
  - 애플리케이션에서 인스턴스, 시스템 수를 늘리는 방법
  - 대부분의 어플리케이션에서 사용 

> 고가용성 (High Availability)

- 애플리케이션 or 시스템이 적어도 둘 이상의 AZ나 데이터 센터에서 가동 중인 것을 의미
- 한 곳이 문제가 생겨도 다른 곳에서 처리할 수 있음

> EC2에서의 확장성 / 고가용성

- 수직 확장 : 인스턴스의 크기 늘림 (scale up/down)
- 수평 확장 : 인스턴스의 수 늘림 (scale out/in)
  - Auto Scailing Group
  - Load Balancer
- 고가용성 : 동일 애플리케이션의 동일 인스턴스를 다수의 AZ에 걸쳐 실행
  - Auto Scailing Group
  - Load Balancer

​     

---

## 1️⃣ Load Balancing

- 트래픽을 다운스트림의 여러 서버(EC2 인스턴스)로 전달하는 서버
- 애플리케이션의 단일 액세스 지점(DNS)만을 공개
- 어떤 인스턴스로 트래픽을 보낼 수 없는지 확인하여(health check) 다운스트림 인스턴스의 장애를 원할히 처리 가능
- 웹사이트의 SSL Termination 제공하여 암호화된 HTTPS 트래픽을 가질 수 있음
- 쿠키의 고정도를 강화할 수 있음
- 고가용성을 가짐
- 클라우드 내에서 개인 트래픽과 공공 트래픽을 분리할 수 있음

​    

### Elastic Load Balancer (ELB)

- 관리형 로드 밸런서
- AWS가 관리하며, 어떤 경우에도 작동할 것을 보장
- 업그레이드와 유지 관리 및 고가용성을 책임짐
- 작동 방식을 수정할 수 있게끔 일부 구성 놉(knob) 제공
- 다수의 AWS 서비스들과 통합되어 있음 (EC2, EC2 Auto Scaling Groups, ECS, ACM, CloudWatch, Route53, WAF, Global Accelerator)

> Health Check (상태확인)

- ELB가 EC2 인스턴스의 작동이 올바르게 되고 있는지 여부를 확인하기 위해 사용됨
- 제대로 동작하지 않으면 해당 인스턴스로 트래픽을 보낼 수 없음
- 포트와 라우트에서 이루어짐 (프로토콜: HTTP, Port: 4567, Endpoint: /health)
- EC2 인스턴스가 괜찮다면 HTTP 상태코드 200을 반환함
- 그렇지 않다면 인스턴스 상태가 좋지 않다고 기록하고 트래픽을 보내지 않음

> 관리형 로드밸런서 (4가지)

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

>  Target Groups (대상 그룹)이 될 수 있는 것들

- EC2 인스턴스
- ECS
- Lambda Functions
- 사설(private) IP 주소

​    

---

## 2️⃣ Auto Scale Group (ASG)

- 인스턴스의 수를 추가/삭제하는 방식인 스케일아웃/인을 의미
- EC2 인스턴스의 최대/최소갯수를 정할 수 있음
- ALB와 연동하여 사용하여 ASG의 각 인스턴스로 트래픽을 분산시킬 수 있음
- 비정상적으로 판단되는 인스턴스를 자동으로 종료하고, 새 인스턴스로 대체 (헬스체크)
- 비용은 무료이고, 생성되는 EC2에 대한 비용만 존재
- ASG를 생성하기 위해서는 Launch Template(시작 템플릿)을 만들어야함
- 시작 템플릿에는 ASG에서 EC2 인스턴스를 시작하는 방법에 대한 정보가 들어있음
  - AMI
  - 인스턴스 유형
  - EC2 사용자 데이터
  - EBS 볼륨
  - 보안 그룹
  - SSH 키페어
  - IAM 역할
  - 네트워크 / 서브넷
  - 로드밸런서
- 최소 인스턴스수(Mininum Capacity), 희망 인스턴스수(Desired Capacity), 최대 인스턴스 수(Maximum Capcity) 설정
- 초기 용량 지정
- CloudWatch를 통한 스케일링 정책 정의

> ASG 설정

![image-20230829001925909](AWS(3).assets/image-20230829001925909.png)

![image-20230829001949452](AWS(3).assets/image-20230829001949452.png)

![image-20230829002424919](AWS(3).assets/image-20230829002424919.png)

![image-20230829002509808](AWS(3).assets/image-20230829002509808.png)

![image-20230829002909247](AWS(3).assets/image-20230829002909247.png)

![image-20230829002925195](AWS(3).assets/image-20230829002925195.png)

![image-20230829002938454](AWS(3).assets/image-20230829002938454.png)

![image-20230829003014629](AWS(3).assets/image-20230829003014629.png)

> ASG에 의한 EC2 자동 시작확인

![image-20230829003532590](AWS(3).assets/image-20230829003532590.png)

![image-20230829003213546](AWS(3).assets/image-20230829003213546.png)

![image-20230829003237789](AWS(3).assets/image-20230829003237789.png)

![image-20230829003324952](AWS(3).assets/image-20230829003324952.png)

> ASG 시작템플릿 설정

![image-20230829002027655](AWS(3).assets/image-20230829002027655.png)

![image-20230829002047236](AWS(3).assets/image-20230829002047236.png)

![image-20230829002123709](AWS(3).assets/image-20230829002123709.png)

![image-20230829002132304](AWS(3).assets/image-20230829002132304.png)

![image-20230829002215619](AWS(3).assets/image-20230829002215619.png)

![image-20230829002223820](AWS(3).assets/image-20230829002223820.png)

​    

### 스케일링 정책

![image-20230829005626964](AWS(3).assets/image-20230829005626964.png)

> 동적 스케일 정책 (Dynamic)

1. 대상 추적 스케일링 (Target Tracking Scaling)

   - 가장 단순하고 설정하기 쉬움
   - 모든 EC2 인스턴스에서 ASG의 평균 CPU 사용률을 추적하여 원하는 수치에 머물수 있도록 할 때 사용

   ![image-20230829005932698](AWS(3).assets/image-20230829005932698.png)

   ![image-20230829010059137](AWS(3).assets/image-20230829010059137.png)

   ![image-20230829010357579](AWS(3).assets/image-20230829010357579.png)

2. 단순/단계 스케일링 (Simple / Step Scaling)
   - CloudWatch 경보를 설정하고, 전체 ASG의 CPU 사용률이 기준치를 초과하는 경우 인스턴스를 더 추가하도록 할 때 사용
   - CloudWatch 경보를 설정하고, 전체 ASG의 CPU 사용률이 기준치보다 떨어지는 경우 인스턴스를 제거하도록 할 때 사용

![image-20230829005858230](AWS(3).assets/image-20230829005858230.png)

![image-20230829005915936](AWS(3).assets/image-20230829005915936.png)

>  예약 작업 (Scheduled Actions)

- 사용 패턴을 바탕으로 스케일링 예상
- 특정 시간에 특정 이벤트가 발생할 것을 예상하고 ASG의 최소 용량을 그 시간에만 자동으로 늘리도록 설정

![image-20230829005711148](AWS(3).assets/image-20230829005711148.png)

> 예측 스케일링 (Predictive Scaling)

- AWS 내 오토스케일링 서비스를 활용하여 과거의 부하를 분석하고 예측을 생성하여 스케일링 작업을 예약함

![image-20230829005800183](AWS(3).assets/image-20230829005800183.png)

> 스케일 지표

1. CPU 사용률 (CPU Utilization)
   - 모든 인스턴스의 평균 CPU 사용률의 수치
2. 요청횟수 (RequestCountPerTarget)
   - EC2 인스턴스는 한 번에 대상별로 1000개의 요청까지만 최적으로 동작
3. 평균 네트워크 입출력량 (Average Network In/Out)
   - 애플리케이션이 네트워크와 연결된 경우
   - 업로드와 다운로드가 많아 EC2 인스턴스에 대해 네트워크에서 병목현상이 나타날 수 있을 때
4. 커스텀 지표
   - 사용자가 CloudWatch에서 직접 지표 지정

> 스케일링 휴지 (Cooldown)

- 스케일링 작업이 끝날 때마다 일정기간동안 휴지기간을 가짐
- 기본 휴지기간은 300초
- 이 기간에는 ASG가 추가 인스턴스를 실행/종료 할 수 없음
- 즉시 사용가능한 AMI를 이용하여 EC2 인스턴스의 구성시간을 단축하면, 휴지기간 또한 단축됨