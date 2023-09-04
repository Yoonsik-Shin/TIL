# Docker (4)

## Deploy

### 1️⃣ 단일 컨테이너 애플리케이션 수동 배포

#### 1. EC2 Docker 설치

```bash
# EC2 터미널
$ sudo yum update -ysudo yum -y install docker
$ sudo service docker start
$ sudo usermod -a -G docker ec2-user
# 위 명령 실행 후 반드시 다시 로그인한 후 아래 명령어 진행
$ sudo systemctl enable docker
$ docker version
```

#### 2. 이미지 도커허브 업로드

```bash
# 이미지 빌드
$ docker build -t 이미지명:태그 .

# 도커허브 로그인
$ docker login

# 도커허브에 이미지 업로드
$ docker push 이미지명:태그
```

#### 3. EC2에서 배포한 이미지 실행

```bash
# EC2 터미널
# 도커허브에서 이미지 다운로드
$ sudo docker pull 이미지명:태그

# 컨테이너 실행
$ sudo docker run -p 8000:8000 이미지명:태그

# 컨테이너 확인
$ sudo docker ps
```

​    

> 코드변경시 EC2 반영 프로세스

1. 이미지 리빌드

   ```bash
   $ docker build -t 이미지명:태그 .
   ```

2. 도커 허브에 새 이미지 업로드 (push)

   ```bash
   $ docker push 이미지명:태그
   ```

3. EC2에서 새 이미지 다운로드 (pull)

   ```bash
   $ sudo docker pull 이미지명:태그
   ```

4. EC2에서 다시 컨테이너 시작

   ```bash
   $ sudo docker run -p 8000:8000 이미지명:태그
   ```

​    

> EC2 배포의 장단점

- 개발자가 모든 것을 관리함
- 보안적인 문제가 생길 수 있음
- 소프트웨어 업데이트를 수동으로 해야함
- 방화벽 관리를 수동으로 해줘야함

​    

---

### 2️⃣ 관리형 리모트 머신 (ECS)

- 컨테이너의 구동, 실행, 모니터링등 컨테이너의 관리를 도와주는 서비스
- AWS에서 세부적인것은 관리해줌
- 컨테이너 배포 및 실행이 더 이상 도커명령으로 수행되지 않음
- ECS는 프리티어가 없어 과금이 될 수 있음

클러스터

컨테이너

태스크

서비스