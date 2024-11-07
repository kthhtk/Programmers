str = input()

# 첫번째 코드
# print(str)

# 참고 코드
str = input()
while True :
    if 1 <= len(str) <= 1000000 and str != ' ' :
        print(str)
        break
    else :
        continue
