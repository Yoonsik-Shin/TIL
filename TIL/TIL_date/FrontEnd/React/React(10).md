# React (10)

​    

## 이미지 업로드

### graghql

```tsx
const UPLOAD_FILE = gql`
  mutation uploadFile($file: Upload!) {
    uploadFile(file: $file) { url }
  }
`;

export default function ImageUploadPage() {  
  const fileRef = useRef<HTMLInputElement>(null)
 	const [imageUIrl, setImageUrl] = useState('')
  const [uploadFile] = useMutation(UPLOAD_FILE);
  
  const onChangeFile = async (e: ChangeEvent<HTMLInputElement>) => {
  	const file = e.target.files?.[0];
    
    // 파일 검증
    const isValid = checkValidationFile(file);
    if (!isValid) return;
    
    // 파일 업로드
    try {
      const result = await uploadFile({ variables: { file } });
      setImageUrl(result.data?.uploadFile.url ?? "");
    } catch (error) {
      console.log(error)
    }
  	
  // 가짜 이미지업로드 박스에 input 태그를 연결
  const onClickImage = () => {
    fileRef.current?.click()
  }
    
  return (
  	<>
    	<div onClick={onClickImage}>이미지선택</div>
      <input style={{ display: "none" }} type="file" onChange={onChangeFile} ref={fileRef} />
    	{/* multiple 속성으로 여러개 드래그 가능 */}
  		<img src={imageUrl} />
    </>
  )
}
```

```typescript
// src > commons > lib > validationFile.ts
export const checkValidationFile = (file?: File) => {
  if (!file?.size) {
    alert("파일이 없습니다!");
    return false;
  }

  if (file.size > 5 * 1024 * 1024) {
    alert("파일 용량이 너무 큽니다. (제한: 5MB)");
    return false;
  }

  if (
    !file.type.includes("jpg") &&
    !file.type.includes("jpeg") &&
    !file.type.includes("png")
  ) {
    alert("jpeg 파일 또는 png 파일만 업로드 가능합니다.");
    return false;
  }

  return true;
};

```



```bash
$ yarn add apollo-upload-client
$ yarn add @types/apollo-upload-client --dev
```

- Apollo 설정

```tsx
// src > components > commons > apollo > index.tsx
import { ApolloProvider, ApolloClient, ApolloLink } from '@apollo/client'
import { createUploadLink } from 'apollo-upload-client'

interface IApolloSettingProps {
  children: JSX.Element
}

export default function ApolloSetting(props: IApolloSettingProps) {
  const uploadLink = createUploadLink( uri: '' })  ✔️✔️
  
  const client = new ApolloClient({
    link: ApolloLink.from([uploadLink])  ✔️✔️
  })
  
  return (
  	<ApolloProvider client={client}>
      {props.children}
    </ApolloProvider>
  )
}
```



###  rest-api



## 결제

