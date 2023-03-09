# Docker (2)

​    

## 1️⃣ 컨테이너

- 애플리케이션을 실행하는 전체환경을 포함하는 작은 패키지
- 이미지의 구체적인 실행 인스턴스
- 소프트웨어 실행 유닛이 실행됨

​    

---

## 2️⃣ 이미지

- 모든 설정 명령과 모든 코드가 포함된 공유 가능한 패키지
- 실제 코드와 코드를 실행하는데 필요한 도구를 포함
- 이미지를 정의하면 여러개의 동일한 환경의 컨테이너를 만들어 낼 수 있음 (블루프린트)
- 읽기 전용
- 스스로 실행되지 않고 컨테이너로만 실행될 수 있음

​    

### 이미지 생성

- 이미 존재하는 이미지 사용 (dockerhub)
- 자신만의 이미지 만들어 사용 (Dockerfile)

```dockerfile
# Dockerfile
FROM node
WORKDIR /app
COPY . /app
RUN npm install
EXPOSE 80 
CMD node server.js
```

​    

- `FROM` : 다른 이미지에서 자신이 필요로 하는 이미지를 가져옴

```dockerfile
FROM `이미 존재하는 이미지`
```

​    

- `WORKDIR` : 컨테이너 내의 작업 디렉토리 설정

```dockerfile
WORKDIR `도커내부 작업 디렉토리`
```

> `./` : 도커 컨테이너의 현재 작업 디렉토리를 의미

​    

- `COPY` : 로컬파일들을 컨테이너로 복사

```dockerfile
COPY `복사될 자료` `복사된 자료를 이미지에 넣을 경로`
```

​    

- `RUN` : 이미지에 명령 내리기

```dockerfile
RUN `npm 파일 설치하기`
```

​    

- `EXPOSE` : 컨테이너 실행시, 로컬 시스템에 특정포트를 노출

```dockerfile
EXPOSE `로컬에서 사용할 포트번호`
```

​    

- `CMD` : 이미지가 생성될 때 실행되지 않고, 컨테이너가 시작될 때 실행됨

```dockerfile
CMD ["node", "server.js"]
```

> 배열 구조로 명령어를 입력해줘야함 

​    

### 이미지 레이어

- 기본적으로 명령어를 다시 실행했을 때의 결과 이전과 동일하고 추론하면 캐시된 데이터를 가져옴
- 다시 실행해야 하는 항목만 다시 빌드하여 이미지 생성속도를 빠르게함
- 레이어 활용 최적화 예시

```dockerfile
# Dockerfile
FROM node
WORKDIR /app

COPY package.json /app # 패키지는 따로 관리
RUN npm install

COPY . /app # 코드 변경시 패키지에는 영향x
EXPOSE 80 
CMD node server.js
```

​    

---

## 3️⃣ 주요 명령어

### 도움말

```bash
$ docker [command] --help
```



### `build`

- `Dockerfile`을 빌드하고 파일을 기반으로 자신만의 이미지 생성

```bash
$ docker build . # Dockerfile이 있는 위치에서 실행해야함
```

- `-t`

```bash
$ docker build -t `name:tag` .
$ docker build -t goals:13 .
```

- `name `: 이미지의 일반적인 이름 설정 (리포지토리)
- `tag` : 이미지의 특정화된 버전 정의

​    

### `tag`

- 이미 존재하는 이미지를 복사한 후 새로운 태그를 부여

```bash
$ docker tage `기존 name:tag` `새로운 name:tag`
```

​    

### `run`

- 이미지를 기반으로 __새 컨테이너__를 만들고, 새 컨테이너를 실행
- `-p (publish)` : 로컬의 포트로 내부 도커 포트를 엑세스

```bash
$ docker run -p `로컬포트:도커포트` `이미지ID or 이름 or 태그`
$ docker run -p 3000:80 34abda4213
```

- `-i` : 인터렉티브 모드
  - 표준 입력을 열린상태로 유지
  - `attached`모드가 아니여도 무언가를 입력할 수 있게 해줌
- `-t` : 터미널 생성
- `-it` : 터미널에 입력가능한 상태로 만들어줌

