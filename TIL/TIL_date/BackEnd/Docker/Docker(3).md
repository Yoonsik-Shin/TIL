# Docker (3)

## 1️⃣ Docker Compose

- 하나의 구성파일로 다수의 `docker build`와 `docker run` 명령어를 대체할 수 있는 도구 
- 도커 컴포즈는 `Dockerfile`을 대체하지는 않음
- 이미지나 컨테이너도 대체하지 않음
- 다수의 호스트에서 다중 컨테이너를 관리하는데는 적합하지 않음
- 하나의 동일한 호스트에서 다중 컨테이너를 관리하는데 좋음

​     

### 1. 파일작성

- `yml`이나 `yaml` 확장자 사용

```dockerfile
# docker-compose.yaml
vesrion: "3.8"   # 도커 컴포즈 버전

services:  # 컨테이너들을 정의
  mongodb:  # 컨테이너 이름
  	container_name: mongodb # 실제 컨테이너 이름을 강제로 지정해줌
    image: 'mongo' # 사용하는 이미지
  	volumes: # 볼륨설정
  	  - data:data/db:ro # 명명된 볼륨 (최상위 볼륨에 등록해야함)
  	  - 또 다른 볼륨
  	environment: # 각각의 환경변수 설정
  	  - TEST=test # (방법2)
  	  # TEST: test (방법1)
    networks:
      - 커스텀 네트워크

  backend:
  #	build: ./backend (short-form)
  	build: # 빌드해야하는 Dockerfile의 위치지정
  	  context: . # 도커파일 위치경로
  	  dockerfile: backend/Dockerfile-dev # 도커파일명
  	  args: # 도커파일 매개변수지정
  	  	some-arg: 100
  	ports:  # 포트포워딩
  	  - '8000:8000'
  	volumes:
  	  - logs:/app/logs # 명명된 볼륨 (최상위 볼륨에 등록해야함)
  	  - ./backend:/app # 바인드 마운트 (상대경로)
  	  - /app/node_modules # 익명볼륨
  	depends_on:
      - mongodb
         
  frontend:
  	build: ./frontend
  	env_file: # 환경변수파일 설정 (.env)
  	  - ./envs/dev.env
  	# -it 옵션
  	stdin_open: true
  	tty: true
 
  npm:
    build: node:14
  	entrypoint: [ "npm" ]
  	working_dir: /var/www/html
  	volumes: ./src:/var/www/html
  	      
# 도커가 services에 명명된 볼륨을 인식할 수 있게해주는 구문
volumes:
  data:
  logs:
```

​    

#### version

- 사용할 도커 컴포즈 버전

```yaml
vesrion: "3.8" 
```



#### services

- 사용할 컨테이너들을 정의
- docker compose를 사용하면 services에 정의한 모든 컨테이너가 동일한 네트워크의 일부가 됨
- services에서 정의해준 컨테이너 이름으로 컨테이너간 네트워킹을 할 수 있음

```yaml
services:
	# 컨테이너 이름
	mongodb:
	mysql:
	backend:
	frontend:
```

​    

> 각각의 컨테이너에서 사용할 수 있는 옵션들

1. 이미지

   - docker hub의 공식이미지 사용

   ```yaml
   image: "mongo"
   ```

   - `Dockerfile`의 커스텀 이미지 사용

   ```yaml
   # 방법1
   build: # 빌드해야하는 Dockerfile의 위치지정
     context: . # 도커파일 위치경로
     dockerfile: backend/Dockerfile-dev # 도커파일명
     args: # 도커파일 매개변수지정
     	some-arg: 100
     	
   # 방법2 - Short Form
   build: ./backend
   ```

2. 포트포워딩

```yaml
ports:
  - "8000:8000"
```

3. 환경변수 설정

- 환경변수 각각 설정

```yaml
# 방법1 - `-` 과 `=` 활용 (배열)
environment:
  - TEST=test
  
# 방법2 - `:` 활용 (객체)
environment:
  TEST: test 
```

- 파일로 설정

```yaml
env_file: # 환경변수파일 설정 (.env)
  - ./envs/dev.env
```

4. 볼륨설정

