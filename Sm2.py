# 1.1
# x = [-1, 4, 5, 8, -10, 20]
# y =int(input('введите число '))
# for i in x:
#     if i == y:
#         print(x.index(y))
    

# x = [-1, 4, 5, 8, -10, 20]
# y =int(input('введите число '))
# z =[]
# for i in x:
#     if abs(i - y) == 0:
#         print(x.index(i))
#     elif abs(i - y) > abs((i + 1) - y):
#         c = i
# print(c)
        

# calc 
# def gum(x, y):
#     return x + y

# def han(x, y):
#     return x - y

# def baz(x, y):
#     return x * y

# def baj(x, y):
#     return x / y

# s = input()
# for i in range(0, len(s)+1):
#     a = int(s[i])
#     b = s[i+1]
#     c = int(s[i+2])
#     if b == '+':
#         print(gum(x = a, y = c))
#     elif b == '-':
#         print(han(x = a, y = c))
#     elif b == '*':
#         print(baz(x = a, y = c))
#     elif b == '/':
#         print(gum(x = a, y = c))
#     else:
#         print('error')





# Write a python program to find max of two numbers.
# def func(x, y):
#     if x > y:
#         return f'{x} is max'
#     else:
#         return f'{y} is max'
# print(func(5, 6))



# Write a python program to sum all numbers
# def func(x, y):
#     return x + y
# print(func(7, 8))



# Write a python program to multiply all numbers
# def mult(x, y):
#     return x * y
# print(mult(7 , 8))


# 102
# def possword(ps):
#     while True:
#         n = 0
#         if len(ps) < 8:
#             print('strong')
#             continue
#         else:
#             if ps[0].isupper():
#                 for i in ps:
#                     if i.isdigit():
#                         n += 1
#             if n > 2:
#                 print('good')
#                 break
#             else:
#                 print('fals')
#                 break
            
# print(possword(ps = input('Enter your possword ')))


# def func(st1, st2):
#     st1 = ()
#     st2 = ()
#     if len(st1) < 6:
#         print(len(st1))
#     else:
#         for i in range(len(st1)+1):
#             if st1[i].isalpha() and st1[i+1].isalpha() and st1[i+2].isalpha():
#                 return 'ok'
#             if st1[i+3].isdigit() and st1[i+4].isdigit() and st1[i+5].isdigit():
#                 return 'ok'

# st1 = []
# import random as r
# def func(st1):
#     a = ('a', 'b' , 'c', 'd')
#     while True:
#         a = ('a', 'b' , 'c', 'd')
#         st1 = []
#         st1 = st1.append(r.choise(a))
#         if len(st1) < 6:
#             print(len(st1))
#         else:
#             for i in range(len(st1)+1):
#                 if st1[i].isalpha() and st1[i+1].isalpha() and st1[i+2].isalpha():
#                     return 'ok'
#                 if st1[i+3].isdigit() and st1[i+4].isdigit() and st1[i+5].isdigit():
#                     return 'ok'
# print(func(st1 = st1.append(r.a)))






import random as r
while True:
    c = 0
    q =0
    n = []
    st1 = []
    st1.append(r.choice('qwertyuioasdfghjzxcvbnm'))
    n.append(r.randint(0, 9))
    for i in n:
        if 'i'.isdigit():
            c += 1
        for j in st1:
            if 'j'.isalpha():
                q += 1
    if q == 3 and c == 3:
        print(n+st1)
        break

    


