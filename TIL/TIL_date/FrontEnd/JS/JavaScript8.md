#  JavaScript 정리 (8) - OOP (객체지향 프로그래밍)

​    

## 1️⃣ Object prototypes 

-  프로토를 조작할 일은 거의 없음
-  prototype은 한마디로 유전자 
- 부모에게 유전자를 등록하면 자식은 자유롭게 활용가능
- prototype은 함수에만 생성 (배열, 객체에는 x)

​    

- 다른 종류의 객체에 대한 프로토타입인 하나의 객체가 존재

```javascript
Array.prototype   // 배열 프로토타입
String.prototype  // 문자열 프로토타입
```

- 새로운 프로토타입 메서드 정의하기

```javascript
String.prototype.newMetodName = () => {};
Array.prototype.pop = () => {};  // 이미 있는 메서드는 오버라이딩됨
```

- 메서드 적용 방식

```js
arr.sort();
1. arr에 sort()가 있는가?
2. arr의 부모 prototype(Array.prototype)에 sort()가 있는가? 
```

​    

> `__proto__`

-  proto(프로토) = dunder(double underscore) 
- 내 부모의 유전자 (부모의 prototype) 검사를 하고 싶을 때 사용
- 모든 배열에 대해 별개의 메서드를 갖는게 아닌 하나의 프로토타입에 각각의 배열이 `__proto__`라는 특별한 특성으로 그 프로토타입을 참조함

```js
var 부모 = { name: 'Shin' };
var 자식 = {};

1. 자식.__proto__ == 부모.prototype;
2. Object.getPrototypeOf(자식) == 부모.prototype; 

자식.name;
>> "Shin"
```

​    

---

## 2️⃣ 팩토리 함수 (Factory Functions)

- 어떤 값을 전달하면 팩토리가 객체를 만들어주고 마지막에 반환하여 사용할 수 있게 만들어줌
- 이상적인 방법은 아님 ❌

```javascript
function makeColor(r, g, b) {   // 팩토리함수
  const color = {};   // 객체 생성
  color.r = r;
  color.g = g;
  color.b = b;
  color.rgb = () => {
    const {r, g, b} = this;
    return `rgb(${r}, ${g}, ${b}`
  };
  color.hex = () => {
    const {r, g, b} = this;
    return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  }
  return color;  // 마지막에 객체 반환
}

const firstColor = makeColor(35, 255, 150);  // 새로운 객체 만들어줌
firstColor.hex()    // 정의한 메서드 사용가능
firstColor.r = 255  // 정의한 값 변경가능
```

​    

---

## 3️⃣ 생성자 함수 (Constructor Function)

- 팩토리 함수보다 효율적
- 생성자 함수를 표시할 때는 보통 대문자 사용

```javascript
// 생성자 함수
function Color(r, g, b) {
  this.r = r;   // this는 새로 생성되는 object를 의미
  this.g = g;
  this.b = b;
}

// 메서드 추가하기
Color.prototype.rgb = function () {
  const { r, g, b } = this;
  return `rgb(${r}, ${g}, ${b}`;
};

Color.prototype.hex = function () {
    const {r, g, b} = this;
    return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  };

Color.prototype.rgba = function(a=1.0) {
  const { r, g, b } = this;
  return `rgba(${r}, ${g}, ${b} ${a}`;
};

// 새 객체 정의
new Color(255, 40, 100);  // new 키워드를 사용하지 않으면 this가 window 객체를 참조함
```

​    

---

## 4️⃣ 클래스  (Class) ✔️✔️

- 객체를 설명하는 설명서
- 생성자 함수보다 효율적
- 클래스를 표시 할때는 보통 대문자 사용

```javascript
class Color {
  constructor(r, g, b, name){   // 새로운 인스턴스를 인스턴스화 할때마다 클래스에 상관없이 즉시 실행
    this.r = r;    // this가 자동으로 새로운 객체 참조
    this.g = g;
    this.b = b;
    this.name = name;
  }
  innerRGB() {  // 메서드 생성
    const { r, g, b } = 'this';
    return `rgb(${r}, (${g}, (${b}`; 
  }
  rgb() {    
    return `rgb(${this.innerRGB()})`;
  };
  rgba(a = 1.0){
    return `rgba(${this.innerRGB()}, ${a})`;
  }
  hex() {
    const {r, g, b} = this;
    return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  };
}

const c1 = new Color(255, 67, 89, 'tomato');
c1.rgb()  // 메서드 활용
c1.hex()
```

​    

---

## 5️⃣ 상속 ✔️✔️

- 클래스간의 기능 공유

```javascript
// 상속 x
class Cat {
  constructor(name, age){
    this.name = name;
    this.age = age;
  }
  eat() {
    return `${this.name} is eating!`
  }
  meow(){
    return '야옹';
  }
}

class Dog {
    constructor(name, age){
    this.name = name;
    this.age = age;
  }
  eat() {
    return `${this.name} is eating!`
  }
  bark() {
    return '멍';
  }
}

const catty = new Cat('catty', 5);
const watty = new Dog('watty', 10);
```

​    

### 5-1. extend

```javascript
// 상속 o
class Pet {
  constructor(name, age){
    this.name = name;
    this.age = age;
  }
  eat() {
    return `${this.name} is eating!`
  }
}

class Cat extends Pet{   // Pet 클래스 상속
  meow(){
    return '야옹';
  }
}

class Dog extends Pet {  // Pet 클래스 상속
  bark() {
    return '멍';
  }
}
```

- 부모 클래스와 자식 클래스에 이름은 같고 내용이 다른 메서드가 있다면 자식클래스에서 메서드 사용시 자식의 속성에서 시작하여 상위 요소들로 올라감 (자식 > 부모 > 프로토타입)

​    

### 5-2. super

- 상속받을 때 부모 생성자로부터 중복되는 요소를 받을 때 사용

```javascript
class Pet {
  constructor(name, age){
    this.name = name;
    this.age = age;
  }
  eat() {
    return `${this.name} is eating!`
  }
}

class Cat extends Pet{   // Pet 클래스 상속
  constructor(name, age, livesLeft = 9){ 
    super(name, age)   // Pet 클래스 상속 // 부모 class의 constructor 의미
    this.livesLeft = livesLeft;
  }
  meow(){ 
    return '야옹';
  }
  eat() {
    return `I'm not dog!`
    super.eat() // 부모 class의 prototype을 의미 // 부모.prototype.eat()
  }
}
```

​    

> ES5 방식 상속 구현

```js
Object.create(프로토타입 객체)
```

```js
var 부모 = { name: 'Lee', age: 58 };
var 자식 = Object.creaet(부모);   // 프로토타입을 부모로 지정

자식.name
>> 'Lee'
1. 자식이 name을 가졌는가?  [`X`]
2. 부모 프로토타입에 name을 가졌는가? [`O`]


자식.age = 20;
자식.age
>> 20

var 손자 = Object.create(자식);

손자.name
>> 'Lee'

손자.age
>> 20
```

​     

---

## 6️⃣ getter / setter

```js
class people {
  constructor(){
    this.name = 'Shin';
    this.age = 26;
  }
  get nextAge(){
    return this.age + 1
  }
  set setAge(age){
    this.age = parseInt(age);
  }
}

person1 = new people();

person1.nextAge;
>> 27

person1.setAge = 10
>> people {name:'Shin', age: 10}
```

- set : 데이터를 변경하는 함수에 사용
  - 파라미터가 1개 이상 있어야 함
- get : 데이터를 꺼내쓰는 함수에 사용
  - return이 반드시 있어야 함
  - 파라미터가 없어야 함
