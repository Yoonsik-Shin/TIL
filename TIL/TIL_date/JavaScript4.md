# JavaScript 정리4



## DOM

- Document Object Model : 문서 객체 모델
- 웹페이지를 구성하는 JavaScript 객체들의 집합

document

console.dir(document)

 

요소선택(Select) > 조작(Manipulate)

​    

---

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

​    

---

## 조작 메소드 (Manipulating method)

### 1. innerText 

- 여는 태그와 닫는 태그 사이의 내용을 텍스트로 반환
- 태그는 모두 무시하고 숨겨진 항목은 무시

```javascript
document.querySelector('').innerText
document.querySelector('h1').innerText = '<i> title </i>'
>> '<i> title </i>'  // 태그가 무시되고 문자열 같이 취급됨
```

​    

### 2. textContent

- innerText와 비슷하지만 현재 나타난 내용이나 사용자에게 보이는 내용은 신경 안씀
- 저장한 방식에 따라 표기됨
- 숨겨놓은 것들도 모두 나오게함

```javascript
document.querySelector('').textContent
```

​    

### 3. innerHTML

- 태그 이름을 포함한 전체 콘텐츠 검색
- 요소를 다른 요소 안에 추가할 때 사용가능

```javascript
document.querySelector('').innerHTML
document.querySelector('p').innerHTML = '<b> bold </b>'
>> bold // 글꼴 굵게 설정됨
```

​    

---

## 속성 (Attributes) 

### getAttribute /  setAttribute

```javascript
document.querySelector('').태그속성

// 속성에 바로 접근
document.querySelector('a').href  
>> "file://~~~"

// getAttribute 메서드
const firstLink = document.querySelector('a')
firstLink.getAttribute('href')
>> "~~~"

// setAttribute 메서드
firstLink.setAttribute('href', '바꿀 속성의 값')
```

​    

---

## 스타일

```javascript
// 인라인 스타일로 적용됨
h1.style.color = 'green'
h1.style.fontSize = '3em'
h1.style.border = '2px solid pink'

>> <h1 style="color: green; font-size: 3em; border: 2px solid pink"></h1>
```

> 실제 스타일 알아내기

```javascript
const h1 = document.querySelector('h1')
window.getComputedStyle(h1)  // >> CSSStyleDeclartion로 반환
window.getComputedStyle(h1).color  // 적용되어있는 color값 반환
window.getComputedStyle(h1).fontSize  // 적용되어있는 font-size값 반환
```

​    

---

## 클래스 적용

### classList

- classList에는 내장된 메서드들이 존재
- 클래스를 적용하는 방법

```javascript
// 방법2 : classList 활용
const h2 = document.querySelector('h2')
h2.classList.add('purple')   // 클래스에 purple 추가 >> <h2 class='purple'>
h2.classList.add('border')   // 클래스에 border 추가 >> <h2 class='purple border'>

h2.classList.remove('border')  // 클래스에서 border 제거

h2.classList.contians('border')  // 클래스에 border가 존재하는지 여부 반환 >> false
h2.classList.contians('purple')  // 클래스에 purple이 존재하는지 여부 반환 >> True

h2.classList.toggle('purple') // 클래스에 purple이 존재하면 삭제하고, 없으면 추가 ❗❗
```

​    

---

## 계층이동

### 1. 부모

```html
<body>
  <p>
    <b></b>
  </p>
</body>
```

#### 1-1.parentElement 

- 한 단계 위의 부모요소를 반환
- 버튼을 클릭했을 때 버튼의 부모 요소나 자식 요소상에 변경을 가하게 할 수 있음

```javascript
const firstBold = document.querySelector('b')
firstBold  //  <b></b>
firstBold.parentElement  //  <p></p>
firstBold.parentElement.parentElement  //  <body></body>
```

​    

### 2. 자식

```html
<body>
  <p>
    <b></b>
  </p>
</body>
```

#### 2-1. children

- 배열처럼 생긴 HTMLCollection 반환
- 반복 가능

```javascript
const firstBold = document.querySelector('b')
const paragraph = firstBold.parentElement

paragraph.children
>> HTMLCollection(3) [a, a, b]

paragraph.children[0]
>> <a></a>
```

#### 2-2.  childElementCount

- 자식 요소의 개수 알려줌

​    

### 3.  형제

#### 3-1. previousSibling / nextSibling

- 요소가 아닌 노드를 출력
- 잘 안씀

#### 3-2. previousElementSibling / nextElementSibling ✔️✔️

- 실제 형제 요소를 반환

​    

---

## 새 요소 만들기

### 1. createElement / appendChild

```jav
node.appendChild()
```

```javascript
const newImg = document.createElement('img')  // 새 이미지 태그 만들기
newImg.src = ""  // 이미지 소스 추가하기
document.body.appendChild(newImg)  // 페이지에 추가하기
newImg.classList.add('square')  // 클래스 추가
```

```javascript
const newH3 = document.createElement('h3')  // h3 태그 생성
newH3.innerText = 'I am new!'  // 태그에 내용 추가
document.body.appendChild(newH3)  // 페이지에 추가
```

​    

### 2. append

- 어떤 항목의 요소의 마지막 자식으로 삽입

```javascript
const p = document.querySelector('p')
p.append('hello', 'bye')
// appendChild는 불가능
```

​    

### 3. prepend

- 어떤 항목을 요소의 첫 번째 자녀로 삽입

```javascript
const p = document.querySelector('p')
const newB = document.createElement('b')
newB.append('hi')
p.prepend(newB)
```

​    

### 4. insertAdjacentElement (position, element)

- position
  - `beforebegin` : 특정 요소의 앞
  - `afterbegin` :  특정 요소내에서 첫번째 자식
  - `beforeend` : 특정 요소내에서 마지막 자식
  - `afterend` : 특정 요소의 뒤

```javascript
const h2 = document.creatElement('h2')
h2.append('go to bed')
const h1 = document.querySelector('h1')
h1.insertAdjacentElement('afterend', h2)
```

​    

### 5. after

- 다른 요소 바로 다음에 삽입

```javascript
const h3 = document.createElement('h3')
h3.innerText = 'I am h3';
h1.after(h3) ✔️
```

​    

### 6. before

- 다른요소 바로 전에 삽입

​    

---

## 요소 제거 

### 1. remove

- 선택한 요소를 제거

```javascript
const img = document.querySelector('img')
img.remove()
```

​    

### 2. removeChild

- 선택한 요소의 자식을 제거
- 잘 안쓰임
- 제거하려는 요소의 부모를 호출해야함
