# JavaScript 정리 (5)

​    

## 0️⃣ DOM Event

- 사용자들이 하는 행동에 반응

​    

> 이벤트와 this

- `this`가 이벤트 핸들러에 의해 발동된 콜백함수 안에서 사용될 때 이벤트를 발동시키는 무언가와 상호작용하거나 그것을 기반으로 작동

```javascript
const makeRandColor = () => {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r}, ${g}, ${b}`;
}

// 기본
const buttons = document.querySelectorAll('button');
for (let button of buttons) {
  button.addEventListener('click', function () {
    button.style.backgroundColor = makeRandColor();
    button.style.color = makeRandColor();
  })
}

const h1s = document.querySelectorAll('h1');
for (let h1 of h1s) {
  button.addEventListener('click', function () {
    h1.style.backgroundColor = makeRandColor();
    h1.style.color = makeRandColor();
  })
}

// this 키워드 사용
function colorize(){
  this.style.backgroundColor = makeRandColor();
  this.style.color = makeRandColor();
}

const buttons = document.querySelectorAll('button');
for (let button of buttons) {
  button.addEventListener('click', colorize)
}

const h1s = document.querySelectorAll('h1');
for (let h1 of h1s) {
  button.addEventListener('click', colorize) 
  })
}
```

​    

---

## 1️⃣ 모든 이벤트 선택/제거

### 1-1. addEventListener  ✔️✔️

- 모든 이벤트를 전달 가능 (click, double click, mouseenter...)
- 이벤트 종류는 mdn문서 참조

> https://developer.mozilla.org/ko/docs/Web/Events

```javascript
.addEventListener(이벤트종류, 실행될 객체 or 함수 [, 옵션]);

const btn3 = document.querySelector('#v3');
btn3.addEventListener('dbclick', fuction () {
	alert('더블클릭 되었습니다.');
})

btn3.addEventListener('dbclick', fuction () {
	alert('더블클릭 되었습니다.');
}, { once: true})   //  addEventListener가 한번만 실행되고 삭제됨
```

​    

### 1-2. removeEventListener

​    

---

## 2️⃣ 마우스 이벤트

### 2-1. onclick

- 인라인 스타일 : html 태그에 넣기

```html
<button onclick="alert('버튼이 눌림')";></button>
```

- 자바스크립트 활용 ✔️

```javascript
const btn = document.querySelector('#id값');

btn.onclick = function () {
  alert('버튼이 눌림');
}
```

​    

### 2-2. onmouseenter

- 마우스가 특정 영역 위에 놓였을 때

```javascript
function scream() {
  alert('범위에 들어 왔습니다.')
}

btn.onmouseenter = scream;
```

​    

---

## 3️⃣ 키보드 이벤트

> 이벤트 객체 (Event Object) : 이벤트에 대한 정보를 담고 있는 객체

```javascript
const input = document.querySelector('input');
input.addEventListener('keydown', function (event) {   // 키보드를 눌름
  console.log(event.key);   // Shift         // a       // 화면에 적용되는 기준
  console.log(event.code);  // ShiftLeft     // KeyA    // 키보드 기준
  
})

input.addEventListener('keyup', function () {   // 키보드 눌림이 해제됨
  console.log('keyup');
})
```

- `key` : 어떤 글자가 생성되었는지 알아내는데 사용
- `code` : 실제로 키보드에서 키가 눌린 위치를 알아내는데 사용

```javascript
// 페이지 어느 곳에서든 이벤트 수신하기
window.addEventListenser('Keydown', function (e) {  ✔️✔️
  swich(e.code){
    case 'ArrwUp':
    	console.log('UP');
    	break
    case 'ArrwDown':
    	console.log('Down');
    	break
    case 'ArrwLeft':
    	console.log('Left');
    	break
    case 'ArrwRight':
    	console.log('Right');
    	break
    default:
    	console.log('X');
  }
})
```

​    

---

## 4️⃣ 폼 이벤트

- 페이지 안넘기고 댓글남기기 

```html
<form action="/" id="tweetForm">
	<input type="text" name="username" placeholder="username">
  <input type="text" name="tweet" placeholder="tweet">
  <button>Post Tweet</button>
</form>

<h2>Tweets:</h2>
<ul id="tweets">
  
</ul>
```

```javascript
const tweetForm = document.querySelector('#tweetForm')
// 제출
tweetForm.addEventListener('sumbit', function(e){
  e.preventDefault();   // 페이지가 바뀌는 것을 방지해줌
  alert('submit')
})

