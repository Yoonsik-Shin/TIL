# Django 비동기처리

​     

## 1️⃣ Axios

- 브라우저를 위한 Promise 기반의 클라이언트

```django
<script src =="https://unpkg. axios dist /axios.min.js"></script>
<script>
	const URL = 'URL'
	axios.get(URL)
  	.then((res) => { console.log(res.data) })
  	.catch((error) => { console.log('Error') })
  	.finally(() => { console.log('무조건 실행되는 구문') })
</script>
```

​    

---

## 2️⃣ Promise

- 비동기 작업을 관리하는 객체
- 미래의 완료 or 실패와 그 결과 값을 나타냄
- 미래의 어떤 상황에 대한 약속
  - 성공(이행) : `.then()`
  - 실패(거절) : `.catch()`
- .then()과 .catch() 메서드는 모두 promise 를 반환하기 때문에 chaining 가능
  - 반환값이 반드시 있어야 함
  - 없다면 callback 함수가 이전의 promise 결과를 받을 수 없음

​     

> .then()

- 이전 작업이 성공했을 때 수행할 작업을 나타내는 콜백함수
- 이전 작업의 성공결과를 인자(response)로 전달받음
- 각각의 `.then` 블록은 서로 다른 promise 반환
- 여러 비동기 작업을 차례대로 수행할 수 있

> .catch()

- .then이 하나라도 실패하면 동작
- 이전 작업의 실패로 인해 생성된 error 객체 사용

> .finally()

- Promise 객체 반환
- 결과와 상관없이 무조건 지정된 콜백함수 실행
- 어떤 인자도 전달받지 않음

​         

---

## 3️⃣ 비동기(Async) 적용

### 1. 팔로우 (follow)

- block tag 영역 작성

```django
<!-- base.html -->
{% block script %}
{% endblock script %}
```

​     

- axios CDN 작성

```django
<!-- accounts/profile.html -->
{% block script %}
	<!-- axios CDN 작성 -->
	<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> 
{% endblock script %}
```

​     

- form 요소 id 속성 지정 / action, method 속성 삭제

```django
<!-- accounts/profile.html -->
<form id='follow-form' data-user-id="{{ person.pk }}"></form>

<script>
	const form = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  form.addEventListener('submit', (e) => {
    e.preventDefault() <!-- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소 -->
    const userID = e.target.dataset.userId
    axios({
      method: 'post',
      url: `/accounts/${userID}/follow/`,
      headers: {'X-CSRFToken': csrftoken}
    })
    	.then((response) => {
      	const isFollowed = response.data.is_followed
        const followBtn = document.querySelector('#follow-form > input[type=submit]')
        if (isFollowed === true) {
          followBtn.value == '언팔로우'
        } else {
          followBtn.value = '팔로우'
        }
      	const followersCountTag = document.querySelector('#followers count')
      	const followingsCountTag = document.querySelector('#followings count')
        followersCountTag.innerText = followersCount
      	followingsCountTag.innerText = followingsCount
    	})
  })
</script>
```

```python
# accounts/views.py
from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
  if request.user.is_authenticated:
    User = get_user_model()
    me = request.user
    you = User.objects.get(pk=user_pk)
    if me != you:
      if you.follwers.filter(pk=me.pk).exists():
        you.followers.remove(me)
       	if_followed = False
      else:
        you.followers.add(me)
        is_followed = True
      context = {
        'is_followed': is_followed,
        'followers_count': you.followers.count()
        'followings_count': you.followings.count()
      }
      return JsonResponse(context)
   	return redirect('accounts:profile', you.username)
  return redirect('accounts:login')
```

​    

- 팔로워 / 팔로잉수 비동기 적용

```django
<!-- accounts/profile.html -->
팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
```



> 총정리

```django
<!-- acoounts/profile.html -->
팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>

{% if request.user != person %}
	<form id='follow-form' data-user-id="{{ person.pk }}">
		{% csrf_token %}
    {% if request.user in person.followers.all %}
    	<input type="submit" value="언팔로우">
    {% else %}
     	<input type="submit" value="팔로우">
   	{% endif %}
	</form>
{% endif %}
```

```python
# accounts/views.py
@require_POST
def follow(request, user_pk):
  if request.user.is_authenticated:
    User = get_user_model()
    me = request.user
    you = User.objects.get(pk=user_pk)
    if me != you:
      if you.followers.filter(pk=me.pk).exists():
        you.followers.remove(me)
        is_followed = False
      else:
        you.followers.add(me)
        is_followed = True
      context = {
        'is_followed': is_followed,
        'followers_count': followers_count,
        'followings_count': followings_count,
      }
      return JsonResponse(context)
    return redirect('accounts:profile', you,username)
  return redirect('accounts:login')
```

```js
<!-- accounts/profile.html -->
const form = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

form.addEventListener('submit', (e) => {
  e.preventDefault()
  const userId = e.target.dataset.userID
  
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken,}
  })
  	.then((response) => {
    	const isFollowd = response.data.is_followed
      const followBtn = document.querySelector('#follow-form > input[type=submit]')
      if (isFollowed === true) {
        followBtn.value = '언팔로우'
      } else {
        followBtn.value = '팔로우'
      }
    	const followersCountTag = document.querySelector('#followers-count')
      const followingCountTag = document.querySelector('#followings-count')
      const followersCount = response.data.followers_count
      const followingsCount = response.data.followings_count
      followersCountTag.innerText = followersCount
    	followingsCountTag.innerText = followingsCount
  	})
  	.catch((error) => {
    	console.log(error.response)
  	})
})
```

​    

---

### 2. 좋아요 (like)

```django
<!-- articles/index.html -->
<form class='like-forms' data-article-id="{{ article.pk }}">
  {% csrf_token %}
  {% if request.user in article.like_users.all %}
  	<input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
  {% else %}
  	<input type="submit" value="좋아요" id="like-{{ article.pk }}">
 	{% endif %}
</form>
```

```python
# articles/views.py
from django.http import JsonResponse

@require_POST
def likes(request, article_pk):
  if request.user.is_authenticated:
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
      article.like_users.remove(request.user)
      is_liked = False
    else:
      article.like_user.add(request.user)
      if_like = True
    context = {
      'if_like': if_like,
    }
    return JsonResponse(context)
  return redirect('accounts:login')
```

```js
// articles/index.html
const forms = document.querySelectorAll('.like-forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

forms.forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault()
    const articleId = e.target.dataset.articleId
    
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/articles/${articleId}/likes/`,
      headers: {'X-CSRFToken': csrftoken},
    })
    	.then((res) => {
      	const isLiked = response.data.is_liked
        const likeBtn = document.querySelector(`#like-${articleId}`)
        if (isLiked === true) {
          likeBtn.value = '좋아요 취소'
        } else {
          likeBtn.value = '좋아요'
        })
       .catch((error) => {
         console.log(error.response)
       }) 
  })
})
```
