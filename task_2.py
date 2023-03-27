'''
Погружение в Python (семинары)
Урок 5. Интераторы и генераторы
Задание 2.
Напишите однострочный генератор словаря, который принимает на вход три списка 
одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
'''
# Первая фаза для понимания: Семинар 4. Погружение в Python. Функции Задание №5 

def func(names: list[str], salaries: list[int], cash_prizes: list[str]) -> dict[str, float]:
    if len({(l := len(names)), len(salaries), len(cash_prizes)}) != 1:
        raise ValueError(f'Lengths of all three lists must be the same!!!')
    return {names[i]: (salaries[i] * float(cash_prizes[i].split('%')[0]) / 100) for i in range(l)}

# Три входящих списка согласно условия Задания 2: 

names_ = ['Vadik', 'Svetlana', 'Dmitry', 'Ivan', 'Roman']
salaries_ = [100000, 50000, 900000, 250000, 500000]
cash_prizes_ = ['10.25', '19.88', '125.98', '55.52', '101.88']

print(f'dictionary from function : {func(names_, salaries_, cash_prizes_)}')

print('')

# Вторая фаза в соответствии с этим заданием 2 Урок 5. Интераторы и генераторы: 
# упрощенно без проверок на соответсвие длин входящих списков

one_line_dictionary = {names_[i]: (salaries_[i] * float(cash_prizes_[i].split('%')[0]) / 100) for i in range(len(names_))}
print(f'one line dictionary: {one_line_dictionary}')