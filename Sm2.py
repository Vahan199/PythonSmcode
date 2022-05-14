# 1.1
# x = [-1, 4, 5, 8, -10, 20]
# y =int(input('введите число '))
# for i in x:
#     if i == y:
#         print(x.index(y))
    

x = [-1, 4, 5, 8, -10, 20]
y =int(input('введите число '))
z =[]
for i in x:
    if abs(i - y) == 0:
        print(x.index(i))
    elif abs(i - y) > abs((i + 1) - y):
        c = i
print(c)
        