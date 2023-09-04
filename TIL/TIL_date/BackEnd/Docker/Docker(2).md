# Docker (2)

## 1️⃣ 데이터 종류

 ### 1. Application

- 소스코드와 애플리케이션이 실행되는 환경
- 이미지가 빌드될 때 코드가 이미지에 복사됨
- 이미지 빌드시에 복사되었으므로 코드는 고정되어 변경될 수 없음
- Read-Only 속성을 가져야함

​    

### 2. Temporary App Data

- 애플리케이션이 실행되는 동안 생성된 데이터 (input 입력값)
- 메모리등에 임시저장
- 컨테이너가 종료되면 이 데이터을 모두 잃음
- Read + Write 속성을 가지고 있으며, 컨테이너에 존재함

​    

### 3.  Permanent App Data

- 데이터가 지속되어 실행중인 컨테이너에서 데이터를 활용
- 컨테이너가 중지된 후 다시 시작되어도 데이터가 보존됨
- Read + Write 속성을 가짐
- 컨테이너에 저장하지만, 볼륨의 도움을 받음

​    

---

## 2️⃣ Data Storages

### 1. Volumes

- 도커에 의해 관리됨
- 호스트 머신의 파일 시스템 상의 볼륨이 어디에 있는지 알 수 없음
- 컨테이너가 종료, 제거된 경우에도 볼륨을 통해 데이터를 유지할 수 있게 해줌
- 호스트 머신의 폴더으로 도커 컨테이너 내부의 폴더와 매핑됨
- 두 폴더의 변경사항이 다른 폴더에 반영됨
- 컨테이너는 볼륨에 데이터를 읽거나 쓸 수 있음

```dockerfile
# Dockerfile
VOLUME []
```

​        

#### 1-1. Anonymous Volumes

```dockerfile
# Dockerfile
VOLUME [ "/app/test"]
```

- 컨테이너가 존재하는 동안에만 실재함
- 하나의 특정 컨테이너에 밀접하게 연결되어있어 컨테이너 간의 데이터 공유는 불가능함
- 컨테이너가 제거되면 익명 볼륨도 같이 제거됨
- `--rm` 명령어로 실행된 컨테이너가 중지되면, 익명 볼륨은 자동으로 제거됨
- 옵션없이 컨테이너를 시작하고 제거하면 익명 볼륨은 제거되지않음
- 하지만, 컨테이너를 다시 실행할 때마다 새로운 익명 볼륨이 만들어져서 기존 익명 볼륨은 쓸모없게됨
- 데이터가 다른 모듈에 의해 덮어쓰여지는 것을 방지하는 데 사용됨

```bash
$ docker run -v /app/node_modules
```

```bash
$ docker volume prune # 익명볼륨 모두 삭제
```

​    

#### 1-2. Named Volumes

- 컨테이너가 종료된 후에도 볼륨이 유지돼 해당 폴더에 저장된 모든 데이터 계속 사용가능
- 영구적이어야 하는 데이터, 편집하지 않거나 직접 볼 필요가 없는 중요한 데이터에 적합
- 하나의 컨테이너에 종속되지 않아, 여러 컨테이너 간의 데이터 공유가능
- Dockerfile 내부에서는 Named Volumns 생성불가
- docker run시에 `-v` 옵션 사용

```bash
$ docker run -v 이름:/app/test
```



### 2. docker volume CLI

#### `help`

- docker volume 명령어 모음

```bash
$ docker volume --help
```

​    

#### `ls`

- 현재 활성화중인 볼륨을 모두 보여줌
- 바인트 마운트는 도커에 의해 관리되는 볼륨이 아니여서 안나옴

```bash
$ docker volume ls 
```

​    

#### `create`

- 수동으로 볼륨 생성

```bash
$ docker volume create 볼륨명
```



#### `rm / prune` 

- `rm` : 하나의 볼륨 제거
- `prone` : 사용하지 않는 모든 볼륨 제거

```bash
$ docker volume rm 볼륨명
$ docker volume prone
```

​    

#### `inspect`

- 볼륨에 대한 정보를 보여줌
- `Mountpoint` 프로퍼티는 실제로 데이터가 저장되는 호스트 머신상의 경로 (실제 경로는 아니라 시스템에서 찾을 수는 없음)
- `Options` 프로퍼티로 `Read-Only` 속성 적용여부 확인가능

```bash
$ docker volume inspect 볼륨명
```

​    

### 3. BInd Mounts

- 개발 중 도커를 사용하는 경우에 코드의 변경사항이 반영되는 것이 중요함
- 위 동작이 안되면 매번 전체 이미지를 리빌드해고, 컨테이너를 재시작해야함
- 개발자가 호스트 머신상에 매핑될 컨테이너의 경로를 설정
- 하나의 컨테이너에 종속되지 않아, 여러 컨테이너 간의 데이터 공유가능
- 컨테이너 종료 및 제거후에도 유지됨
- 바인트마운트를 삭제하고 싶으면 호스트 머신에서 삭제 (도커 명령어로는 삭제할 수 없음)
- 소스코드의 스냅샷을 복사하는 게 아닌, 바인트마운트에서 복사하여 컨테이너는 항상 최신코드에 엑세스 할 수 있음
- 영구적이고 편집가능한 데이터에 적합
- 실행하는 컨테이너에만 적용되므로 이미지에는 영향을 주지 않아 Dockerfile 내부에서 설정할 수 없음
- 컨테이너를 실행할 때 터미널에서 바인트마운트 설정

