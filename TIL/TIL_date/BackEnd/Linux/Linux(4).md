# Linux (4)

​    

## 1️⃣ 권한

- 다중 사용자 
- 각 사용자는 개인별로 Home 디렉토리가 존재

![image-20230525012806755](Linux(4).assets/image-20230525012806755.png)

```bash
# 파일속성  ?? 파일소유자 그룹소유자 파일크기 날짜        파일명
drwxr-x---  7  yoonsik  yoonsik   4096    May 24 21:52 .
drwxr-xr-x  3  root     root      4096    Mar  6 15:53 ..
lrwxrwxrwx  1  yoonsik  yoonsik     23    Mar  9 14:59 .aws -> /mnt/c/Users/pocke/.aws
lrwxrwxrwx  1  yoonsik  yoonsik     25    Mar  9 14:59 .azure -> /mnt/c/Users/pocke/.azure
-rw-------  1  yoonsik  yoonsik   5864    May 24 21:51 .bash_history
-rw-r--r--  1  yoonsik  yoonsik    220    Mar  6 15:53 .bash_logout
-rw-r--r--  1  yoonsik  yoonsik   3771    Mar  6 15:53 .bashrc
```

​    

### 파일속성 (File Attributes)

![KakaoTalk_20230529_111520457](Linux(4).assets/KakaoTalk_20230529_111520457.jpg)

```bash
drwxr-x---
drwxr-xr-x
-rw-------
```

- 첫 글자는 __파일 유형__을 나타냄
- 디렉토리는 `d`로 시작, 파일은 `-`로 시작, 심볼릭 링크는 `l`로 시작
- 뒤 9글자는 각각 파일, 그룹, 모든사람의 읽기, 쓰기, 실행권한을 의미함
- 파일 속성 해석
  - `-` : 비활성화 상태
  - `r` : 읽기 권한 (Read)
  - `w`  : 쓰기 권한 (Write)
  - `x` : 실행 권한 (Execute)

​    

### chmod

- change mode
- 권한을 설정해주는 명령어

​    

#### 기호표기법

```bash
$ chmod 부여할권한 권한을수정할파일

$ chmod +x test.txt # 모든 권한 부여
$ chmod u+x test.txt # user에게 실행권한(x) 부여
$ chmod o-r test.txt # others에게 읽기권한(r) 박탈
```

- 부여받는 사용자
  - u : user 
  - g : group 
  - o : others 
  - a : all (u + g + o)
- 설정 방식
  - `+` : 권한부여
  - `-`: 권한박탈
  - `=` : 해당 권한을 제외한 나머지 권한박탈

​    

#### 팔진법

```bash
$ chmod 751 파일명
```

![KakaoTalk_20230529_113226684](Linux(4).assets/KakaoTalk_20230529_113226684.jpg)

- `r` : 4 
- `w` : 2 
- `x` : 1

​    

### su

- 대체 사용자의 커맨드 사용
- 현재 사용자를 로그아웃하지 않고도 다른 사용자의 커맨드를 이용할 수 있음

```bash
$ su 사용자명 # 현재 디렉토리를 변경하지 않음
$ su - 사용자명 # 사용자의 Home 디렉토리로 이동함
```

​    

### root user

- super user
- 모든 커맨드에 엑세스, 실행할 수 있고, 모든 파일에 엑세스 할 수 있음
- 일반 사용자가 할 수 없는 작업을 수행하는 특수계정(사용자)를 의미

   

#### sudo

- root 사용자로서 다른 커맨드를 실행할 수 있는 커맨드
- root 사용자의 비밀번호는 알 수 없지만, 커맨드를 실행 할 수 있는 권한은 부여되어 있음
- 첫 계정을 생성한 사용자의 경우 `sudo` 명령어를 사용할 수 있음

