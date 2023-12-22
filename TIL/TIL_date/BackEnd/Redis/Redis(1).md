# Redis

## 0️⃣ 개요

- Remote Dictionary Server
- 다수의 서버를 사용하는 분산환경 서버가 공통으로 사용할 수 있는 해시 테이블
- 표준 C로 작성된 오픈소스 인메모리 DB
- key-value DB

​    

### 특징

1. 인메모리 (In-Memory)
   - 백업을 제외한 모든 데이터를 RAM에 저장
2. 싱글쓰레드 (Single Threaded)
   - 단일  쓰레드에서 모든 task를 처리함
3. 클러스터 모드 (Cluster Mode)
   - 다중 노드에 데이터를 분산 저장하여 안정성 및 고가용성을 제공함
4. 영속성 (Persistence)
   - Redis Database(RDB)와 Append only file (AOF)를 통해 영속성 옵션을 제공함
5. Pub / Sub
   - Pub / Sub 패턴을 지원하여 채팅, 알림들의 기능을 쉽게 구현가능

​    

### 장점

1. 높은 성능
   - 모든 데이터를 메모리에 저장하여 매우 빠른 읽기 쓰기 속도를 보장함
2. 데이터 타입 지원
   - Redis에서 제공하는 다양한 타입으로 다양한 기능 구현 가능
3. 하나의 언어에 종속되지 않음
   - Python, Java, JavaScript등 다양한 언어로 작성된 클라이언트 라이브러리를 지원함

​    

### 사용사례

1. 캐싱 (Caching)
   - 임시 비밀번호 
   - 로그인 세션
2. 비율 계산기 (Rate Limiter)
   - 서버에서 특정 API에 대한 요청 횟수를 제한하기 위해 사용하는 기술
   - Fixed-Window
   - Sliding-Window
3. 메시지 브로커 (Message Broker)
   - 메시지 큐로 사용하여 서비스 간의 커플링 줄임
4. 실시간 분석 / 계산수
   - 순위표 (Rank, LeaderBoard)
   - 반경탐색 (GeoFencing)
   - 방문자 수 계산 (Visitors Count)
5. 실시간 채팅
   - Pub/Sub 패턴

​    

### 영속성

- Persistence
- 주로 캐시로 사용되지만 데이터 영속성을 위한 옵션도 제공함
- 안정적인 캐시 서버 운영을 위해 데이터 손실을 방지하기 위한 옵션을 제공

​     

#### RDB

- Redis Database
- 특정 시간의 스냅샷을 생성하는 기술
- 장애가 발생했을 때, 특정 시점에 스냅샷으로 빠르게 캐시를 되돌리거나, 동일한 데이터를 가진 캐시를 복제할 때 사용
- 새로운 스냅샷이 생성되기 이전에 일부 데이터의 유실이 있을 수 있음
- 스냅샷 생성중에 전체적인 레디스 서버의 성능 저하가 발생하여 클라이언트 처리에 지연이 발생할 수 있음

​    

#### AOF

- Append Only File
- Redis에 저장되는 모든 Write 작업을 모두 log로 저장하는 기술
- 데이터 유실 없이 거의 모든 데이터에 대한 싱크를 맞출 수 있지만, 재난 복구시 모든 로그를 다시 적용해야 하기 때문에 스냅샷 방식보다 복구되는 속도가 느림

​    

### 캐싱

- 데이터를 빠르게 읽고 처리하기 위해 임시로 저장하는 기술
- 계산된 값을 임시로 저장해두고, 동일한 계산/요청이 발생시 저장된 값을 바로 사용



#### 사용사례

1. CPU 캐시
   - CPU와 RAM 속도차이로 발생하는 지연을 줄이기 위해 L1, L2, L3 캐시 사용
2. 웹 브라우저 캐싱
   - 웹 브라우저가 웹 페이지 데이터를 로컬 저장소에 저장하여 해당 페이지 재방문시에 사용
3. DNS 캐싱
   - 이전에 조회한 도메인 이름과 해당하는 IP 주소를 저장하여 재요청시 사용
4. DB 캐싱
5. CDN
   - 원본 서버의 컨텐츠를 PoP 서버에 저장하여 사용자와 가까운 서버에서 요청을 처리함
6. 애플리케이션 캐싱
   - 애플리케이션 데이터, 계산 결과를 캐싱



#### Cache Hit / Miss

> Cache Hit

