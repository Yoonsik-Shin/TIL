# Git 정리 (8) 

​    

## Git Rebase

```bash
$ git switch feature
$ git rebase master
```

-  깃이력 재작성

​    

### 주의사항 ❗

- 마스터 브랜치를 기준으로는 사용하면 안됨
- 다른 개발자들이 이미 가져간 커밋은 리베이스하면 안됨
- 이미 공유한 커밋은 리베이스 하면 안됨



### 충돌발생시

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

## Interactive Rebasing

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



### 주요 옵션 

- pick (default) : 커밋 그대로 유지
- reword : 커밋 메시지 재설정
- fixup : 커밋의 코드를 이전 커밋에 병합하고 커밋 메시지만 제거
- drop : 커밋 자체를 제거
- edit : 해당 커밋의 내용 변경



