# Linux (5)

​    

## 서버세팅

### 패키지매니저

#### yum

- Redhat 계열

```bash
$ yum install 
$ yum remove
$ yum update
$ yum search
$ yum list 
$ yum repolist
$ yum install epel-release -y # 많이 사용하는 repo들 다운로드
```

​    

#### dnf

- CentOS8 버전 이상에서만 사용가능

```bash
$ dnf install
$ dnf update
$ dnf info 
```

​    

####  apt-get

- Ubuntu에서 사용

```bash
$ apt-get install
```

​    

### nginx

- Redhat 9 버전

```bash
$ sudo yum module list nginx # 사용가능한 모듈 스트림 확인
$ sudo yum install nginx -y # 모듈 스트림이 있다면 설치진행
```

- 위 방법으로 설치가 안되면

```bash
$ vi /etc/yum.repos.d/nginx.repo # yum 외부저장소 추가
-----------------------------
# 위 파일에 해당 내용 추가 
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
-----------------------------

$ yum install nginx -y
```

- 설치된 nginx 확인 및 서비스 등록

```bash
$ nginx # nginx 실행
$ nginx -s stop # nginx 중지
$ nginx -s reload # nginx 재시작

$ ps -ef | grep nginx # nginx 프로세스 확인

# 시작프로그램에 등록/활성화/중지
$ systemctl start nginx
$ systemctl enable nginx
$ systemctl stop nginx
$ systemctl reload nginx
```

   

### [volta](https://volta.sh/)

```bash
$ curl https://get.volta.sh | bash
$ source .bash_profile
```

### Node

```bash
$ volta install node@버젼
```

### PM2

```bash
$ volta install pm2
```

### MySQL

- [url 사이트](https://dev.mysql.com/downloads/file/?id=518487)

```bash
$ yum localinstall https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-community-server-8.0.33-1.el7.x86_64.rpm
```

- [오류시 먼저 설치](https://dev.mysql.com/downloads/repo/yum/)

```bash
$ yum localinstall https://dev.mysql.com/get/mysql80-community-release-el7-7.noarch.rpm
```

- 설치된 mysql파일 확인

```bash
$ vi /etc/my.cnf
---------------------------------------------------------------------
# 해당파일에 아래내용 추가하고 원래 존재하던 [mysql] 주석처리
[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqldump]
default-character-set = utf8mb4

[mysqld]
skip-character-set-client-handshake
init_connect="SET collation_connection = utf8mb4_unicode_ci"
init_connect="SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci"

character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
---------------------------------------------------------------------
```

- 설치 확인

```bash
$ ps -ef | grep mysql
```

- 실행 / 중지

```bash
$ systemctl start mysqld
$ systemctl stop mysqld
```

- 비밀번호 설정

```bash
$ grep 'temporary password' /var/log/mysqld.log # 임시 패스워드 알아내기
$ /usr/bin/mysql_secure_installation # 임시 패스워드 입력하면 새로운 패스워드 설정하도록 해줌
```

- mysql 진입

```bash
$ mysql -u root -p
```

- mysql 다루기

```bash
$ show database; # DB 목록보기
$ CREATE DATABASE 새로생성할DB명; # DB 생성

# 계정 생성 및 권한부여
$ CREATE USER '유저명'@'IP주소(%:모든주소)' IDENTIFIED WITH mysql_native_password BY '비밀번호';
$ GRANT ALL PRIVILEGES ON DB명.테이블명 TO '유저명'@'IP주소(%:모든주소)' WITH GRANT OPTION;

# 비밀번호 변경
$ ALTER USER 유저명 IDENTIFIED WITH mysql_native_password BY '새비밀번호';

$ show variables like '%max_connection%'; # 커넥션수 보기
$ set global max_connections=100; # 커넥션수 제한하기
```

   

### Domain 설정

```bash
$ nslookup url
```



### HTTPS 설정

- certbot, [Let's Encrypt](https://letsencrypt.org/ko/) 활용

```bash
$ yum install certbot -y
$ systemctl stop nginx
$ certbot --standalone -d 도메인주소 certonly
```

- `fullchain.pem`, `privkey.pem`파일을 nginx에 등록해줘야함

```bash
$ vi conf.d/mydeal.conf

# 해당 파일에 아래내용 붙여넣기
----------------------------------------------------------------
server {
	listen 80;
	server_name mydeal.topician.com;

	location / {
        	root   /var/www/mydeal;
       	index  index.html;
        	try_files $uri /index.html;
        }

        return      301 https://$host$request_uri; ✔️✔️
}

server {
    listen 443 ssl http2;   ✔️✔️
    listen [::]:443 ssl http2;   ✔️✔️

    server_name mydeal.topician.com;

    ssl_certificate /etc/letsencrypt/live/도메인명/fullchain.pem;   ✔️✔️
    ssl_certificate_key /etc/letsencrypt/live/도메인명(mydeal.topician.com)/privkey.pem;   ✔️✔️

    location / {
        root   /var/www/mydeal;
        index  index.html;
        try_files $uri /index.html;
    }

}
----------------------------------------------------------------

# nginx 다시 켜기
$ systemctl start nginx
```

​    

#### 인증서 갱신

```bash
# 해당 명령어 입력시 자동으로 인증서 갱신
$ certbot renew 
```

​    

> 크론탭 설정하여 자동 시행

- nginx가 중지된 상태에서 설정해야함

```bash
$ crontab -e
-----------------------------------------------------------------------
0 5 1 */2 * /usr/bin/certbot renew >> /etc/nginx/cert.log 2>&1
-----------------------------------------------------------------------

# 오류나면 시도
0 5 1 */2 * /usr/bin/certbot renew --force-renew --pre-hook="/usr/bin/systemctl stop nginx" --post-hook="/usr/bin/systemctl start nginx" >> /etc/nginx/cert.log 2>&1
```

