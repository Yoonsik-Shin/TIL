# Git 정리 (8) 

​    

## 1️⃣ Git Rebase

- 깃이력 재작성

```bash
$ git switch feature
$ git rebase master
```

​    

### 1. 주의사항 

- 마스터 브랜치를 기준으로는 사용하면 안됨
- 다른 개발자들이 이미 가져간 커밋은 리베이스하면 안됨
- 이미 공유한 커밋은 리베이스 하면 안됨

​    

### 2. 충돌발생시

- 방법1 : rebase 이전으로 돌아가기

```bash
$ git rebase --abort
```

​     

- 방법2 : 충돌한 부분 해결 후 rebase 진행

```bash
# 충돌 해결한 후
$ git add .
$ git rebase --continue
```

​    

---

## 2️⃣ Interactive Rebasing

```bash
$ git rebase -i HEAD~돌아가고싶은커밋수
```

- 자신이 있는 브랜치를 기준으로 진행됨
- 변경된 커밋이후의 커밋들은 모두 재설정됨

​    

> 예시

![image-20221010223332577](Git(8).assets/image-20221010223332577.png)

![image-20221010223407618](Git(8).assets/image-20221010223407618.png)

![image-20221010223501178](Git(8).assets/image-20221010223501178.png)

![image-20221010223522773](Git(8).assets/image-20221010223522773.png)

​    

### 주요 옵션 

- pick (default) : 커밋 그대로 유지
- reword : 커밋 메시지 재설정
- fixup : 커밋의 코드를 이전 커밋에 병합하고 커밋 메시지만 제거
- drop : 커밋 자체를 제거
- edit : 해당 커밋의 내용 변경

​    

---

## 3️⃣ Git Tag

### 1. 조회

```bash
$ git tag  # 현 저장소에 있는 모든 태그 조회
$ git tag -l "v17*" # 값이 포함된 모든 태그 조회 (와일드카드 가능)
```

​    

> [Semeantic versioning](https://semver.org/) : 버전 번호를 매기는 일종의 규칙

1. 패치 

- 작은 업데이트, 
- 신규기능이나 의미있는 변경사항 x, 
- 단순 버그 수정, 미미한 수정
- 패치를 배포하여도 사용자에게 영향 x

2. 마이너 릴리스

- 신기능이 추가됐을 때 (무조건은 아님)
- 마이너 릴리스를 배포하면 패치번호는 항상 0으로 초기화

3. 메이저 릴리스

- 하위 호환성이 보장되지 않을 때
- 기능 완전 삭제, 큰 변화
- 메이저 릴리스 배포시 나머지 번호 모두 0으로 초기화

​    

### 2. 비교

```bash
$ git diff tag1 tag2
$ git diff 1.0.2 1.1.3
```

​     

### 3. 생성

```bash
# 최근 커밋
$ git tag <tagname>
$ git tag 1.3.0

# 특정 커밋
$ git tag <tagname> <commit>    
$ git tag 2.1.3 685edq1
```

​    

### 4. 교체

- git은 태그 재사용을 지양
- 강제로 진행시켜야함

```bash
$ git tag <tagname> <commit> -f
```

​    

### 5. 삭제

```bash
$ git tag -d <tagname>
```

​    

### 6. 주석태그

- 태그에 주석을 남길 수 있음

```bash
$ git tag -a <tagname>   # 생성
$ git show <tagname>     # 주석보기
```

​    

### 7. tag 푸시

- 태그는 따로 푸시해줘야함

```bash
# 방법1 : 모든 태그 푸시
$ git push --tags

# 방법2 : 특정 태그 푸시
$ git push 원격이름 <tagname>
$ git push origin 1.3.2
```
