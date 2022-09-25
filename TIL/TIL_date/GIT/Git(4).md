# Git 정리 (4)

## 1️⃣ Git diff

![image-20220924225709473](Git(4).assets/image-20220924225709473.png)

### 1. Git diff

- 다음 커밋을 위해 스테이지에 등록되지 않은 워킹 디렉토리의 모든 변경사항을 나열 (🔴)
- 워킹 디렉토리와 스테이지 영역 간의 변경 사항 비교

```bash
$ git diff
```

- Git diff 결과해석

```bash
dif --git a/파일명 b/파일명
index 7egas34..53gasd 103452   # 중요도 낮음 (메타데이터 해시값, 내부 파일 모드 식별자)
--- a/파일명
+++ b/파일명
@@ -3, 4 +3, 5 @@    # @@ a파일 3번쨰줄부터 4줄까지 b파일 3번째줄부터 5번째줄까지 @@ / ❗부호는 파일 구분용
# 수정된 부분의 주변을 보여줌
yellow
green
blue
-purple
+indigo
+violet
```

​    

### 2. Git diff HEAD

- 스테이지 등록 여부와 상관없이 마지막으로 실행된 커밋이후 워킹 디렉토리에 있는 새로운 변경사항을 보여줌

```bash
$ git diff HEAD
```

​    

> `git diff` VS `git diff HEAD`

| git diff                    | git diff HEAD                             |
| --------------------------- | ----------------------------------------- |
| 등록되지 않은 모든 변경사항 | 마지막 커밋이 실행된 이후의 모든 변경사항 |

​    

### 3. Git diff --staged / git diff --cached

- 같은 기능을 하나 명령어만 다른 것
- 스테이지에 등록된 변경사항만 보여줌 (🟢)

```bash
$ git diff --staged
$ git diff --cached
```

​    

> 특정 파일로 범위 줄이기

```bash
$ git diff HEAD 파일명
$ git diff --staged 파일명
```

​    

### 4. 브랜치끼리 비교하기

- 순서 중요
- 비교하려는 브랜치들 사이에 `..` 사용 or 공백 2칸 사용

```bash
$ git diff 브랜치1..브랜치2
$ git diff 브랜치1  브랜치2 
```

​    

### 5. 커밋끼리 비교

- 순서 중요
- 비교하려는 브랜치들 사이에 `..` 사용 or 공백 2칸 사용

```bash
$ git diff commit1의 해시값..commit2의 해시값
$ git diff commit1의 해시값  commit2의 해시값
```

​    

---

## 2️⃣ Git stash

- 작업중인 브랜치에서 다른 브랜치로 이동할 때 작업중인 브랜치를 커밋하지않고 임시저장하여 다른 브랜치로 이동하여도 영향을 끼치지 않게 하는데 사용됨

​     

### 1. Git stash

![stash](Git(4).assets/stash.jpg)

- 커밋하지 않은 변경사항들을 임시 저장
- 불필요한 커밋으로 이력이 지저분해지는 일 없이 나중에 돌아올 수 있게 해줌

```bash
$ git stash
```

​    

### 2. Git stash pop

- 스태시로 임시저장했던 내용들을 불러오고 스태시를 비움

```bash
$ git stash pop
```

​    

### 3. Git stash apply

- 스태시에 임시저장했던 내용을 불러오지만 임시저장내용을 삭제하지 않고 스태시에 남겨둠 

```bash
$ git stash apply
```

​    

### 4. Git stash list

- 스태시한 내역을 보여줌

```bash
$ git stash list
```

```bash
# 불러오기
$ git stash apply stash@{2}
```

​    

### 5. Git stash drop

- 지정한 일부 스태시 내역을 삭제

```bash
$ git stash drop stash@{2}
```

​    

### 6. Git stash clear

- 모든 스태시 지우기

```bash
$ git stash clear
```

