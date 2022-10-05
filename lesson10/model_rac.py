import math


def output(res1, res2):
    nod = math.gcd(res1, res2)
    res1, res2 = res1/nod, res2/nod
    if res1 % res2 == 0:
        s = str(int(res1/res2))
    elif res1 > res2:
        s = str(int(res1//res2))
        s = s + ' целых, дробь ' + str(int(res1%res2)) + '/' + str(int(res2))
    else:
        s = str(int(res1)) + '/' + str(int(res2))
    s = "Результат = " + s
    return s

def inp(lst):
    
    num1 = list(map(int, lst[0].split('/')))
    if len(num1) ==1:
            num1.append(1)
    num2 = list(map(int, lst[1].split('/')))
    if len(num2) ==1:
            num2.append(1)
    t = [[1,1],[1,1]]
    return lst1    

def summ(lst):
    num1 = list(map(int, lst[0].split('/')))
    if len(num1) ==1:
            num1.append(1)
    num2 = list(map(int, lst[1].split('/')))
    if len(num2) ==1:
            num2.append(1)
    res1 = num1[0]*num2[1] + num2[0]*num1[1]
    res2 = num1[1]*num2[1]
    return output(res1, res2)

def subtr(lst):
    num1 = list(map(int, lst[0].split('/')))
    if len(num1) ==1:
            num1.append(1)
    num2 = list(map(int, lst[1].split('/')))
    if len(num2) ==1:
            num2.append(1)
    res1 = num1[0]*num2[1] - num2[0]*num1[1]
    res2 = num1[1]*num2[1]
    return output(res1, res2)

def mult(lst):
    num1 = list(map(int, lst[0].split('/')))
    if len(num1) ==1:
            num1.append(1)
    num2 = list(map(int, lst[1].split('/')))
    if len(num2) ==1:
            num2.append(1)
    res1 = num1[0]*num2[0]
    res2 = num1[1]*num2[1]
    return output(res1, res2)

def div(lst):
    num1 = list(map(int, lst[0].split('/')))
    if len(num1) ==1:
            num1.append(1)
    num2 = list(map(int, lst[1].split('/')))
    if len(num2) ==1:
            num2.append(1)
    res1 = num1[0]*num2[1]
    res2 = num1[1]*num2[0]
    return output(res1, res2)

