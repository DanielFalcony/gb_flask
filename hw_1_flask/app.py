from flask import Flask, render_template

app = Flask(__name__)

# Мокап данных о товарах (в реальных проектах данные будут храниться в базе данных)
products_data = {
    'Одежда': [
        {'name': 'Футболка', 'price': 1000},
        {'name': 'Джинсы', 'price': 2000},
        # Добавь еще товары...
    ],
    'Обувь': [
        {'name': 'Кроссовки', 'price': 2500},
        {'name': 'Сапоги', 'price': 3000},
        # Добавь еще товары...
    ],
    'Куртка': [
        {'name': 'Ветровка', 'price': 3500},
        {'name': 'Пуховик', 'price': 5000},
        # Добавь еще товары...
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/<category_name>')
def category(category_name):
    if category_name in products_data:
        products = products_data[category_name]
        return render_template('category.html', category_name=category_name, products=products)
    else:
        return "Такая категория не найдена"

@app.route('/product/<product_name>')
def product(product_name):
    # Предполагается, что здесь будет логика для получения информации о товаре из базы данных
    # В данном примере просто отобразим имя товара
    return render_template('product.html', product_name=product_name)

if __name__ == '__main__':
    app.run(debug=True)
