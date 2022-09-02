# CSS 정리_2



## 1️⃣ 박스모델

- width : 너비
- height : 높이



### 1. Border  (테두리) 

- Border 특성

1. border-width : 테두리 굵기
2. border-color : 테두리 색상
3. border-style : 테두리 종류 (점선, 실선)
4. __box-sizing : border-box__ : 좌우 테두리를 기준으로 요소의 크기를 결정하게 만들어줌❗❗
5. border-radius : 모서리 곡률

>  한번에 width / style / color 특성 사용

```css
border: witdh style color;
```



### 2. Padding (패딩)  -  초록색

- 콘텐츠 박스와 테두리 사이의 남는 공간

```css
padding: 10px;                      /* 4방향 모두 */
padding: vertical horizontal;       /* 상하 좌우 */
padding: top horizontal bottom;     /* 상 좌우 하 */
padding: top right bottom left;     /* 상 우 하 좌 (시계방향) */
```



### 3. Margin (여백)  -  주황색

- 두 요소의 Border (테두리)간의 간격
- 몇몇 태그들은 기본적으로 마진이 설정되어있기도 함 (body, h1)

```css
margin: 10px;                      /* 4방향 모두 */
margin: vertical horizontal;       /* 상하 좌우 */
margin: top horizontal bottom;     /* 상 좌우 하 */
margin: top right bottom left;     /* 상 우 하 좌 (시계방향) */
```



---



## 2️⃣ Display

display 특성

- 인라인 요소는 width, height 무시, padding, margin 좌우는 적용, 상하는 무시

1. Inline : 블록 요소를 인라인 요소로 만들어줌 
2. Block : 인라인 요소를 블록 요소로 만들어줌
3. __Inline-Block__ : 인라인 요소처럼 작동하지만 width, height, padding, margin 적용가능❗❗
4. None : 안보이게 설정 (JS에서 활용)

```css
display: inline;
display: block;
display: inline-block;
display: none;
```



---



## 3️⃣ CSS 단위

상대적 단위 (Relavtive)

- em : 부모요소의 배수, 요소에 맞춰 자동으로 바뀌는 경우에 사용 (연동), 단점 여러번 상속되면 값 증감이 누적됨
- rem : 부모 요소에 따라 바뀌지않고 루트 HTML 요소의 글씨 크기에 따라 바뀜
- %

절대적 단위 (Absolute)

- px
- cm
- in 
- mm