- 캐시서버에 특정 키를 가진 캐시를 요청했을 때, 정상적으로 응답이 오는 경우
- 캐시 데이터가 존재하는 경우

> Cache Miss

- 키가 잘못되었거나, 해당 데이터가 이미 만료되어 데이터를 응답하지 못한 경우



#### Cache Aside

- 애플리케이션에서 클라이언트에 요청을 처리할 때 먼저 캐시를 조회하여 캐시 히트면 캐시를 사용, 미스면 원본 스토리지에서 데이터를 조회하여 데이터를 캐싱하는 패턴

​    

---

## 1️⃣ 설치 및 실행

```bash
$ curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

$ echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

$ sudo apt-get update

$ sudo apt-get install redis

# 레디스 실행
$ sudo service redis-server start
```

​    

---

## 2️⃣ 데이터 타입

### Strings

- 문자열, 숫자, JSON string 타입 저장

```bash
# 단일 키값 저장 / 조회
$ SET <key> <value>
$ GET <key>

# 다중 키값 저장 / 조회
$ MSET <key1> <value1> <key2> <value2> <key3> <value3> ...
$ MGET <key1> <key2> <key3>

# 숫자형 문자열 값 증감
$ INCR <숫자형 문자열>
$ INCRBY <숫자형 문자열> <증감값>
price = 100
$INCR price >> 101
$INCBY price 9 >> 110

# JSON string값 저장
$ SET <key> <JSON string값>
$ SET yoonsik '{"name": "shin", "age": 27}'
```

- key에서 `:`을 이용하여 데이터의 의미를 구분하여 데이터 저장

```bash
$ SET yoonsik:shin:28 good
```

​    

#### Strings 활용

1. OTP (One Time Password)
   - 인증을 위해 사용되는 임시 비밀번호
2. 분산락 (Distributed Lock)
   - 분산 환경의 다수 프로세스에서 동일한 자원에 접근할 때, 동시성 문제 해결
   - `NX` 옵션을 통해 키가 존재하지 않는 경우에만 Lock을 획득할 수 있도록 하고, 이미 존재하여 Lock을 획득할 수 없는 경우 `(nil)`을 리턴하여 프로세스를 대기시킴
3. 비율 계산기 (Rate Limiter)
   - 시스템의 안정성과 보안을 위해 요청의 수를 제한하는 기술
   - 종류로는 IP / User / Application 기반이 있음
   - 횟수를 카운트하는 기준에 따라 여러가지 방법이 있음
   - `Fixed-window Rate Limiting` : 고정된 시간안에 요청 수를 제한하는 방법

​    

### Lists

- String을 Double Linked List로 저장하는 데이터 타입
- 양 끝에 데이터를 추가하거나 삭제하는 연상에 최적화 되어 있음
- Queue / Stack 을 쉽게 구현 가능

```bash
# 데이터 삽입 (Left: current >> Right: old) 
$ LPUSH <리스트명> job1 job2 job3 # job1: old, job3: current

# 가장 먼저 넣은 자료 추출
$ RPOP <리스트명>

# 가장 최신에 넣은 자료 추출
$ LPOP <리스트명>
```

- 리스트 슬라이싱

```bash
# 조회
$ LRANGE <리스트명> <시작 인덱스> <종료 인덱스>
$ LRANGE queue -3 -1

# 뽑아내기
$ LTRIM <리스트명> <시작 인덱스> <종료 인덱스>]
$ LTRIM queue 0 1
```

​    

#### Lists 활용

- 소셜 네트워크 활동피드 (SNS Activity Feed)

  - 사용자 / 시스템과 관련된 활동이나 업데이트를 시간순으로 정렬하여 보여주는 기능

  - `Fan-Out` : 단일 데이터를 한 소스에서 여러 목적지로 동시에 전달하는 메시징 패턴

​    

### Sets

- 중복없이 유니크한 string 값을 저장하는 정렬되지 않은 집합
- 중복을 제거해줌
- 교집합 (intersection), 합집합 (union), 차집합 (difference)

```bash
# set 값 저장
$ SADD <key> <value1> <value2> <value3> <value3> ...

# set의 모든 멤버(값들) 조회
$ SMEMBERS <key>

# set의 카디널리티를 출력 (고유한 아이템의 개수)
$ SCARD <key>

# set에 특정 아이템이 포함되어있는지 확인
$ SISMEMBER <key>
```

- 집합간의 연산

```bash
# 교집합
$ SINTER <key1> <key2>

# 차집합 (key1 기준)
$ SDIFF <key1> <key2>

# 합집합
$ SUNION <key1> <key2>
```

