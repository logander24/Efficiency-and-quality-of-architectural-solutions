Пояснення рішення:
    1. Розділення обов'язків: Клас Product був розділений на три окремі класи, кожен з яких виконує конкретну задачу:
        - ProductInfo: Зберігає інформацію про продукт і відображає її.
        - ProductSearch: Виконує пошук продуктів за запитом.
        - ProductOrder: Обробляє замовлення на продукт.

    2. Зменшення залежностей: Кожен клас тепер має чітко визначену відповідальність і не залежить від інших класів. Це спрощує підтримку та розширення коду.

    3. Принцип єдиного обов'язку: Кожен клас відповідає лише за одну конкретну задачу, що робить код більш зрозумілим і легким для підтримки.