import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярні вирази, щоб знайти числа.
    # Шаблон r'\b\d+\.\d+\b|\b\d+\b' шукає цілі числа або числа з крапкою,
    # які стоять окремо (оточені межами слів/пробілами).
    for match in re.finditer(r'\b\d+\.\d+\b|\b\d+\b', text):
        # Перетворюємо знайдений текст на число з крапкою і "віддаємо" через yield
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Створюємо змінну, де будемо накопичувати суму
    total_sum = 0
    
    # Викликаємо функцію-генератор і проходимо по кожному знайденому числу
    for number in func(text):
        total_sum += number
        
    return total_sum

# Наш текст для перевірки
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Розраховуємо прибуток
total_income = sum_profit(text, generator_numbers)

# Виводимо результат
print(f"Загальний дохід: {total_income}")