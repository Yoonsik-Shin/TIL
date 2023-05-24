# Vim

​    

```bash
:w  # 저장
:q  # 종료
:wq  # 저장하고 종료
:wq! # 저장하고 강제로 종료

# '!'는 강제로 실행해주는 명령어
```



커서이동

```bash
# 방향키로도 가능
-----------------------------------------------------
h  # 왼쪽
j  # 아래로
k  # 위로
l  # 오른쪽
-----------------------------------------------------
3h  # 왼쪽으로 3칸이동
4j  # 아래로 4칸이동
-----------------------------------------------------
w  # 단어단위 (정방향)
b  # 단어단위 (역방향)
e  # 단어단위 (단어끝부분)
-----------------------------------------------------
W  # 공백단위 (정방향)
B  # 공백단위 (정방향)
E  # 공백단위 (단어끝부분)
-----------------------------------------------------
# 문장단위 
0  # 행의 맨앞
$  # 문장의 마지막으로 이동
^  # 공백을 제외한 첫번째 글자

f'찾을문자'
fB  # 문장에서 B가 들어간 첫단어로 이동
FB  # 문장에서 B가 들어간 마지막 단어로 이동

t'찾을문자' # 내가 찾고있는 문자 바로 앞으로 커서이동
ta  # 문장에서 B가 들어간 첫 단어 바로 앞으로 커서이동
Ta  # 문장에서 B가 들어간 마지막 단어 바로 앞으로 커서이동

# 찾은 상태에서 `;`을 누르면 계속 같은 명령어 수행 (정방향)
# 찾은 상태에서 `,`을 누르면 계속 같은 명령어 수행 (역방향)
```



단어검색

```bash
/검색할단어
enter

n 다음단어로 포커싱 이동
N 역방향으로 포커싱 이동

* # 검색하고싶은 단어 위에서 사용시 하이라이트후 다음 단어로 이동
# #  검색하고싶은 단어 위에서 사용시 하이라이트후 마지막 단어로 이동 (방향전환됨)
```



화면스크롤

```bash
ctrl + e  # 한줄씩 아래로 스크롤
ctrl + y  # 한줄씩 위로 스크롤

ctrl + u  # 반페이지씩 위로 스크롤
ctrl + d  # 반페이지씩 아래로 스크롤

gg # 문서의 첫행으로 이동
G  # 문서의 마지막행으로 이동
:10  # 특정행으로 이동하고 싶을때 (예시: 10행으로 이동)
```

​    

vim mode

입력모드

a : 현재 커서 뒤

A : 그 줄의 가장 마지막 칸으로 이동

i : 현재 커서 앞

I 그 줄의 가장 첫글자 앞으로 이동

o : 밑으로 한 줄

O : 위로 한줄 추가

r : replace 



일반모드

삭제는 잘라내기 형태로 저장됨

x : 한글자 삭제

dd : 한 문장 삭제

D : 현재위치부터 끝까지 삭제

J : 아랫줄내용을 윗줄로 공백하나 차이로 붙여줌

p : 윗줄에 붙여넣기

P : 아랫줄에 붙여넣기

yy : 한줄 복사



되돌리기

u : 실행취소

ctrl + r : 다시 실행

. : 방금 실행한 행동 재실행



esc  === ctrl + [

backspace === ctrl + h



비주얼모드

선택, 복사, 삭제

v : 한 글자 선택

V : 행 단위로 선택

ctrl + v : 열 단위로 선택



단어선택

v + i + w : 커서가 위치해 있는 단어 선택

v + i + ( : 소괄호안에 있는 단어 선택

v + i + ' : 작은 따옴표 안에 있는 단어 선택

y + i + w : 비주얼모드를 사용하지 않고 커서가 위치한 단어를 복사

c + i + w : 단어를 삭제함과 동시에 입력모드로 전환



단어바꾸기

:%s/내가바꿀단어/어떻게바꿀지/c : 마지막 플래그가 c이면 한 개씩 물어봄

:%s/내가바꿀단어/어떻게바꿀지/g : 마지막 플래그가 g이면 한꺼번에 다 바꿈



창 분할하기

:vs

:sp 

ctrl + w + 방향키 : 창끼리 이동

:q  : 분할된 창끄기

:enew : 빈창 생성



파일다루기

:E : 다른 파일열기 (기존파일은 계속존재)

:bn : 다음 버퍼로 이동

:bp : 이전 버퍼로 이동

:b번호 : 해당 번호를 가진 버퍼로 이동

:bd : 버퍼닫기



작업자동화

q등록할키 : 키 매크로 등록 시작

q : 매크로 등록 종료

@등록한키 : 키 매크로 실행

@@ : 이전 작업 반복

반복할숫자 + @@ : 숫자만큼 매크로 반복



vimrc 설정

_vimrc 파일 : vim에디터 환경설정파일





https://vim-adventures.com/