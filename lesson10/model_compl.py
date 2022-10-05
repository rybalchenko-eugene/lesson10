import math
from gui import menu, type_num, get_compl_numbers

def compl_calc():
    def sum():
        num1 = get_compl_numbers(1)
        num2 = get_compl_numbers(2)
        res1 = num1[0] + num2[0]
        res2 = num1[1] + num2[1]
        s = "Результат сложения = " + str(res1) + '+' + str(res2) + '*i'
        return s

    def subtr():
        num1 = get_compl_numbers(1)
        num2 = get_compl_numbers(2)
        res1 = num1[0] + num2[0]
        res2 = num1[1] + num2[1]
        s = "Результат вычитания = " + str(res1) + '+' + str(res2) + '*i'
        return s

    def mult():
        num1 = get_compl_numbers(1)
        num2 = get_compl_numbers(2)
        res1 = num1[0]*num2[0] - num1[1]*num2[1]
        res2 = num1[0]*num2[1] - num1[1]*num2[0]
        s = "Результат умножения = " + str(res1) + '+' + str(res2) + '*i'
        return s

    def div():
        num1 = get_compl_numbers(1)
        num2 = get_compl_numbers(2)
        return 'ЭТО ОЧЕНЬ СЛОЖНАЯ ФОРМУЛА ЧТОБЫ ПИСАТЬ ЕЕ ЗДЕСЬ'
        

    c = menu('комплексными')
    if c == '1':
        return sum()
    if c == '2':
        return subtr()
    if c == '3':
        return mult()
    if c == '4':
        return div()
    if c == '5':
        return