```bash
# 폴더 to 폴더
$ docker run -v 호스트머신상의폴더절대경로:도커내부폴더경로 

# 파일 to 파일도 가능
$ docker run -v 호스트머신상의파일절대경로:도커내부파일경로

# 예시
$ docker -v "/Users/yoonsik/development/test:/app"
```

- 도커가 호스트 머신의 로컬파일을 덮어쓰지 않고, 로컬파일이 도커 컨테이너에 있는 내용을 덮어씀
- 외부에서 덮어쓰지 않았으면 하는 부분이 있다는 걸 도커에 알려야함
- 도커 컨테이너에 익명 볼륨 추가

```bash
$ docker run 
>	-v "/Users/yoonsik/development/test:/app"
>	-v /app/node_modules # 익명볼륨
```

```dockerfile
# Dockerfile
Volume ["/app/node_module"] # -v /app/node_modules 옵션과 같음
```

- 도커는 모든 볼륨을 평가하고, 충돌이 있을 경우 더 길고 구체적인 내부경로를 우선시함

```bash
/app/node_module✔️  >> /app
# /app의 node_module 폴더를 제외한 나머지는 외부에서 덮어씌워짐
```



>바인트마운트가 있는데 COPY 명령어를 사용하는 이유

- `docker run` 명령어는 개발중에 사용하는 명령어
- 개발중에는 코드의 변경사항을 실행중인 컨테이너에 즉시 반영
- 배포시에는 바인트 마운트를 사용하지 않고, `COPY` 명령어의 결과인 스냅샷을 활용함

​    

### 4. Read-Only Volumes

- 볼륨은 기본적으로 `read-write` (컨테이가 볼륨에서 데이터를 읽고 쓸 수 있음)
- read-only 옵션을 통해 읽기전용으로 설정할 수 있음 (`volume_path:ro`)

```bash
$ docker run -v "/Users/yoonsik/development/test:/app:ro"
```

- 옵션 적용에서 제외되어야하는 파일은 볼륨 설정을 통해 제외할 수 있음

```bash
$ docker run 
>	-v "/Users/yoonsik/development/test:/app:ro" 
>	-v /app/temp  # read-only 적용 제외
> 	-v feedback:/app/temp # read-only 적용 제외
```

​    

---

## 3️⃣ 도커네트워킹

### 1. 웹 통신

- 기본적으로 컨테이너는 www에 요청을 보낼 수 있음
- 도커화된 애플리케이션 내부에서 웹 API나 웹페이지와 통신가능
- 특별한 설정 필요없이 자동으로 동작함

​    

### 2. 로컬호스트 통신

- 도커화된 컨테이너 코드와 로컬 호스트 머신간의 통신
- 통신을 위해서는 `localhost`를 도커가 이해할 수 있는 특별한 도메인인 `host.docker.internal`로 대체해야함

```js
// 일반적인 통신 도메인
'mongodb://localhost:27017/aaa'
'http://localhost:3000'

// 로컬호스트 - 도커 통신
'mongodb://host.docker.internal:27017/aaa'
'http://host.docker.internal:3000'
```

​    

### 3. 컨테이너간 통신

- 서로 다른 도커 컨테이너끼리 통신

​     

#### 도커 IP주소

- 도커가 가지는 IP주소를 이용하여 통신
- IP주소를 하드코딩하기 때문에 컨테이너의 IP주소 변경될 때마다 매번 새 이미지를 빌드해야해서 좋은 방법은 아님

```bash
$ docker container inspect 컨테이너명

...
"NetworkSettings" : {
	"IPAddress": "172.11.05.3"
	...
}
...
```

```js
'mongodb://172.11.05.3:27017/aaa'
```

​    

#### `--network` 옵션

- `docker run` 명령에 `--network` 옵션 추가하면 모든 컨테이너를 하나의 동일한 네트워크에 존재하여 서로 통신가능
- 같은 네트워크상에서는 도커가 자동으로 IP조회 및 연결을 수행함
- 네트워크는 도커가 자동으로 생성하지 않아 직접 만들어줘야함

```bash
# 도커 네트워크 생성
$ docker network create 네트워크이름

# 도커 네트워크 리스트보기
$ docker network ls

# 생성한 네트워크에 도커 연결하여 실행
$ docker run --network 네트워크이름
```

- 다른 컨테이너의 이름을 도메인으로 사용

```js
'mongodb://mongodb:27017/aaa'
```

​     

> 도커 네트워크 드라이버

- 네트워크 생성시 `--driver` 옵션으로 설정가능

```bash
$ docker network create --driver 네트워크옵션 네트워크이름
```

- 대부분의 시나리오에서 `bridge` 드라이버가 가장 적합
- 종류
  - `host` : 스탠드얼론 컨테이너의 경우, 컨테이너와 호스트 시스템간의 격리가 제거됨 (localhost를 네트워크로 통신)
  - `overlay` : 거의 사용 안함 
  - `macvlan` : 컨테이너에 custom MAC주소를 설정하여 이 주소로 컨테이너와 통신가능
  - `none` : 모든 네트워킹 비활성화
  - 서드파티 플러그인

​    