```bash
$ sudo -l
>> 비밀번호 요구
>> 로그인 후 15분 동안 비밀번호 요구없이 root명령어 사용가능
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

​    

#### addgroup

- 새로운 그룹만들기
- root 계정만 가능

```bash
$ sudo addgroup 그룹명
```

​    

#### adduser

- 그룹에 멤버 추가하기

```bash
$ sudo adduser 유저명 그룹명
```



----

## 2️⃣ 환경

### 변수

- 셀 변수(사용자가 정의)와 환경변수는 다름
- 따옴표를 꼭 써야하는 것은 아님
- 대소문자 구분 o

 ```bash
 $ printenv # 환경변수들을 보여줌
 $ printenv | less
 ```

- 변수 활용

```bash
$ $변수명 
```

- 쉘변수정의
- 해당 쉘 세션에서만 존재함

```bash
$ 변수명=변수값
```

- 환경변수 정의

```bash
$ export 환경변수명=환경변수
```

​    

### Startup FIles 

#### 로그인 세션 파일

1. `/etc/profile` 
   - 모든 사용자의 전역설정
2. `~/.bash_profile`
   - 개별사용자의 개인 설정파일
3. `~/.bash_login`
   - `.bash_profile`파일을 찾을 수 없을 때 읽음
4. `~/.profile`
   - `.bash_profile`, `~/.bash_login` 파일 둘 다 찾을 수 없을 때 사용함

​    

#### 비로그인 세션 파일

1. `/etc/bash.bashrc`
   - 모든 사용자의 전역설정
2. `~/.bashrc` 
   - 사용자의 홈 디렉토리에 존재
   - 해당 사용자만의 설정 저장

​    

### 프롬프트 변경

- PS1 변수 활용

```bash
$ printenv | grep PS1
```

- 쉘환경에서의 프롬프트 설정

```bash
$ PS1='커스텀프롬프트'
```

- 개인사용자만의 프롬프트 설정

```bash
# .bashrc 진입
$ vi .bashrc

# .bashrc 내용수정
export PS1=""

# .bashrc 실행
$ source .bashrc
```

​    

### 별칭

![image-20230529125121152](Linux(4).assets/image-20230529125121152.png)

- 쉘환경에서의 별칭 설정

```bash
$ alias 사용할별칭='명령어'
```

- 개인사용자만의 별칭 설정

```bash
# .bashrc 진입
$ vi .bashrc

# .bashrc 내용수정
alias 사용할별칭='명령어'

# .bashrc 실행
$ source .bashrc
```



> 별칭 별도 파일로 관리하기

- `.bash_aliases` 파일 활용
- `.bashrc` 파일에 `.bash_aliases` 파일 존재하면 이를 활용하도록 하는 명령어가 내장되어있음

![image-20230529130026214](Linux(4).assets/image-20230529130026214.png)

```bash
# 홈 디렉토리에 `.bash_aliases` 파일 생성
$ vi .bash_aliases

# .bash_aliases 파일에 커스텀 alias 작성
alias test="명령어"
```

   

---

## 3️⃣ bash script

### shebang 

- `#!/bin/bash`
- 파일이 실행파일인 것을 알려줌

```bash
# shebang
#!/bin/bash 

# 이글은 주석처리됩니다. 

# 명령어입력
echo "테스트입니다."
```

```bash
# 파일실행
$ bash 경로/파일명
```

> 파이썬으로 스크립트 실행하기

```bash
# shebang 설정
#!/usr/bin/python3
```

​    

### PATH변수

- 쉘이 실행가능한 프로그램을 찾기 위해 살펴보는 디렉토리 목록

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



####  PATH 추가

- `/.profile` 파일에 PATH에 __사용자의 개인저장소__를 포함하라는 명령어가 이미 정의되어 있음

```bash
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
```

- `bin` 폴더를 만들고, 실행만 시켜주면 됨

```bash
$ source .profile
# PATH에 'home/사용자/bin' 추가됨
```

>  위 명령어가 안될 경우, 수동으로 지정가능

```bash
# .bashrc 파일 열기
$ vi .bashrc
----------------------------
# .bashrc에 PATH 입력
PATH="$HOME/bin:$PATH"
----------------------------
# .bashrc 실행
$ source .bashrc
```

- 실행권한 부여

```bash
$ cd bin/
$ chmod +x 실행할파일
```

  

---

## 4️⃣ 크론 (Cron)

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