​    

#### Sets 활용

- 장바구니

  - 사용자가 구매를 원하는 상품을 임시로 모아두는 가상공간

  - 수시로 변경될 수 있고, 실제 구매로 이어지지 않을 수 있다.

​    

### Hashes

- field-value 구조를 갖는 데이터 타입
- dictionary나 map과 유사한 개념
- 다양한 속성을 갖는 객체의 데이터를 저장할 때 유용

```bash
# key-value는 하나의 field
$ HSET <해시값> <key1> <value1> <key2> <value2> <key3> <value3> ...

# 하나의 field값 조회
$ HGET <해시값> <조회할 key>

# 다수의 field값 조회
$ HMGET <해시값> <key1> <key2> ...

# 숫자형으로 저장된 field값 조작
$ HINCRBY <해시값> <숫자가 저장된 key> <증감값>
```

​    

#### Hashes 활용

- 로그인 세션
  - 사용자의 로그인 상태를 유지하는 기술
  - 로그인시 세션의 개수를 제한하여, 동시에 로그인 가능한 디바이스 개수를 제한하는데 사용됨

​    

### Sorted Sets (Zset)

- 중복없이 유니크한 string 값을 저장하는 set과 유사하지만, Score라는 추가적인 Field를 통해 데이터를 미리 정렬해놓는 데이터 타입
- Redis의 독특한 데이터 타입 중 하나
- Skip List와 Hash Table로 이루어져 있음
- 값을 추가하는 순간에 Score에 의해 정렬을 유지함
- Score가 동일한 값이 존재한다면 사전 편찬(Lexicographically) 순으로 정렬됨
- Zset으로도 불림

```bash
# sorted set에 값 저장
$ ZADD <key> <score1> <value1> <score2> <value2> <score3> <value3> ...

# sorted set 값만 조회
$ ZRANGE <key> 0 -1

# sorted set 값과 스코어 같이 조회
$ ZRANGE <key> 0 -1 WITHSCORES

# 내림차순 조회
$ ZRANGE <key> 0 -1 REV

# 랭킹 반환 (0부터 시작하는 인덱스 값과 동일)
$ ZRANK <key> <value>
```

​     

#### Sorted Sets 활용

- Sliding Window Rate Limiter
  - 시간에 따라 window를 이동시켜 동적으로 요청수를 조절하는 기술
  - Fixed window는 window 시간마다 허용량이 초기화되지만, Sliding window는 시간이 경과함에 따라 window가 같이 움직인다.

​    

### Streams

- Append only log에 Comsumer groups과 같은 기능을 더한 자료 구조
- 카프카와 같은 이벤트 스트리밍 플랫폼과 유사한 부분이 있음
- Stream에 추가되는 이벤트/메시지는 고유 ID를 가짐
- 고유 ID는 Stream에 추가되는 시간과 순서를 기준으로 Redis가 자동으로 할당함
- 고유 ID를 통해 하나의 Entry를 읽을 때, O(1)의 시간복잡도를 갖게함
- 분산 시스템의 다수 컨슈머에서 안전하게 메시지를 컨슈밍할 수 있도록 Consumer Group이라는 기능을 포함함
- Comsumer Group을 이용하면 다수의 컨슈머가 메시지를 처리하면서도 동일한 메시지를 중복처리하는 문제를 쉽게 해결할 수 있음

```bash
# Stream에 Entry 추가
# key 이후에 *를 사용하면 자동으로 고유 ID가 할당됨
$ XADD <key> * 
$ XADD events * 유저1이 유저2를 팔로우함
>> "1643253453454-0" # 고유 ID

# 다수의 메시지를 조회 (리스트와 유사)
# - : 가장 처음 들어갔던 이벤트 / + : 가장 마지막에 들어갔던 이벤트 
$ XRANGE <key> - + 
>> 1) 1) "1643253453454-0"
      2) 1) "유저1이"
      	 2) "유저2를"
      	 3) "팔로우함"

# 완료된 메시지 Stream에서 제거
$ XDEL <key> ID
```

> Append only log

- DB나 분산 시스템에 주로 사용되는 데이터 저장 알고리즘
- 데이터가 수정되거나 삭제되지 않고 항상 추가만 되는 구조

​    

### Geospatials

- 좌표를 저장하고, 검색하는 데이터 타입
- 거리 계산, 범위 탐색등을 지원함

