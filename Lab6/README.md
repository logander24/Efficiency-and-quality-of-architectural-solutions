Рефакторинг коду
    Цей репозиторій містить перероблені версії наданого коду для усунення дублювання коду та покращення зручності обслуговування.
    
    output_1.py
    Проблеми з оригінальним кодом
        Оригінальний код мав дві функції, `calculate_total_price` і `calculate_total_price_with_tax`, які містили повторювану логіку для розрахунку загальних цін зі знижкою та без неї.
    
    Рішення для рефакторингу
        Перероблена версія об’єднує загальні функції в одну функцію, `calculate_total_price`, яка може обробляти обидва випадки за допомогою додаткового параметра для ставки податку.

    def calculate_total_price(product_prices, discount, tax_rate=0):
        def apply_discount(price):
            return price * 0.9 if discount else price

        total_price = sum(apply_discount(price) for price in product_prices)
        return total_price * (1 + tax_rate)

    Цей підхід усуває повторюваний код і полегшує його підтримку та розширення в майбутньому.

    output_2.py
        Оригінальний код
            Клас `DataAnalyzer` у вихідному коді вже був добре структурований і не містив жодного повторюваного коду, який потребував рефакторингу.

        Структура коду
            Клас використовує приватний метод `_calculate_total_and_count` для інкапсуляції логіки обчислення загальної суми та кількості елементів даних. Цей метод повторно використовується в інших публічних методах, забезпечуючи чистий та ефективний дизайн.

    class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None

Ця структура гарантує, що код є модульним, простим для розуміння та підтримки.

    Висновок
        Перероблений код у `output_1.py` і `output_2.py` демонструє найкращі практики для усунення дублювання коду та покращення зручності обслуговування коду. Завдяки консолідації загальної функціональності та забезпеченню модульного дизайну оновлений код стає чистішим, ефективнішим і простішим у обслуговуванні.