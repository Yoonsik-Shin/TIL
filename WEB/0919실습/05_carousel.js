const nextBtn = document.querySelector('#nextBtn')
nextBtn.addEventListener('click', function () {
    // 지금 active인 것은 어떻게 알죠?
    const currentElement = document.querySelector('.active')
    // 전체 item 중에....... 이 Element의 인덱스?
    const items = document.querySelectorAll('.carousel-item')
    const idx = [...items].indexOf(currentElement)
    console.log(currentElement, items, idx)
    currentElement.classList.toggle('active')
    items[(idx + 1) % items.length].classList.toggle('active')
})
