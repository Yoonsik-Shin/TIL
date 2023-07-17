# Node.js (4) 

## 1️⃣ SSE 

- Server Sent Event
- 서버가 일방적으로 데이터를 실시간으로 전송
- 문자열만 전송가능

```js
// front-end
// 서버에서 보낸 데이터 받기
eventSource ?? eventSource.close()
eventSource = new EventSource(`/경로/${chatRoomId}`)
eventSource.addEventListener('데이터이름', (e) => {
    console.log(JSON.parse(e.data))
})

// back-end
app.get('/경로/:parentId', isLogin, (req, res) => {
    res.writeHead(200, {
        "Connection": "keep-alive",
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache"
    })
    
    db.collection('message')
        .find({ parent: req.params.parentId })
        .toArray()
    	.then((result) => {
			res.write('event: 데이터이름\n')
			res.write(`data: ${JSON.stringify(result)}\n\n`)
    	})
   	
    // MongoDB Change Stream 설정
    // 찾을 문서
    const pipeLine = [
        { $match: { 'fullDocument.parent': req.params.parentId } }
    ]
    const changeStream = db.collection('message').watch(pipeline)
    changeStream.on('change', (result) => {
        // 추가된 문서
        const addedpipeLine = [result.fullDocument]
        res.write('event: 데이터이름\n')
        res.write(`data: ${JSON.stringify(addedpipeLine)}\n\n`)
    })
})
```

​    

---

## 2️⃣ Socket.io

- 실시간, 양방향, 이벤트 기반의 통신을 제공해주는 프레임워크

​    

### 설치

```bash
# back-end
$ npm install socket.io
$ yarn add socket.io
```

​    

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

#### 유저 => 서버 (Front to Back)

- `emit`
  - 데이터 전송
- `done`
  - 마지막 인자로 오는 함수는 백엔드의 `done`함수에 전달됨
  - 백엔드에서 실행되지 않고, 프론트엔드에서 실행됨

```js
socket.emit(
  '메시지이름',  // 고정
  보낼 내용들1,  // ❗제한없이 여러개 보낼수 있음
  ...
  보낼 내용들11,
  실행될 함수    // 마지막 인자는 함수만 올 수 있음
)
```

```html
<!-- front-end -->
<input id='message'>
<button id='send'>서버에 메시지 전송</button>
<script>
	const socket = io(); 
	const message = document.querySelector('#message').value // 메시지 내용
	const button = document.querySelector('#send').addEventListener('click', () => {
    	socket.emit('메시지이름', message) ✔️✔️ // 유저 --> 서버로 메시지 전송
      	message.value = ''
 	})
</script>
```

```js
// back-end
io.on('connection', (socket, done) => {  // 유저 --> 서버로 온 메시지 받기
  // 해당이름의 메시지를 받으면 콜백함수 실행
  socket.on('메시지이름', (data) => {
    console.log(data);  // 유저가 보낸 메시지
    done() // 프론트에서 보낸 함수를 다시 프론트에서 실행하도록 함
  }) 
})
```

​    

#### 서버 => 유저 (Back to Front)

- `io.emit()` : 서버에서 프론트의 모든 유저에게 메시지 전송
- `socket.on()` : 프론트에서 서버로부터 받은 메시지 수신

```js
// back-end
io.on('connection', (socket) => {
	socket.on('메시지이름', (data) => {
        // 서버 --> 모든유저로 메시지 전송
    	io.emit('메시지명', data) ✔️✔️ 
        
         // 서버 --> 해당소켓유저에게만 메시지 전송
    	io.to(socket.id).emit('메시지명', data) ✔️✔️
        
         // 서버 --> 해당룸에 있는사람들만 메시지 전송
    	io.to('room아이디').emit('메시지명', data) ✔️✔️
  	}) 
})
```

```html
<!-- front-end -->
<script>
    const socket = io(); 
    socket.on('서버에서받은메시지명', (data) => {
    	console.log(data);  // 서버가 보낸 메시지
   	})
</script>
```



### 채팅방 만들기

```js
io.on('connection', (socket) => {
   	socket.on('joinRoom', (data) => {
        // 채팅방 생성 및 입장
        socket.join('방이름');
    })   
})
```
