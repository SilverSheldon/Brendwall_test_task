const productForm = document.getElementById('product-form');
const productsList = document.getElementById('products-list');

var url = "http://127.0.0.1:8000/api/v1.0/products/"

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Обработчик отправки формы
productForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Предотвращаем перезагрузку страницы
    const formData = new FormData(productForm);
    const productData = {
        title: formData.get('title'),
        description: formData.get('description'),
        price: parseFloat(formData.get('price')),
    };
    const response = await fetch(url, {
        mode: 'same-origin',
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json; charset=UTF-8',
        },
        body: JSON.stringify(productData),
    });
    if (!response.ok) {
        throw new Error('Ошибка при добавлении продукта');
    }
    await fetchProducts(); // Обновляем список продуктов
    productForm.reset(); // Сбрасываем форму
});


async function fetchProducts() {
    const response = await fetch(url, {mode: 'no-cors'});
    const products = await response.json();
    productsList.innerHTML = ''; // Очистить существующий список
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.title}</td>
            <td>${product.description}</td>
            <td>${Number(product.price).toFixed(2)}</td>
        `;
        productsList.appendChild(row);
    });
}

fetchProducts();

