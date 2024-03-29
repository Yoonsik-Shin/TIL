

# CSS정리 (1)

​    

## 0️⃣ CSS란?

- 스타일을 지정하기 위한 언어
- ❗CSS는 `;` 세미콜론이 무조건 필요❗

``` css
Selector(선택자) {
  property(속성): Value(값);  /* Declaration (선언) */ 
}
```

> CSS 주석처리 

```css
/* 주석처리할 내용 */
```

​    

---

## 1️⃣ CSS 적용방법

1. 직접 적용 (활용도 낮음)

```html
<h1 style="color:blueviolet">Hello World</h1>
```

2. CSS 정의 (활용도 낮음)

- <head>안에 정의

```html
<head>
  <style>
  	h2 {
    	color: palegoldenrod
  	}
</style>
</head>
```

3. 외부스타일 시트 활용 (❗활용도 높음❗)

- 파일명.css

- <head>안에 정의

```html
<head>
  <link rel="stylesheet" href="파일명.css">
</head>
❗href링크 형식이 파이썬과 다름
```

​    

---

## 2️⃣ 텍스트 설정

### 1. 색상 설정 

- 적용방법
  - color : 텍스트색상
  - background-color: 배경색상
- 색상 지정
  1. 색상 키워드 [`color: red;`]
  2. RGB 색상 [`color: rgb(0, 255, 0);`]
  3. 헥스 컬러 코드
     - 16진법 사용
     - `#ffff00`  #(red,red)(green,green)(blue,blue)
  4. HSL 색상 [`color: hsl(120, 100%, 0);`]

> [COOLORS](https://coolors.co/palettes/trending) : 트렌디한 색 조합 알려주는 사이트

### 2. 기타 설정

```css
text-align: center / left / right;       /* 정렬 */
font-weight: 400(normal), 700(bold);     /* 굵기 */
text-decoration: 속성(underline);        /* 데코레이션 */
text-decoration: none;
line-height: ;                          /* 줄간격 */
letter-spacing: ;                       /* 자간 */
word-spacing :                          /* 단어간 */
font-size: ;                            /* 글 크기 */
font-family: 1순위폰트, 백업폰트1, ..;    /* 글 폰트변경 */
text-transform: uppercase;              /* 모든 글자 대문자로 변경 */
```

> [운영체제별 폰트 점유율](cssfontstack.com)

​    

---

## 3️⃣ 선택자

> [CSS 선택자 게임](https://flukeout.github.io/)
>
> ![image-20220907015540922](CSS_1.assets/image-20220907015540922.png)

### 1. 전체 선택자 (Universal Selector)

- 모든 값에 적용 (활용도 낮음)

```css
* { }
```

### 2. 요소 선택자 (Element Selector)

- 해당 모든 요소에 적용 (활용도 낮음)

```css
h1, h2 { }
```

### 3. ID 선택자 

- ID는 페이지 내에서 한번만 사용되어야함 (고유식별자)

```html
<p id="signup"></p>
```

```css
#signup { }
```

### 4. 클래스 선택자 

```html
<p class="this"></p>
```

```css
.this { }
```

### 5. 자손선택자 (Desencdant Selector)

> ❗선택자 문법 중에 공백 == ~안에 있는 모든 자식

```css
/* post클래스속에 있는 a태그(자손) */
.post a { }
```

### 6. 인접선택자 (Adjacent Selector)  = 결합자 (combinator) [`+`]

```css
/* h2태그 바로뒤에 있는 button */
h2 + button { }
```

### 7. 일반 형제 결합자 (General Sibling selector) [`~`]

```css
/* 서로 형제인 문단 중 이미지 뒤쪽인 경우에만 선택 */
img ~ p { }
```

### 8.  직계자손선택자 (Direct Child Selector) [`>`]

- 자주 안씀
- 직계만
- 필요할때가 있긴함

```css
/* div안에 첫번째 li만 선택 */
div>li { }
```

### 9. 속성선택자 (Attribute Selector)

- 자주 안쓰임

```css
input[type="속성(text, password)"]{ }

section[class="post"]{ }
```

- 응용

```css
/* href속성에 example이 포함된 모든 앵커 태그 */
a[href*="example"]{ }

/* .org로 끝나는 href */
a[href$=".org"]{ }

/* O를 포함하는 속성 */
태그[for*="o"]{ }
```

> ⛔!importance⛔ : CSS 최우선 적용, 다른 모든 규칙 무시, 사용시 주의해야함

​    

---

## 4️⃣ 가상클래스 (Pseudo Class)

1. `hover`
   - 마우스를 위로 가져갔을 때 동작

```css
button:hover{
  ;
}
```

2. `active`
   - 클릭한 순간부터 떼는 시점까지

```css
button:active{
	;  
}
```

3. `link` / `visitied`

```css
a:link{
  color:blue;
}
a:visited{
  color:red;
}
```

3. `nth-of-type(n)`
   - 부모 요소의 __특정 자식__ 요소중 n번쨰
   - n은 `An + B`값 가질 수 있음

```css
p:nth-of-type(3){    /* p태그중에서 3번째 */
    color:blue;
}
```

4. `nth-of-child(n)`
   - 부모 요소의 __모든 자식__ 요소중 n번째

```css
p:nth-child(5){   /* p태그의 부모요소의 모든 자식 요소중 5번째 */
    color:red;
}
```

3. first-child
4. only-child
5. last-child
6. nth-last-child()
7. first-of-type
8. only-of-type
9. last-of-type
10. empty

​    

---

## 5️⃣ 가상요소 (Pseudo Elements)

```css
/* 첫 글자 지정 */
h2::first-letter{
	;
}
```

```css
/* 첫 문장 지정 */
p::first-line {
  ;
}
```

```css
/* p태그의 드래그한 부분 처리 */
p::selection {
  ;
}
```

​     

---

​    

> CASCADE

- 적용된 스타일의 우선순위
- 같은 선택자일때 : 가장 나중에 정의된 스타일 반영

​    

## 6️⃣ Specificity (특이도)

- 충돌이 생길 경우 브라우저에서 규칙을 적용하는 방법 

```markdown
❗!important❗ >>>>>>>>>>>>>>>>>>>>>>> 모두 무시하고 적용됨
(0순위) 인라인 스타일 >> 
(1순위) ID 선택자 >> 
(2순위) 클래스 선택자 >> 
(3순위) 요소 선택자
```

- 특이도 계산공식
  - 10진수 계산아님
  - 금 은 동 순위처럼 작용, 

| 100의 자리수 | 10의 자리수   | 1의 자리수       |
| ------------ | ------------- | ---------------- |
| ID 선택자    | 클래스 선택자 | 요소             |
|              | 속성값        | 가상 요소 선택자 |
|              | 가상 클래스   |                  |

```css
/* 예시 */
section p {
  color: teal;
}
>> 0 0 2 [2점]

#submit {
  color: olive;
} 
>> 1 0 0 [100점]

nav a.active {
  color: orange;
}
>> 0 1 2 [12점]
```

> [특이도 계산기](https://specificity.keegan.st/)