// 댓글 작성
const tweetForm = document.querySelector('#tweetForm');
const tweetsContainer = document.querySelector('#tweets');
tweetForm.addEventListener('submit', function (e) {
  e.preventDefault();  
  const usernameInput = tweetForm.elements.username;
  const tweetInput = tweetForm.elements.tweet;
  addTweet(usernameInput.value, tweetInput.value)
  usernameInput.value = '';
  tweetInput.value = '';
})

const addTweet = (username, tweet) => {
  const newTweet = document.createElement('li');
  const bTag = document.createElement('b');
  bTag.append(username)
  newTweet.append(bTag);
  newTweet.append(`- ${tweet}`)
  tweetsContainer.append(newTweet);
}
```

- `preventDefault` : 이벤트 결과로서 일어날 기봉 동작을 방지 ✔️✔️

​    

---

## 5️⃣ 입력(input) / 변경(change) 이벤트

- 입력시 실시간으로 이벤트가 일어남

​    

### 5-1. 변경 이벤트 [`change`]

- `change`는 입력 했을 때가 아니라, 입력한 후 입력에서 떠날때 마다 이벤트 발동 (blur)
- enter 키를 치는 것이 아님

```javascript
const input = document.querySelector('input');

input.addEventListener('change', (e) => {  
  console.log('');
})
```

​    

### 5-2.입력 이벤트 [`input`]

- 입력 내의 값이 달라질 때마다 발동
- 뭔가 타이핑 될때마다 이벤트 발동
- 입력값에 영향을 주지 않는 키를 누르면 반응 x
- 복사/붙여넣기도 이벤트로 간주

```javascript
// 입력창 입력/삭제시 h1태그의 글도 동기화됨
const input = document.querySelector('input');
const h1 = document.querySelector('h1');

input.addEventListener('input', (e) => {
  h1.innerText = input.value;
})
```

​    

---

## 6️⃣ 이벤트 버블링

- 하위요소의 이벤트가 상위요소들의 이벤트까지 영향을 미치는 경우 

```html
<section onclick="alert('3')">
  <p onclick="alert('2')">
		<button onclick="alert('1')"></button> <!--> 버튼 클릭시 1, 2, 3 순서로 버블링 </-->
	</p>
</section>
```

- 버블링 멈추기
  - `e.stopPropagation()` : 이벤트가 더 이상 버블링하지 않도록 막아줌

```html
<div id="container">
  <button id="changeColor"></button> 
</div>
```

```javascript
const container = document.querySelector('#container');
const button = document.querySelector('#changeColor');

// 버튼 클릭시 div 배경색 변경
button.addEventListener('click', (e) => {
	container.style.backgroundColor = 'green';
	e.stopPropagation();  // 상위요소에는 영향을 끼치지 않도록 만들어줌
})

// div 클릭시 안보이게 하기
container.addEventListener('click', () => {
  container.classList.toggle('hide'); 
})
```

​    

---

## 7️⃣ 이벤트 위임 (Event Delegation)

- `e.target`
- 상위요소에 `EventListener`를 추가
- 이벤트 수신기가 추가된 시점에 페이지에 없었던 요소를 다루는 상황에서 사용

```html
<form action="/" id="tweetForm">
	<input type="text" name="username" placeholder="username">
  <input type="text" name="tweet" placeholder="tweet">
  <button>Post Tweet</button>
</form>

<h2>Tweets:</h2>
<ul id="tweets">
</ul>
```

```javascript
// 댓글 작성
const tweetForm = document.querySelector('#tweetForm');
const tweetsContainer = document.querySelector('#tweets');
tweetForm.addEventListener('submit', function (e) {
  e.preventDefault();  
  const usernameInput = tweetForm.elements.username;
  const tweetInput = tweetForm.elements.tweet;
  addTweet(usernameInput.value, tweetInput.value)
  usernameInput.value = '';
  tweetInput.value = '';
})

const addTweet = (username, tweet) => {
  const newTweet = document.createElement('li');
  const bTag = document.createElement('b');
  bTag.append(username)
  newTweet.append(bTag);
  newTweet.append(`- ${tweet}`)
  tweetsContainer.append(newTweet);
}

// ul태그 클릭으로 li 지우기
tweetsContainer.addEventListener('click', (e) => {
  e.target.nodeName === 'LI' && e.target.remove();
})
```
