import re
from typing import Callable


def generator_numbers(text: str): #провожу typing
    numbers = r"(\d+\.\d+)" #виконую прегулярний вираз для виділення тільки чисел з плаваючою крапкою
    number_finding = re.findall(numbers, text) #виконую пошук їх у тексті за допомогою re.findall
    yield [float(nums) for nums in number_finding] #перетворюю список на числа у генераторі


def sum_profit(text: str, func: Callable):
    number_finding = func(text) # передаю функцію з текстом у generator_numbers
    total_income = sum(*number_finding) # рахую загальну суму всіх чисел які створилися в генераторі у функції generator_numbers
    return total_income #повертаю занальну суму,вже пораховану

#провожу інпут даних у функцію,та рахую загальну суму доходу
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
