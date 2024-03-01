# Результати тестування

Тестування проводилось на однаковому массиві данних з різним розміром
`sizes = [100, 1000, 10000, 15000, 30000]`

Отримані результати:
### Insertion Sort:
* Size 100: 0.00035609991755336523 seconds
* Size 1000: 0.027654000092297792 seconds
* Size 10000: 3.082708499976434 seconds
* Size 15000: 6.431470500072464 seconds
* Size 30000: 21.18526820000261 seconds
### Merge Sort:
* Size 100: 0.00016380008310079575 seconds
* Size 1000: 0.0020623999880626798 seconds
* Size 10000: 0.02999080007430166 seconds
* Size 15000: 0.0341543999966234 seconds
* Size 30000: 0.07283309998456389 seconds
### Timsort:
* Size 100: 1.1899974197149277e-05 seconds (приблизно 0.0000146 секунд)
* Size 1000: 0.00012069998774677515 seconds
* Size 10000: 0.0016568999271839857 seconds
* Size 15000: 0.001982400077395141 seconds
* Size 30000: 0.011260700062848628 seconds

# Висновки

З результатів виконання можна зробити наступні висновки:

## Масштабування ефективності:

* Сортування вставками показує прийнятну продуктивність на невеликих масивах (до 1000 елементів), але його час виконання різко зростає зі збільшенням розміру вхідних даних через квадратичну часову складність (O(n²)). Це робить його непрактичним для великих датасетів.
* Сортування злиттям демонструє стабільно хорошу продуктивність на всіх розмірах датасетів завдяки своїй часовій складності O(n log n). Час виконання злегка зростає при збільшенні розміру вхідних даних, але значно менше, ніж у сортування вставками.
* Timsort (використовується в функції sorted Python) показує найкращу продуктивність на всіх розмірах датасетів. Час виконання зростає лінійно-логарифмічно, що робить його надзвичайно ефективним для будь-якого розміру даних.

## Адаптивність та оптимізація:

* Timsort є найбільш адаптивним до різних типів датасетів завдяки своїм оптимізаціям, які використовують переваги вже відсортованих сегментів даних. Це пояснює його перевагу в швидкості навіть на дуже великих масивах.

## Вибір алгоритму для практичного використання:

Для невеликих масивів або коли оптимізація за часом не є критичною, можна використовувати сортування вставками.
Сортування злиттям є хорошим вибором для великих масивів, де потрібна гарантована ефективність O(n log n), особливо якщо є обмеження на використання додаткової пам'яті.
Timsort є оптимальним вибором для великих масивів завдяки його високій продуктивності та ефективності в широкому спектрі ситуацій, особливо у випадках, коли вхідні дані містять частково відсортовані сегменти.
Ці висновки підкреслюють важливість вибору правильного алгоритму сортування в залежності від конкретного сценарію використання та розміру даних. Вони також пояснюють, чому Timsort вибрано як стандартний алгоритм сортування в Python.