```bash
$ GEOADD <key> <longitude1> <latitude1> <value1> <longitude2> <latitude2> <value2> # 경도 위도 순
$ GEOADD seoul:station
	126.923917 37.556944 hong-dae
	127.027583 37.497928 gang-nam

# 두 좌표사이의 거리
$ GEODIST <key> <value1> <value2> [ M | KM | FT | MI ]
$ GEODIST seoul:station hong-dee gang-name KM
```

​    

#### Geospatials 활용

- `Geofencing` : 위치를 활용하여 지도 상의 가상의 경계 or 지리적 영역을 정의하는 기술

```bash
$ GEOADD <key>
	 <longitude1> <latitude1> <value1>
	 <longitude2> <latitude2> <value2>
	 <longitude3> <latitude3> <value3>
	 <longitude4> <latitude4> <value4>
	 
$ GEORADIUS <key>
	<longitude1> <latitude1> <value1> <거리> [ M | KM | FT | MI ]
```

​    

### Bitmaps

- 실제 데이터타입이 아닌, String에 binary 연산을 적용한 것
- 최대 42억개(2^32)의 binary 데이터를 표현할 수 있음 
- 적은 메모리를 사용하여 바이너리 상태값을 저장하는데 많이 활용됨

```bash
# 비트맵 등록 (기본적으로 0으로 초기화 되어 있음)
$ SETBIT <key> <value> [ 0 / 1 ]

# 해당 키에 1로 저장된 값들의 수
$ BITCOUNT <key> 

# key1, key2 모두 1로 저장된 값 추출
# 결과값이 바로 출력되는 것이 아닌 결과값 작명 비트맵에 저장됨
$ BITOP [ AND | OR | XOR ] <결과값 작명 비트맵>
	<key1> <key2>

# 결과값 확인
$ GETBIT <결과값 작명> <>
```

​    

#### Bitmaps 활용

- `Online Status`
  - 사용자의 현재 상태를 표시하는 기능
  - 실시간성을 완벽히 보장하지는 않고, 수시로 변경되는 값임

​    

### HyperLogLog

- 집합의 카디널리티를 추정할 수 있는 확률형 자료구조
- 결과값이 실제와 오차가 발생할 수 있음
- 정확성을 일부 포기하는 대신에 저장공간(메모리)을 효율적으로 사용함 (평균 에러 0.81%)
- Member의 값을 해싱하여 Bucket이라는 단위로 분류하여 해시값에 맞게 표시함
- 동일한 아이템이 추가된 경우 동일한 해시를 갖기 때문에 카디널리티를 일정하게 계산할 수 있음
- 해시 충돌이 발생하는 경우 정확하지 않은 카디널리티를 반환할 수 있음
- 실제 값을 저장하지 않아서 모든 아이템을 다시 출력해야하는 상황에서는 활용할 수 없음

```bash
# HyperLogLog에 값 추가
$ PFADD <key> <value1> <value2> <value3> <value4> ...

# key의 카디널리티 출력
$ PFCOUNT <key>
```

​    

#### HyperLogLog 활용

- 방문자수 추정
  - 방문자수를 대략적으로 추정하는 경우
  - 정확한 횟수를 셀 필요없이 대략적인 어림치만 알고자 하는 경우

​    

### BloomFilter

- 요소가 집합 안에 포함되어있는지 확인할 수 있는 확률형 자료구조
- mebership test라는 기능을 구현할 때 자주 사용됨
- 정확성을 일부 포기하는 대신 저장공간을 효율적으로 사용
- 값이 집합에 포함되지 않는다는 사실은 정확하게 확인할 수 있지만, 집합에 포함되지 않는 값이 존재한다고 잘못 말하는 `false positive`를 반환하는 경우가 있음
- 값을 해싱하여 여러개의 해시키를 만듦

```bash
# 집합에 아이템 추가
$ BF.ADD <key> <value>

# 집합에 여러 아이템 한번에 추가
$ BF.MADD <key> <value1> <value2>

# 아이템이 집합에 포함되어있는지 여부 확인
$ BF.EXISTS <key> <value>
```

​    

#### BloomFilter 활용

- 중복이벤트 제거 (Unique Events)
  - 동일한 요청이 중복으로 처리되지 않기 위해 빠르게 해당 아이템이 중복인지 확인하는 방법

​    

---

## 3️⃣ 특수명령어

### 데이터 만료 (Expiration)

