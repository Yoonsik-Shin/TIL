# Bootstrap

- CSS 프레임워크

>  [Getbootstrap](https://getbootstrap.com/)



컨테이너

```css
<div class="container">
```



### 버튼

class="btn"







## 그리드 (Grid)

- 공간 분배를 화면 크기에 따라 달라지게 하는 반응형 레이아웃
- `flexbox`로 제작되어 모든 속성 사용가능 (justify, align)
- 컨테이너 안에서만 작동
- `row`(행) 클래스를 사용하여 행을 만들어야함
- 부트스트랩의 모든 행에는 분배될 공간이 12유닛씩 존재❗
- 기본요소
  - `Column` : 실제 컨텐츠를 포함하는 부분
  - `Gutter` : 컬럼들 사이의 공간
  - `Container` : 컬럼들을 담고 있는 공간

```html
<div class="container">
  <div class="row">
    <div class="col-6">1 / 12 ~ 6 / 12</div>
    <div class="col-6">7 / 12 ~ 12 / 12</div>
  </div>
  <div class="row">
    <div class="col"></div>     <!-- 균일하게 배치 -->
    <div class="col"></div>     <!-- 균일하게 배치 -->
  </div>
</div>
```

> Offset

- 열을 오른쪽으로 이동
- 열의 왼쪽 여백을  늘림



### 중단점 (Breakpoints)

- 6개의 `grid breakpoints`를 가짐

| 중단점            | 표기   | 너비                 | 컨테이너 (max-width) |
| ----------------- | ------ | -------------------- | -------------------- |
| X-Small           | (생략) | 0 < X < 576px        | (자동)               |
| Small             | sm     | 576px <= X < 768px   | 540px                |
| Medium            | md     | 768px <= X < 992px   | 720px                |
| Large             | lg     | 992px <= X < 1200px  | 960px                |
| Extra large       | xl     | 1200px <= X < 1400px | 1140px               |
| Extra extra large | xxl    | 1400px <= X          | 1320px               |

```css
@media (min-width: 576px) {
	.container-sm, .container {
		max-width: 540px;
		}
}
@media (min-width: 768px) {
	.container-md, .container-sm, .container {
		max-width: 720px;
	}
}
@media (min-width: 992px) {
	.container-lg, .container-md, .container-sm, .container {
		max-width: 960px;
	}
}
@media (min-width: 1200px) {
	.container-xl, .container-lg, .container-md, .container-sm, .container {
		max-width: 1140px;
	}
}
@media (min-width: 1400px) {
	.container-xxl, .container-xl, .container-lg, .container-md, .container-sm, .container {
		max-width: 1320px;
	}
}
```

