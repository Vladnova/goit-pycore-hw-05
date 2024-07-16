import re
from typing import Callable, Generator

def generator_numbers(text: str)->Generator[float, None, None]:

    pattern = r'(?<=\s)-?\d+\.\d+(?=\s)|(?<=\s)-?\d+(?=\s)'
    
    list_numbers_type_str = re.findall(pattern, text)
    
    for num_type_str in list_numbers_type_str:
        yield float(num_type_str)


def sum_profit(text: str, gen_num:Callable[[str], Generator[float, None, None]])->float:
    return sum(gen_num(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