```yaml
volumes:
  - logs:/app/logs # 명명된 볼륨 (최상위 볼륨에 등록해야함)
  - ./backend:/app # 바인드 마운트 (상대경로)
  - /app/node_modules # 익명볼륨
```

5. 네트워크설정

```yaml
networks:
  - 커스텀 네트워크이름
```

6. 기타

- `container_name`: 실제 컨테이너 이름을 강제로 지정해줌

```yaml
container_name: mongodb
```

- `-it` 옵션

```yaml
stdin_open: true
tty: true
```

- `depends_on`
  - 도커컴포즈에만 존재하는 옵션    
  - 컴포즈파일에서 먼저 실행되어야하는 서비스들을 명시해줌

```yaml
depends_on:
  - mongodb
  - mysql
```

​    

#### Volumes

- 도커가 services에 명명된 볼륨(Named Volumes)을 인식할 수 있게 만들어주는 구문
- 익명볼륨과 바인드 마운트는 지정할 필요없음

```yaml
volumes:
  명명된 볼륨:
  logs:
```

​    

### 2. 서비스조작

#### 실행 (`up / run / start`)

##### `up`

```bash
# 기본 실행
$ docker-compose up

# detach 모드로 실행
$ docker-compose up -d
```

- 컴포즈 파일에서 찾을 수 있는 모든 서비스들이 시작됨
- 컨테이너를 시작할 뿐 아니라 필요한 모든 이미지도 가져와서 빌드함
- 서비스 중 일부만 실행할 수 도 있음

```bash
# 일부만 실행
$ docker-compose up 서비스명1 서비스명2 서비스명3
```

- 하나의 서비스에 `depends_on` 프로퍼티에 다른 서비스가 있을 경우, 하나의 서비스만 실행해도 같이 실행됨

> `--build`

```bash
$ docker-compose up --build
```

- 커스텀 이미지의 리빌드를 강제할 수 있음

​    

##### `run`

- 1회성이나 특별한 작업을 실행하기 위해 사용
- 컨테이너를 종료시켜도 자동으로 제거되지 않음
- `--rm` 옵션을 추가하면 컨테이너 종료시 자동 삭제됨
- 컨테이너에 대화식 터미널을 열고 컨테이너의 프로세스 종료 상태와 일치하는 종료 상태를 반환한다는 점에서 `docker run -it` 와 같이 작동

​    

##### `start`

- 이전에 생성되었지만 중지 된 컨테이너를 다시 시작하는 데 사용
- 새로운 컨테이너를 생성하지 않음

​    

#### 중지 (`down / stop`)

##### `down`

- container와 networks를 정지 및 삭제

```bash
$ docker-compose down
```

- 모든 서비스를 중지하고 모든 컨테이너를 제거
- 일반적으로 볼륨은 삭제되지않음
- 볼륨도 삭제하려면 `-v` 플래그 사용

```bash
$ docker-compose down -v
```

​    

##### `stop`

- container를 정지함 

​     

---

## 2️⃣ Utility Container

- 특정 환경만 포함하는 컨테이너
- 애플리케이션은 시작하지 않음
- 컨테이너를 시작할 때 이미지 이름 뒤에 부가 명령을 추가

```bash
$ docker exec -it 컨테이너이름 명령
```

- 호스트 머신에 모든 부가 도구를 설치하지않고 호스트 머신에 영향을 미치는 어떤 것을 실행하는 데 사용

```dockerfile
# dockerfile
FROM node:14-alpine
WORKDIR /app
```

```bash
$ docker run -it -v 절대경로바인드마운트 이미지이름 명령어
$ docker run -it -v /Users/yoonsik/...:/app mynpm npm init
```

​     

### ENTRYPOINT

- 미리 입력되어있는 명령어 

```dockerfile
# dockerfile
FROM node:14-alpine
WORKDIR /app
ENTRYPOINT [ "npm" ]
```

```bash
$ docker run -it -v 절대경로바인드마운트 이미지이름 init
```



### Docker-compose활용

```yaml
version: '3.8'

services: 
  단일서비스명:
  	build: ./
  	stdin_open: true,
  	tty: true,
  	volumes:
  	  - ./:/app
```

```bash
$ docker-compose run 단일서비스명
```

