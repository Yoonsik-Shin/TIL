# Git 정리 (9)

​    

## 1️⃣ Git Reflog

- reference log (참조기록)
- Git이 헤드 참조 기록의 이동 추적
- 지역적으로 자신의 컴퓨터의 참조목록에 대해서만 기록
- 영구적으로 보관되는 것이 아님, 만료기간 존재

```bash
$ git reflog show HEAD
$ git reflog show <branch>
```



> Reflog References

```bash
name@{qualifier}
HEAD@{2}
```

 ```bash
 # 응용 (Timed References)
 $ git reflog show HEAD@{2.days.ago}
 $ git reflog show HEAD@{two.days.ago}
 $ git reflog show HEAD@{one.minute.ago}
 ```



### 사라진 커밋 복구

```bash
# 삭제된 커밋 찾기
$ git reflog show HEAD
$ git checkout <commit-hash>

$ git reset --hard <commit-hash>    # 1번 방법
$ git reset --hard name@{qualifier} # 2번 방법
```

​    

---

## 2️⃣ Git Alias

1. `.gitconfig` 파일에서 작성

```bash
[alias]
	s = status
	l = log
```

```bash
$ git s
$ git l
```

​    

2. 터미널에서 작성

```bash
git config --global alias.status s
git config --global alias.log l
```

​    

> Global Git Config (전역적 깃 설정파일)

- 모든 저장소에 걸쳐 적용할 수 있는 설정을 구성할 수 있는 곳
- `.gitconfig`