```bash
$ docker run -it `이미지ID`
```

- `--rm` : 컨테이너가 중지되었을 때 자동으로 삭제되도록 설정

```bash
$ docker run --rm `이미지ID`
```

- `--name` : 컨테이너 이름설정

```bash
$ docker run --name `커스텀 컨테이너 이름` `이미지ID`
```

​    

### `ps`

- 현재 실행중인 프로세스만 표시

```bash
$ docker ps
```

- 모든 프로세스 표시

```bash
$ docker ps -a
```

​    

### `stop`

- 실행중인 컨테이너 종료

```bash
$ docker stop `컨테이너ID or 이름 or 태그`
```

​    

### `start`

- 종료된 컨테이너 실행

```bash
$ docker start `컨테이너ID or 이름 or 태그`
$ docker start -ai `컨테이너ID` # 입력값이 있을 경우
```

​    

### `Attached vs Detached`

- `Detached`

  - 컨테이너는 실행중이지만, 터미널과는 연결되어있지 않음
  - __docker start__ 로 실행시 default
  - `docker run`에서 detached 모드로 실행

  ```bash
  $ docker run -d `컨테이너ID`
  ```

  - detached 상태에서 생성된 로그보기

  ```bash
  $ docker logs `컨테이너ID or 이름`
  $ docker logs -f `컨테이너ID or 이름` # Attached 상태로 만듬
  ```

​    

- `Attached`

  - __docker run__으로 실행시 default
  - 실행중인 컨테이너와 다시 연결하기

  ```bash
  $ docker attach `컨테이너ID or 이름`
  ```

  - 실행중지된 컨테이너 다시 실행시에 attached 모드로 실행

  ```bash
  $ docker start -a `컨테이너ID or 이름`
  ```

​        

### `rm`

- 컨테이너 삭제
- 삭제하기전에 컨테이너가 실행종료상태여야함

```bash
$ docker rm `컨테이너ID or 이름`
```

​    

### `images`

- 현재 가지고있는 모든 이미지 표시

```bash
$ docker images
```

​    

### `rmi`

- 이미지 삭제
- 이미지로 생성된 컨테이너가 먼저 삭제되어야 이미지 삭제가능

```bash
$ docker rmi `이미지ID or 이름`
```

​    

### `image prune`

- 사용되지 않는 모든 이미지 제거

```bash
$ docker image prune
```

​    

### `image inspect`

- 이미지에 대한 정보

```bash
$ docker image inspect `이미지ID`
```

​     

### `cp`

- 실행중인 컨테이너 안에서 밖으로 or 밖에서 안으로 파일이나 폴더를 복사할 수 있음

```bash
$ docker cp `폴더or파일` `복사경로(컨테이너이름:컨테이너내부경로)`

# 로컬 >>> 도커내부
$ docker cp dummy/. aaa:/test

## 도커내부 >>> 로컬
$ docker cp aaa:/test dummy
```

​    



---

## 4️⃣ 이미지 공유하기

- 방법
  1. `Dockerfile` 공유하기
  2. `DockerHub` 이용하기



### [DockerHub](https://hub.docker.com/)

- 레포지토리 만들기

![image-20230309022217005](Docker(2).assets/image-20230309022217005.png)

![image-20230309022246843](Docker(2).assets/image-20230309022246843.png)

> Private는 계정당 한개만 만들수 있음

![image-20230309022338250](Docker(2).assets/image-20230309022338250.png)

- 로그인

```bash
$ docker login
```

- 로그아웃

```bash
$ docker logout
```

​    

### `push`

```bash
$ docker push `dockerhub아이디/레포이름:태그이름`
$ docker push yoonsikshin/test:tagname
```

​    

### `pull`

- 최신 이미지만 가져옴

```bash
$ docker pull `dockerhub아이디/레포이름:태그이름`
```

- pull받지 않고 `docker run`을 실행하면 로컬에서 파일 못 찾으면, dockerhub로 접근시도
- 만약 이전에 사용한 로컬파일이 있다면 `docker run` 만으로는 최신 업데이트된 이미지를 제공받지 못함
