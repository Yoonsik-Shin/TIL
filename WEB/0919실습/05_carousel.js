const nextBtn = document.querySelector('#nextBtn')

nextBtn.addEventListener('click', () => {
    const currentElement = document.querySelector('.active')
    const items = document.querySelectorAll('.carousel-item')
    const idx = [...items].indexOf(currentElement)
    console.log(currentElement, items, idx)
    currentElement.classList.toggle('active')
    items[(idx + 1) % items.length].classList.toggle('active')
})

// previous 버튼 추가
// const previous = document.createElement('button')

// previous.innerText = 'previous'
// previous.classList = 'previous-Btn'
// document.body.append(previous)

const previousActive = document.querySelector('#prevBtn')

previousActive.addEventListener('click', () => {
    const currentElement = document.querySelector('.active')
    const items = document.querySelectorAll('.carousel-item')
    const idx = [...items].indexOf(currentElement)
    console.log(currentElement, items, idx)
    currentElement.classList.toggle('active') // 현재 포커싱되어있는 div에서 active클래스 삭제
    items[(idx - 1) % items.length].classList.toggle('active') // 전 div에 active클래스 추가
})