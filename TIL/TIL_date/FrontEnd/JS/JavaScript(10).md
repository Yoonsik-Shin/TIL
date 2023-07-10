# JavaScript (10)

## 클로저 (Closure)

- MDN 정의 
  - 함수와 함수가 선언된 Lexical Environment의 조합
  - A closure is the combination of a function and the lexical environment within which that function was declared
- 정의
  - 상위 스코프의 식별자를 참조하는 하위 스코프가 외부에서 지속적으로 참조되어 상위 스코프보다 더 오래 존재하는 것
  - 상위 스코프의 식별자를 하위 스코프가 지속적으로 참조함
  - 하위 스코프가 계속 참조되는 한 상위 스코프는 종료되지 않고 지속됨
- 모든 함수형 언어가 가지고 있는 가장 중요한 특성

```js
let user;

{
    const privateUser = { id: 1, name: 'shin' }
    user = privateUser // 상위스코프의 식별자 user가 하위 스코프의 privateUser를 참조
}
// block이 종료되어 Block Lexical Environment가 사라져야하지만
// privateUser가 user를 참조하고 있어 사라지지 못함

user.age = 27
console.log(user) // { id: 1, name: 'shin', age: 30 }
```

