# Docker (1)

​    

## 기본개념

- 개발환경을 동일하게 맞추기 위해 사용
- 가상머신과 비슷한 개념이지만 더 빠르고, 자원을 효율적으로 사용
- 추가적으로 운영체제 설치가 필요없음

   

## 설치

- 우분투

```bash
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
$ sudo apt update
$ apt-cache policy docker-ce
$ sudo apt install docker-ce
```

- 윈도우

>  [WSL2 설치가이드](https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/)

- 도커사이트

> [Docker](https://www.docker.com/)

​    

---

## `Dockerfile`

- 컨테이너를 실행하기전에 먼저 이미지를 만들어 줘야함

```dockerfile
// Dockerfile
FROM node:14  # 노드가 설치된 컴퓨터 불러오기

COPY ./index.js /myfolder/  # 내 컴퓨터의 index.js를 가상 컴퓨터속 myfolder에 복사

WORKDIR /myfolder/  # 명령어를 실행할 작업 폴더 지정

CMD node index.js  # 실행
```

​     

### `docker build`

- 설명서를 하나로 묶여진 이미지로 만들어줌

```bash
$ docker build .
```

- 빌드가 완료됐는지 확인

```bash
$ docker images
```

​    

### `docker run`

- 만들어진 이미지로 새로운 가상컴퓨터 만들기

```bash
$ docker run 이미지ID
```

- 이미지를 실행하면 가상 컴퓨터가 하나 만들어짐
- 도커를 통해 만들어진 가상컴퓨터를 _컨테이너_라고 부름

​    

- 실행되고 있는 프로그램 확인

```bash
$ docker ps
$ docker ps -a  # 종료된 컨테이너까지 보여줌
```

​    

- 종료된 컨테이너 삭제

```bash
$ docker rm 컨테이너ID
```

​    

### `docker stop`

- 실행되고 있는 컨테이너 정지

```bash
$ docker stop 컨테이너ID
```



---

## `.dockerignore`

- 기존에 있는 `node_modules` 폴더의 복사를 방지하기 위해 사용

```dockerfile
# .dockerignore
node_modules
```

​    

---

## 도커 내부 접속

```bash
$ docker exec -it 컨테이너ID /bin/bash
```

- 화면이 bash쉘로 바뀜
- 도커가 돌아가고 있는 가상 컴퓨터의 터미널로 들어온 것을 의미

​    

----

## 포트포워딩

- 내 컴퓨터의 포트와 가상컴퓨터의 포트를 연결해주는 것

```bash
$ docker run -p 8000:3000 이미지ID  # 내컴퓨터 8000포트 : 가상컴퓨터 3000포트
```

​    

---

## package.json과 Docker

- 도커는 미리 설치된 것들을 캐싱하고 있음
- 소스코드 수정이 발생한 부분 이후의 과정을 다시 실행함
- `package.json`에서 수정된 부분이 없는 파일들도 불필요하게 다시 설치됨

```dockerfile
// Dockerfile
COPY . /myfolder/
RUN yarn install
# 위와 같은 순서로 실행시키면 소스코드의 일부만 수정해도 `yarn install` 명령어가 다시 실행되는 경우가 발생
```

- 이를 해결하기 위해 아래와 같은 순서로 작성해줘야함

```dockerfile
// Dockerfile

FROM node:14

WORKDIR /myfolder/
COPY ./package.json /myfolder/
COPY ./yarn.lock /myfolder/
RUN yarn install

COPY . /myfolder/
CMD yarn dev
# 위와 같이 작성하면 package.json과 yarn.lock 파일 수정시에만 `yarn install`이 다시 실행됨
```

