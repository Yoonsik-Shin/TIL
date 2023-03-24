# Node.js (4) 

​    

## Socket.io

### 설치

```bash
$ npm install socket.io
$ yarn add socket.io
```



### 기본세팅

```js
// back-end
import http from "http";
import SocketIO from "socket.io";

const httpServer = http.createServer(app);
const io = SocketIO(httpServer);
const handleListen = () => console.log(`http://localhost:3000`);

httpServer.listen(3000, handleListen);
```

```html
<!-- front-end -->
<script>
	const socket = io();  
</script>
<script src="/socket.io/socket.io.js"></script>
```

​    

### 메시지 보내기

#### 유저 => 서버

```html
<!-- front -->
<input id='message'>
<button id='send'>서버에 메시지 전송</button>

<script>
	const message = document.querySelector('#message').value // 메시지 내용
  
	document
    .querySelector('#send')
    .addEventListener('click', () => {
    	socket.emit('메시지이름', message) ✔️✔️ // 유저 --> 서버로 메시지 전송
 		})
</script>
```

```js
// back
io.on('connection', (socket) => {  // 유저 --> 서버로 온 메시지 받기
  // 해당이름의 메시지를 받으면 콜백함수 실행
  socket.on('메시지이름', (data) => {
    console.log(data);  // 유저가 보낸 메시지
  }) 
})
```

​    

#### 서버 => 유저

```js
// back
io.on('connection', (socket) => {
	socket.on('메시지이름', (data) => {
    console.log(data);  // 유저가 보낸 메시지
    io.emit('메시지명', data) ✔️✔️ // 서버 --> 모든유저로 메시지 전송
    io.to(socket.id).emit('메시지명', data) ✔️✔️ // 서버 --> 해당소켓유저에게만 메시지 전송
    io.to('room아이디').emit('메시지명', data) ✔️✔️ // 서버 --> 해당룸에 있는사람들만 메시지 전송
  }) 
})
```

```html
<!-- front -->
<scirpt>
	socket.on('서버에서받은메시지명', (data) => {
  	console.log(data);  // 서버가 보낸 메시지
  })
</scirpt>
```



### 채팅방 만들기

```js
io.on('connection', (socket) => {
	socket.join('방이름');
})
```

