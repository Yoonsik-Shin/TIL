# 	👍오늘 배운것 (22.07.05(화))

1. [마크다운](./markdown.md)

2. Git

   

---



- CLI (Command Line Interface) : 명령 기반 인터페이스

- GUI (Graphic User Interface) : 그래픽 기반 인터페이스

  

---



✅ 기본적인 디렉토리 관리

1. `pwd` : 현재 디렉토리 출력

2. `cd 디렉토리명` : 디렉토리 변경

   ​	- `cd ..` : 상위 디렉토리로 이동 (❗띄어쓰기 중요)

   ​	- `cd (파일명 첫글자) `+ TAB => 파일명 전체를 찾아줌

3.  `ls` : 현재 디렉토리의 목록

4.  `mkdir 디렉토리명` : 디렉토리 생성

5.  `rm -r 디렉토리명`  or `rmdir 디렉토리명`: 디렉토리 삭제 ()

6. `touch 파일명.확장자` : 파일 생성

7. `rm 파일명.확장자` : 파일 삭제

   

> bash창 정리 : `ctrl + l` or `clear`  



---



### #️⃣ Git

: 분산 버전 관리시스템 (DVCS)

> 버전 : 컴퓨터 SW의 특정 상태



#### 1. git 기본흐름

- 작업 > add하여 Staging area에 모음 > commit으로 버전 기록 

![KakaoTalk_20220706_110959410](TIL (22.07.05).assets/KakaoTalk_20220706_110959410.jpg)



1. 저장소 처음 만들때

   ```bash
   $ git init # 특정 폴더를 repository(깃 저장소)로 만들어 git으로 관리
   ```

   - `.git` 폴더 생성 (숨겨진 폴더)

   - `(master)` 표기 생성 

     

   ⛔ 주의사항

   > 폴더를 잘못 지정했을 경우 
   >
   > 1. 직접 `.git` 파일 삭제 
   > 2. `rm -rf .git` 명령어 사용

   

2.  버전을 기록할 떄

   ```bash
   # 첫번째
   $ git add 파일명 # working directory 변경사항 staging area에 추가
   ```

   ```bash
   # 두번째
   $ git commit -m '커밋메시지' # staged 상태의 파일을 버전으로 기록
   ```
   
   
   
3.  상태를 확인할 때


![KakaoTalk_20220706_111804542](TIL (22.07.05).assets/KakaoTalk_20220706_111804542.jpg)

​	

- `$ git status `:  파일의 상태 확인

```bash
# a.txt 파일 만든 직후 > 빨간글씨 (untracked, modified)

$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working directory)
# => 한번도 git으로 관리되고 있지 않은 파일!
Untracked files:
# git add 사용해봐...
# 포함시키기 위해서 / 커밋이 될 것 => 2통에 넣으려면
  (use "git add <file>..." to include in what will be committed)
        a.txt

# 커밋할 것은 없어 => 2통이 비어있어
# 하지만(but) 트래킹되지 않은 파일은 존재한다. 
# (git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

```bash
# b.txt 파일을 만들고 add한 이후 > 초록글씨 (staged)

$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
  		# 새로운 파일: b.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt
```

````bash
# a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋까지

$ git status
On branch master
# 2통, 1통 모두 클린~!
nothing to commit, working tree clean
````



- `$ git log` : 기록된 커밋 조회

```bash
$ git log -1 # 가장 최근에 커밋된 로그 조회

$ git log --oneline # 간단히 한줄로 조회

$ git log -1 --oneline # 가장 최근 간단히 한줄로
```



> 파일 라이프사이클

![KakaoTalk_20220706_114334903](TIL (22.07.05).assets/KakaoTalk_20220706_114334903.jpg)

- Tracked : 이전부터 버전으로 관리되고 있는 파일
  - modified : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
  - staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소) 
  - committed : 커밋이 된 상태

- Untracked : 버전으로 관리된 적 없는 파일 (파일 새로 만든 경우)



---



#### 2. Git 설정

- 사용자 정보 : 커밋하기 위해 반드시 필요

  ```bash
  $ git config --global user.name '유저이름'
  $ git config --global user.email 'abc123@gmail.com'
  
  # 확인
  $ git config --global --list
  ```
  
  
  
  











