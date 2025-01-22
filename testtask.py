def BlackAndWhite(n,k,line):
    black = 0
    white = 0

    results = []
    for i in line:
        if black == k:
            return black
        elif i=="B":
            black+=1
        else:
            white +=1
        if black + white == k:
            results.append(white)
            black = white = 0
    
    black = 0
    white = 0   
    for i in line[::-1]:
        if i=="B":
            black+=1
        else:
            white +=1
        if black + white == k:
            results.append(white)
            black = white = 0   

    return min(results)

try:
    t = int(input("Введите количество наборов входных данных :\n"))
    if t > 10**4:
        raise Exception()
except:
    raise Exception("Ошибка!\nЗначение должно представлять из себя целое число ,которое не превышает 10^4")
while t > 0:
    
    n = int(input("Введите длину строки :\n"))
    if n > 2*10**5:
        raise Exception("Число n должно быть меньше чем 2*10^5")
    
    k = int(input("Введите необходимое количество черных клеток в ряд  :\n"))
    if k > n:
        raise Exception("Число k не может превышать значение n")
    
    WB = input("Введите строку в формате :WBBWBBWW :\n")
    if len(WB) != n:
        raise Exception("Количество символов в строке должно совпадать со значением n")
    if len(WB.upper().replace("W",'').replace("B","")) > 0:
        raise Exception("Строка должна содержать только символы 'W' и 'B'")

    print(BlackAndWhite(n,k,WB.upper()))

    t -=1
