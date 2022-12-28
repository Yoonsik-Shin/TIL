# JavaScript 정리 (6)

​    

## 1️⃣ Call Stack (콜 스택)

- 여러 함수를 호출하는 스크립트에서 해당 위치를 추적
- 스크립트가 함수를 호출하면 해석기는 콜 스택에 추가한 후 함수 수행
- 현재 함수가 완료되면 해석기는 콜 스택에서 함수를 제거
- 크롬 디버거 > `Sources`

> [Call-Stack-참고사이트](http://latentflip.com/loupe/?code=ZnVuY3Rpb24gbXVsdGlwbHkoeCx5KSB7CiAgICByZXR1cm4geCAqIHk7Cn0KCmZ1bmN0aW9uIHNxdWFyZSh4KSB7CiAgICByZXR1cm4gbXVsdGlwbHkoeCx4KTsKfQoKZnVuY3Rpb24gaXNSaWdodFRyaWFuZ2xlKGEsYixjKXsKICAgIHJldHVybiBzcXVhcmUoYSkgKyBzcXVhcmUoYikgPT09IHNxdWFyZShjKTsKfQoKaXNSaWdodFRyaWFuZ2xlKDMsNCw1KQ%3D%3D!!!)

​    

---

## 2️⃣ Single Thread (단일 스레드) & WebAPIs

- JS는 최대 한번에 한줄의 코드만 실행
- `WebAPIs` : JS에서 호출하여 브라우저로 전달하는 방법 (JS : 이건 내가 못하니 브라우저가 대신해줘)

```javascript
console.log('1');
setTimeout( () => {
  console.log('2')
}, 3000);
console.log('3');

// 1 출력후 3000ms후에 2 출력후 3 출력 (x)
// 1 출력후 setTimeout함수의 작업을 WebAPIs로 넘기고 3을 바로 출력, 3000ms후 2출력 (o)
>> 1 3 2
```

​    

---

## 3️⃣ Callback Hell

```javascript
setTimeout( () => {
  document.body.style.backgroundColor = 'red';
  setTimeout( () => {
  	document.body.style.backgroundColor = 'orange';
  	setTimeout( () => {
  		document.body.style.backgroundColor = 'yellow';
		}, 1000)
	}, 1000)
}, 1000)
```

​    

---

## 4️⃣ Promises  ✔️✔️

```javascript
// 데모 데이터 리퀘스트
const fakeRequestPromise = (url) => {
  return new Promise((resolve, reject) => {
    const delay = Math.floor(Math.random() * (4500)) + 500;  // 랜덤 지연시간 
    setTimeout(() => {
      if (delay > 4000) {
        reject('연결시간초과')
      } else {
      	resolve(`${url}로 부터 전송받은 데이터`);
    	}	
    }, delay)
  })
}

fakeRequestPromise('yoonsik.com/api/git/page1')
	.then((data) => {
  	console.log('정상작동 (page1)')
  	console.log(data)
  	return fakeRequestPromise('yoonsik.com/api/git/page2')
  })
  .then((data) => {
      console.log('정상작동 (page2)')
  		console.log(data)
  		return fakeRequestPromise('yoonsik.com/api/git/page3')
  })
  .then((data) => {
      console.log('정상작동 (page3)')
  		console.log(data)
  })
	.catch((error) => {
  	console.log('작동오류')
  	console.log(error)
})
```

- Callback Hell 극복하기

```javascript
const delayedColorChange = (color, delay) => {
  return new Promise((resovle, reject) => {
  	setTimeout(() => {
      document.body.style.backgroundColor = color;
      resolve();
    }, delay)
	})
}

delayedColorChange('red', 1000)
	.then(() => delayedColorChange('orange', 1000))
	.then(() => delayedColorChange('yellow', 1000))
	.then(() => delayedColorChange('green', 1000))
  .then(() => delayedColorChange('blue', 1000))
  .then(() => delayedColorChange('violet', 1000))
```

   

---

## 5️⃣ 비동기함수(Async funtions) 

### 5-1.`async` ✔️

- 함수 앞에 async를 입력하여 비동기함수로 선언하면 자동으로 `promise`를 반환

```javascript
async function hello() {}
const hello = async () => {}
```

- 비동기함수에 오류가 있으면 `promise`의 상태는 실패(`rejected`)로 뜸

​    

---

## 6️⃣ 대기함수 (Await function)

### 6-1. `await` ✔️

- 비동기 코드를 쓰면서 동기적으로 보이게 해줌
- `promise`가 값을 반환할 때까지 기다리기 위해 비동기함수의 실행을 일시 정지시킴
- `await` 키워드를 쓰면 `promise`가 결과를 낼 때까지 기다림

```javascript
const delayedColorChange = (color, delay) => {
  return new Promise((resovle, reject) => {
  	setTimeout(() => {
      document.body.style.backgroundColor = color;
      resolve();
    }, delay)
	})
}

async function rainbow() {
  await delayedColorChange('red', 1000)
  await delayedColorChange('orange', 1000)
  await delayedColorChange('yellow', 1000)
  await delayedColorChange('green', 1000)
  await delayedColorChange('blue', 1000)
  await delayedColorChange('violet', 1000)
}

async function printRainbow() {
  await rainbow();   
  console.log("END OF RAINBOW");  // rainbow 함수 종료후 출력됨
}
```

​    

---

## 7️⃣ Exports / Imports (Modules)

- 코드를 여러 파일로 나누고 가져올 수 있음
- `default` : 파일에서 어떤 것을 가져오면 항상 내보내진 것의 기본값을 가져옴 
- named export : 불러올 요소가 무엇인지 중괄호[`{}`]로 정확히 표현

```javascript
// person.js 파일
const person = {
  name: 'yoonsik';
}

export default person

// utility.js
// 두개의 상수를 내보냄
export const clean = () => {} 
export const baseData = 10;

//app.js
import person from './person.js'
import prs from './person.js'  // export를 default로 했기때문에 아무 이름을 사용해도됨

// 특정한 값을 읽기위해 중괄호 사용
import {baseData} from './utility.js'
import {clean} from './utility.js'
```

