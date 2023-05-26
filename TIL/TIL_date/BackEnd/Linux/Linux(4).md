# Linux (4)

​    

## 권한

- 다중 사용자 
- 각 사용자는 개인별로 Home 디렉토리가 존재



![image-20230525012806755](Linux(4).assets/image-20230525012806755.png)

파일소유자 그룹소유

파일속성 (File Attributes)

- 읽기, 쓰기, 실행권한

```bash
drwxr-x--- 7 yoonsik yoonsik  4096 May 24 21:52 .
drwxr-xr-x 3 root    root     4096 Mar  6 15:53 ..
lrwxrwxrwx 1 yoonsik yoonsik    23 Mar  9 14:59 .aws -> /mnt/c/Users/pocke/.aws
lrwxrwxrwx 1 yoonsik yoonsik    25 Mar  9 14:59 .azure -> /mnt/c/Users/pocke/.azure
-rw------- 1 yoonsik yoonsik  5864 May 24 21:51 .bash_history
-rw-r--r-- 1 yoonsik yoonsik   220 Mar  6 15:53 .bash_logout
-rw-r--r-- 1 yoonsik yoonsik  3771 Mar  6 15:53 .bashrc
```

- 첫 글자는 파일 유형을 나타냄
- 디렉토리는 `d`로 시작, 파일은 `-`로 시작, 심볼릭 링크는 `l`로 시작

뒤 9글자

| 파일소유자 (Owner) | 그룹소유자 (Group) | 모든사람 (World) |
| ------------------ | ------------------ | ---------------- |
| rwx                | rwx                | rwx              |



Read : 읽기 권한 r

Write : 쓰기 권한 w

Execute : 실행 권한 x



### chmod

- change mode

```bash
$ chmod 부여할권한 권한을수정할파일
```

방법1

u : user 

g : group 

o : others 

a : all (u + g + o)

`+` : 권한부여

`-`: 권한박탈

`=` : 해당 권한을 제외한 나머지 권한박탈



방법2 : 팔진법

```bash
chmod 777 파일명
```



### su

- 대체 사용자의 커맨드 사용

```bash
$ su 사용자명 # 현재 디렉토리를 변경하지 않음
$ su - 사용자명 # 사용자의 Home 디렉토리로 이동함
```



root user

sudo  



sudo

```bash
$ sudo -l
>> 비밀번호 요구
>> 로그인 후 15분 동안 root명령어 사용가능
```



### chown

- 오너쉽 변경
- 파일, 디렉토리의 소유자나 그룹 소유자를 변경할 수 있는 방법

```bash
$ chown 유저명 파일명  # 소유자만 변경
$ chown :그룹명 파일명  # 그룹소유자만 변경
$ chown 유저명:그룹명 파일명 # 둘다 변경
```

- 자신이 파일을 소유하고 있어도 소유자를 바꿀 수 없음
- root 사용자만이 소유자를 변경할 수 있음 



### groups

- 유저가 속한 그룹을 보여줌
- 그룹이 할당되었을 때 실행중인 세션을 로그아웃한 후 다시 로그인 해줘야 반영됨

```bash
$ groups 유저명
```

### addgroup

- 새로운 그룹만들기
- root 계정만 가능

```bash
$ sudo addgroup 그룹명
```

### adduser

- 그룹에 멤버 추가하기

```bash
$ sudo adduser 유저명 그룹명
```



----

## 환경

- 셀 변수(사용자가 정의)와 환경변수는 다름
- 따옴표를 꼭 써야하는 것은 아님

 ```bash
 $ printenv # 환경변수들을 보여줌
 $ printenv | less
 ```

- 변수 활용

```bash
$ $변수명 
```

- 쉘변수정의

```bash
$ 변수명=변수값
```

- 환경변수 정의

```bash
$ export 환경변수명=환경변수
```

​    

PS1 변수 : 프롬프트 변경

Startup Files

---

## bash script

### shebang 

- `#!/bin/bash`
- 파일이 실행파일인 것을 알려줌

```bash
#!/bin/bash
# 이글은 주석처리됩니다. 

# 명령어입력
echo "테스트입니다."
```

```bash
# 파일실행
$ bash 경로/파일명
```

​    

### PATH변수

```bash
$ printenv | grep PATH
# or
$ echo $PATH
```

- 해당 경로들을 돌면서 명령어의 위치를 찾아냄

```bash
$ which ls # 실행파일이 어디있는지 알려줌
>> /usr/bin/ls

$ which adduser
>> /usr/sbin/adduser
```

![image-20230526154940760](Linux(4).assets/image-20230526154940760.png)

   

---

## 크론 (Cron)

- 특정 간격이나 시간에 실행되도록 커맨드를 예약하는데 사용하는 서비스 
- 모든 사용자는 자신의 작업을 예약하고 cronjob을 설정할 수 있는 자체테이블을 가지고 있음

```bash
# crontab 파일열기
$ crontab -e
```

​    

### 구문

```bash
# crontab 설정파일
a b c d e 명령어
```

|      |                        |                                                         |
| ---- | ---------------------- | ------------------------------------------------------- |
| a    | 분 (Min)               | 0 ~ 59분                                                |
| b    | 시 (Hour)              | 0 ~ 23시                                                |
| c    | 일 (Day)               | 1 ~ 31일                                                |
| d    | 월 (Month)             | 1 ~ 12월                                                |
| e    | 요일 (Day of the week) | 0 : 일요일<br />1 : 월<br />2 : 화<br />...<br />6 : 토 |

- `*` : 모든값

```bash
* 10 * * * 명령어 # 매일 10시마다 명령어 실행
30 * 1 1 * 명령어 # 1월 1일에 30분 마다 명령어 실행
```

- `,` : 선택 

```bash
30 * 1 1,2,3 * 명령어 # 1월 1일, 2월 1일, 3월 1일 매시간 30분마다 명령어 실행
```

- `-` : 범위

```bash
10 10 * * 1-5 명령어 # 매주 월요일~금요일 10시 10분에 명령어 실행
```

- `*/n` : 단계값 (n)

```bash
*/5 * * * * # 매일 5분마다 명령어 실행
```

> 구문 확인할 수 있는 페이지 : https://crontab.guru/

​    

### 오류다루기

- 표준오류 리다이렉팅

```bash
# crontab 설정파일
* * * * * 잘못된명령어 >> ~/로그파일 2>&1
```

​    

### 파일 백업하기

```bash
# 백업실행파일 (want_backup)
#!/bin/bash
DATE=$(date +%m-%d-%Y-%M)
BACKUP_DIR="home/사용자/backups"

tar -cvzf $BACKUP_DIR/backup_$DATE.tar.gz /home/사용자/Desktop
```

```bash
$ chmod +x 백업실행파일명
$ crontab -e
```

```bash
# cronjob 설정
0 */3 * * * /home/사용자/bin/백업실행파일명 # 3시간마다 실행
```

​    

>  파일압축 (`tar`)

- `tar -cvzf 파일위치/파일명 압축할파일` : 파일압축하기
- `tar -xvzf 파일명`  : 파일압축해제
