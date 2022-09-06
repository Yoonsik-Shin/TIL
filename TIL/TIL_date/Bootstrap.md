# Bootstrap

- CSS 프레임워크

>  [Getbootstrap](https://getbootstrap.com/)



컨테이너

```css
<div class="container">
```



### 버튼

class="btn"







## 그리드

콘텐츠 배열

공간 분배를 화면 크기에 따라 달라지게 하는 반응형 레이아웃

컨테이너 안에서만 작동

`row`(행) 클래스를 사용하여 행을 만들어야함

부트스트랩의 모든 행에는 분배될 공간이 12유닛씩 존재

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

반응형 처리