- 데이터를 특정시간 이후에 만료시키는 기능
- 데이터 조회 요청시에 만료된 데이터는 조회되지 않음
- 데이터가 만료되자마자 삭제하지 않고, 만료로 표시했다가 백그라운드에서 주기적으로 삭제

> TTL 

- Time To Live
- 데이터가 유효한 시간
- 초단위 (s)
- `-1` 은 데이터 만료가 설정 되어있지 않음을 의미
- `-2`는 데이터 TTL이 만료되었다는 의미, 잠시뒤에 다시 조회해보면 `(nil)`을 반환함

```bash
# 데이터 만료
$ EXPIRE <key> <value>

# 만료시간 확인
$ TTL <key>

# 데이터 저장시 만료시간도 같이 적용
$ SETEX <key> <TTL> <value>
```



### NX/XX

- NX : 해당 key가 존재하지 않는 경우에만 SET 적용
- XX : 해당 key가 이미 존재하는 경우에만 SET 적용
- SET이 동작하지 않은 경우 `(nil)`을 응답함

```bash
$ SET <key> <value> NX
$ SET <key> <value> XX
```

​    

### Pub/Sub

- 시스템 사이에 메시지를 통신하는 패턴중 하나
- Publisher와 Subscriber가 서로 알지 못해도 통신이 가능하도록 Decoupling된 패턴
- Pub/Sub의 장점은 두 시스템간의 강한 커플링을 줄일 수 있다는 것
- Publisher는 Subscriber에게 직접 메시지를 보내지 않고, Channel에 Publish
- Subscriber는 관심이 있는 Channel만 구독하여 메시지를 수신
- Subscriber의 기능이 변경되어도 Publisher는 이를 신경쓰지 않아도 됨
- 발행된 메시지가 보관되는 Stream과 달리 Pub/Sub은 Fire And Forget 메커니즘이 적용되어 있어 구독 전에 이미 발행된 메시지는 다시 수신할 수 없음



### Pipeline

- 다수의 Redis 명령어를 한번에 요청하여 네트워크 성능을 향상시키는 기술
- Round-Trip Times를 최소화함
- 대부분의 레디스 클라이언트 라이브러리에서 지원함

> Round-Trip Times : Request / Response 모델에서 발생하는 네트워크 지연 시간

​    

### Transaction

- 다수의 명령을 하나의 트랜잭션으로 처리하여 원자성을 보장해줌
- 중간에 에러가 발생하여도 모든 작업이 ROLLBACK됨
- 하나의 트랜잭션이 처리되는 동안에는 다른 클라이언트의 요청이 중간에 끼어들 수 없음

```bash
# 트랜잭션 시작
$ MULTI

# 트랜잭션 ROLLBACK
$ DISCARD

# 트랜잭션 COMMIT
$ EXEC
```

​    

---

## 4️⃣ 사용시 주의사항

### O(n) 명령어

- 대부분의 명령어는 O(1) 시간복잡도를 갖지만, 일부 명령어는 O(n)을 가짐
- Redis는 Single Thread로 명령어를 순차적으로 처리하기 때문에, 오래 걸리는 O(n) 명령어 수행시, 전체적인 애플리케이션 성능이 저하될 수 있음
- 대표적인 O(n) 명령어
  1. KEYS
     - 지정된 패턴과 일치하는 모든 키 조회
     - Production 환경에서 절대 사용을 금지해야함
     - SCAN 명령어로 대체해야함
  2. SMEMBERS
     - Set의 모든 member를 반환
     - Set에 포함된 유니크한 값이 많을수록 (카디널리티가 높은 경우) 동작이 오래걸림
     - 하나의 set에 10,000개 이상의 아이템을 추가하지 않는게 좋음
     - 그 이상으로 추가해야한다면, set을 여러개로 나눠서 저장하는게 좋음
  3. HGETALL
     - Hash의 모든 field를 반환
  4. SORT
     - List, Set, ZSet의 아이템을 정렬하여 반환

​    

### Thundering Herd Problem

- 병렬 요청이 공유자원에 대해 접근할 때, 급격한 과부하가 발생하는 문제
- 캐시의 만료에 의해 수많은 요청이 한번에 DB를 조회하여 발생할 수 있음
- 별도의 프로세스에서 Cronjob을 통해 캐시를 주기적으로 최신화 시켜줘야함

​    

### Stale Cache Invaildation

- Cache Invaildation
  - 캐시의 유효성이 손실되었거나 변경되었을 때, 캐시를 변경하거나 삭제하는 기술

