# Python `.env`  활용

1.  python-dotenv  모듈 다운로드

```bash
$ pip install python-dotenv
```



2. `.env` 파일 생성 및 숨길 내용 추가

```python
secret_key = 'hello'
```



3. 적용될 파일에 작성할 항목

```python
from dotenv import load_dotenv
import os

load_dotenv()
<변수> = os.environ.get('secret_key')
```



4. .gitignore 파일에 .env 작성

