Рефакторинг: AdvancedCalculator і LibraryBookManager

    Частина 1: AdvancedCalculator
        Опис
            Клас `BasicCalculator` містив лише базові методи додавання та віднімання. Щоб додати функціональність множення та ділення, було створено підклас `AdvancedCalculator`.

        Зміни
            1. Додано методи `multiply` та `divide` до `AdvancedCalculator`.
            2. Початковий клас `BasicCalculator` залишено незмінним.

        Переваги
            - Збільшена функціональність калькулятора.
            - Початковий клас залишається простим і без змін.

    Частина 2: LibraryBookManager
        Опис
            Клас `LibraryBook` надавав базові методи для роботи з бібліотечними книгами, але бракувало додаткової функціональності. Для цього був створений клас `LibraryBookManager`, який додає нові методи.

        Зміни
            1. Додано метод `get_book_info` для отримання інформації про книгу.
            2. Додано метод `check_condition` для перевірки стану книги.
            3. Початковий клас `LibraryBook` залишено незмінним.

        Переваги
            - Збільшена функціональність для роботи з бібліотечними книгами.
            - Початковий клас залишається простим і без змін.

    Висновок
        Рефакторинг покращив дизайн і функціональність коду, зберігаючи початкові класи незмінними та додавши нові можливості через підкласи та делегування.
