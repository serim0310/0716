# 연습문제 8
list = [[100, 200], [400, 800], [1000, 1400]]

for i in list :
    num = 0
    for j in i :
        num = num + j

    print(num / len(i))