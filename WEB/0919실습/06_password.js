// 비밀번호 일치/불일치

const form = document.querySelector('form')

const password = document.querySelector('#password')
const password_confirmation = document.querySelector('#password_confirmation')

password.addEventListener('change', () => {
    if (password.value.length < 8 && password.value.length > 0) {
        alert('비밀번호는 8자리 이상이어야 합니다.')
        password.value = ''
    }
})

password_confirmation.addEventListener('change', (e) => {
    if (password_confirmation.value.length < 8 && password_confirmation.value.length > 0) {
        alert('비밀번호는 8자리 이상이어야 합니다.')
        password_confirmation.value = ''
    } else {
        if (password.value !== password_confirmation.value) {
            alert('비밀번호가 일치하지 않습니다.')
            password.value = ''
            password_confirmation.value = ''
        } else {
            alert('비밀번호가 일치합니다.')
        }
    }
})

// form.addEventListener('change', (e) => {
//     e.preventDefault();

// }
// })