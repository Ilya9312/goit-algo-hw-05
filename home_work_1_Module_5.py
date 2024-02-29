def caching_fibonacci():
    cache = {} #створюю список кэш,для збереження значень які вже попадали у фібоначчі

    def fibonacci(number):
        nonlocal cache
        if number <= 0: #перевірка якщо число дорівнює нулю,то повертаємо 0
            return 0
        elif number == 1: #перевірка якщо число дорівнює 1,то повертаємо 1
            return 1
        elif number in cache: #перевірка якщо число вже є в словнику кєш,тоді повертаємо його
            return cache[number]

        cache[number] = fibonacci(number - 1) + fibonacci(number - 2) #виконуємо розрахунок чисел фібоначчі за допомогою формули f(n - 1) + f(n - 2)
        return cache[number] #повертаємо вже виконаний результат функції фібоначчі з розрахунками

    return fibonacci



# Проводимо інпут всії даних
fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
