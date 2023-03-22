# Node.js (2)



## MongoDB

![image-20221218134729332](Node.js (2).assets/image-20221218134729332.png)

![image-20221218134738740](Node.js (2).assets/image-20221218134738740.png)

```bash
$ npm install mongodb
$ npm install mongodb@3.6.4  # 버전
$ yarn add mongodb
```

```js
var db;

const MongoClient = require('mongodb').MongoClient;
MongoClient.connect('URL', (error, client) => {
  if (error) { return console.log(error) };
  
  db = client.db('DB이름')
  
  app.listen(8080, () => {
    
  })
})
// URL에 DB Access 메뉴에서 만든 ID, PW 입력필요
```

![image-20221218135110983](Node.js (2).assets/image-20221218135110983.png)



database : 폴더

collection : 파일

DB에 저장하기

```js
db.collection('파일명').insertOne('저장할데이터(Object자료형)', (에러, 결과) => {
  console.log('저장완료')ㅣ;
});
// _id로 데이터의 ID값 직접 부여가능
```



DB에 저장된 데이터 보여주기



EJS

```bash
npm install ejs
```

- 파일확장자 : `.ejs`
- ejs 파일들은 `views`폴더 안에 생성해야함
- ejs문법을 이용하여 Server 데이터 삽입 가능

```ejs
<%= 변수이름 %>
```

```js
// 상단에 등록
app.set('view engine', 'ejs');

app,get('/', (request, response) => {
  // DB에 저장된 col이라는 collection안의 모든 데이터 꺼내기
  db.collection('col').find().toArray((error, result) => {
    console.log(error);
    response.render('*.ejs', { result : result });
  });
})
```

> 반복문 사용해보기

```ejs
<% for (let i = 0; i < data.length; i++) { %>
	array[i]
<% } %>
```

> auto increment

![image-20221218144724674](Node.js (2).assets/image-20221218144724674-1671342447644-1.png)

```js
app.post('/', (requset, response) => {
  response.send();
  db.collection('counter').findOne({name : '게시물개수'}, (error, result) => {
    
    var 총게시물수 = result.totalPost
   
    db.collection('post').insertOne({ _id : 총게시물수 + 1 }, (error, result) => {
      console.log(result)
      db.collection('counter').updateOne({name:'개시물개수'}, { $inc : {totalPost:1}}, 
        (error, result) => {	
        	if (error) { return console.log(error) }
      })
    })
  })
})
```

>operator

1. `$set` : 변경 

```js
{ $set : {totalPost : 바꿀값} }
```

2. `$inc` : 증가

```js
{ $inc : {totalPost: 기존값에 더해줄 값} }
```

3. `$min` : 기존값보다 적을때만 변경

4. `$rename` : key값 이름변경



DELETE / PUT 요청하는 법

1. method-override 라이브러리 이용

- HTML에서 PUT/DELETE 요청을 할 수 있게 해줌

```bash
$ npm install method-override
```

```js
// server.js
const methodOverride = require('method-override')
app.use(methodeOverride('_method'))
```



```ejs
<!-- ejs -->
<form action='/edit?_method=PUT' method="POST"></form>
```





2. AJAX 이용

```js

```



게시물마다 상세페이지 만들기



css파일 넣기

- public이라는 폴더 생성 후 그안에 생성 : public/main.css

```js
// static 파일을 보관하기 위해 public 폴더 사용을 정의
app.use('/public', express.static('public'));
```



component 형식으로 만들기

- 네비게이션바 : views/nav.html

```ejs
<%- include('nav.html') %>
```





Session 방식 로그인 구현

1. 라이브러리 설치 (3가지)

```bash
$ npm install passport passport-local express-session
```

```js
// server.js
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const session = require('express-session')

app.use(session({secret: '비밀코드', resave: true, saveUninitialized: false}));
app.use(passport.initialize());
app.use(passport.session());
```

> app.use : 미들웨어



