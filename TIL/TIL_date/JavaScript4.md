# JavaScript 정리4



## DOM

- Document Object Model : 문서 객체 모델
- 웹페이지를 구성하는 JavaScript 객체들의 집합

document

console.dir(document)

 

요소선택(Select) > 조작(Manipulate)



## 선택 메소드 (Selecting method)

### 1. getElementById

- id가 일치하는 요소를 찾음, 없으면 `null` 반환

```javascript
const 변수 = document.getElementById('ID')
```

​    

### 2. getElementsByTagName

- 태그가 일치하는 요소 찾음
- `HTMLCollection` 형태로 반환됨
- `.length`, `for-of` 사용가능

```javascript
const 변수 = document.getElementsByTagName('태그이름');

// 문서 내 모든 이미지 태그 같은 소스로 변경
const allImages = document.getElementsByTagName('img');

for (let img of allImages) {
  img.src = "새로운 사진";
}
```

​    

### 3. getElementsByClassName

- 클래스가 일치하는 요소 찾음
- `HTMLCollection` 형태로 반환됨

```javascript
// 문서 내 클래스가 같은 요소 찾아 반환
const ImageClass = document.getElementsByClassName('img');

for (let img of ImageClass) {
  img.src = "새로운 사진";
}
```

​    

### 4. QuerySelector

- 무엇이든 선택가능
- 첫 번째로 일치하는 값 반환

```javascript
document.qureySelector('p')
document.qureySelector('#banner')
document.qureySelector('.square')
document.qureySelector('img:nth-of-type(2)')
document.qureySelector('a[title="Java"]')
```

​     

### 5. QuerySelectorAll

- 무엇이든 선택가능
- 일치하는 모든 요소 반환

```javascript
const links = document.qureySelectorAll('p a');

for (let link of links) {
  console.log(link.href);
}
```

