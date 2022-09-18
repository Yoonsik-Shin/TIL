const form = document.querySelector('form');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    const product = document.querySelector('#product')
    const qty = document.querySelector('#qty')
    add(product.value, qty.value);
    product.value = '';
    qty.value = '';
})

const add = (product, quantity) => {
    const newProduct = document.createElement('li');
    const ul = document.querySelector('#list')
    newProduct.innerText = `${quantity} ${product}`;
    ul.appendChild(newProduct);
}


// form.addEventListener('sumbit', (e) => {
//     e.preventDefault();
// })


// const form = document.querySelector('form');
// const product = document.querySelector('#product');
// const qty = document.querySelector('#qty');
// const list = document.querySelector('#list');

// form.addEventListener('submit', function (grocery) {
//     grocery.preventDefault();
    //     const productName = product.value;
    //     const size = qty.value;
    //     const data = `You Bought ${product.value}  ${qty.value} times.`;
    //     const newLi = document.createElement("li");
    //     newLi.innerText = data;
    //     list.appendChild(newLi);
    //     product.value = '';
    //     qty.value = '';
// });
