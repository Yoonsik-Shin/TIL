const password = document.querySelector('#password')
const password_confirmation = document.querySelector('#password_confirmation')

if (password.value !== password_confirmation) {
    alert('비밀번호가 일치하지 않습니다.')
}