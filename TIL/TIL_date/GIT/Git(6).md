# Git 정리 (6) 

​    

## 0️⃣ Remote Tracking Branch  (원격 추척 브랜치)

```bash
$ git branch -r  # 확인하기
```

### `origin/<브랜치명>`

- 깃허브 저장소의 브랜치의 가장 마지막 커밋을 가리킴

​    

---

## 1️⃣ Git fetch

![](Git(6).assets/fetch_pull.jpg)

```bash
$ git fetch origin
$ git fetch origin <브랜치명>
```

- 원격 브랜치에서 변경사항을 가져와 원격 추적 브랜치(origin/branch)를 업데이트함
- 이전의 작업파일과 통합되지않음 ✔️
- 체크아웃을 통해 `origin master`를 볼 수 있음

> 가서 깃허브에서 최신 정보를 가져와주는데, 현재 작업중인 것은 건들지 말아줘

​    

---

## 2️⃣ Git pull

![pull](Git(6).assets/pull.jpg)

```bash
$ git pull origin <브랜치명>
$ git pull
```

- 깃허브 저장소의 항목을 로컬 저장소로 가져옴
- HEAD 브랜치(워킹 디렉토리)를  업데이트함
- `git pull` = `git fetch` + `git merge`
- 병합 충돌이 발생할 수 있음

> [해결법](./Git(3).md)
