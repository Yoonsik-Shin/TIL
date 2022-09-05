# 마크다운 정리

​    

#### 마크다운이란?

: 텍스트 기반의 가벼운 마크업 언어

: 가능한 최소한의 문법으로 구조화

​    

##### - 마크다운 활용 예

: Github의 README.md

: 기술블로그

: Jupyter notebook

​    

### 마크다운 문법

#### 1. heading 

: 문서 제목이나 소제목에 사용

| HTML | Markdown                      |
| ---- | ----------------------------- |
| h1   | `# 문서 제목 or 소제목`       |
| h2   | `## 문서 제목 or 소제목`      |
| h3   | `### 문서 제목 or 소제목`     |
| h4   | `#### 문서 제목 or 소제목`    |
| h5   | `##### 문서 제목 or 소제목`   |
| h6   | `####### 문서 제목 or 소제목` |

⛔ 주의사항

> 1. #과 문자열사이에 띄어쓰기 필수!
> 2. 글자 크기를 조절하기 위해 사용되면 안됨

​    

#### 2. List

1. 순서가 있는 리스트

   `1.` 사용

2. 순서가 없는 리스트

​	`-` (hypen) or `*`  (asterisk) 사용

​    

#### 3. Fenced Code block

 ` ```언어``` ` (backtick) 사용

: 특정 언어를 명시하면 Syntax Highlighting 적용가능

```python
simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
	if lang in ['python', 'perl']:
		print("%6s need interpreter" % lang)
	elif lang in ['c', 'java']:
		print("%6s need compiler" % lang)
	else:
		print("should not reach here")
```

​    

#### 4. Inline Code block

` `` ` 활용

: 특정 문자열 하이라이트 적용가능

ex) `안녕하세요`

​    

#### 5. Link

`[문자열](url)` 활용

```markdown
[네이버](https://naver.com)
```

❗같은 폴더에 있는 파일 링크 

​	> `[ ](./파일명.확장자)`

​    

#### 6. Images

1. `![문자열](url)` 활용

2. 드래그 앤 드롭

   ![d1431b4dd5389c1651a3d02085f6b66bfedc315b5e7047a552a72b21a972885c4db0744372595ab14020d6baad8d7b573e234aaaa34ee950b49f6a4ba2af60b2258fb7f70260f57b68eae9b1814a0822fe8b0fb65d2625b21fea5aa05e34418d](markdown.assets/d1431b4dd5389c1651a3d02085f6b66bfedc315b5e7047a552a72b21a972885c4db0744372595ab14020d6baad8d7b573e234aaaa34ee950b49f6a4ba2af60b2258fb7f70260f57b68eae9b1814a0822fe8b0fb65d2625b21fea5aa05e34418d.png)

⛔ 주의사항

> 상대경로를 사용해야 업로드시 이미지 오류 안남

​    

#### 7. 인용문

`>` 활용

> 인용문 활용시

​    

#### 8. 표

- `본문 > 표` or `Cntl + t` 활용

  |      |      |
  | ---- | ---- |
  |      |      |

  ​    

#### 9. 텍스트 강조

> ctrl + b : 볼드체, ctrl + i : 이텔릭체

- 볼드체

  1. `**bold**` > **bold** (별표활용)
  2. `__bold__` > __bold__ (언더바활용)
- 기울림체

  1. `*italic*`  > *italic* (별표활용)
  2. `_italic_` > _italic_ (언더바활용)

​    


#### 10. 수평선

`***` or `___`  or `---` 사용

***





