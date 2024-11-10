a, b = map(int, input().strip().split(' '))
# print(a + b)

while True :
    if all(-100000 <= i <= 100000 for i in (a, b)) : # while, break, else, continue 지워도 됨
        print(f'a = {a}')
        print(f'b = {b}')
        break
    else :
        continue
