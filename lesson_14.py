# numbers = [4, 2, 4, 1, 2, 4, 3]
# # data = {i: numbers.count(i) for i in numbers}
# data = {}
# for i in numbers:
#     if i in data:
#         data[i] += 1
#     else:
#         data[i] = 1

# print(data)

# max_value = 0
# max_count = 0

# for i in data:
#     if data[i] > max_count:
#         max_count = data[i]
#         max_value = i

# print(f'Amenashaty {max_value}-a {max_count} hat')


# numbers = [2, 7, 3, 6, 11, 15]
# target = 9
# data={}

# for i in numbers:
#     if (target-i) in numbers:
#         print(i, target-i)
#     else:
#         data[i]=True



# numbers = [2, 6, 5, 7]
# target = 9
# data = {}

# for i in numbers:
#     if (target - i) in data:
#         print(target - i, data[target - i])
        
#     else:
#         data[i] = target - i



# data = {}

# while True:
#     name = input('Enter your name: ').capitalize()
#     if name == 'Q':
#         break
#     email = input('Enter your mail: ').lower()
#     password = input('Enter your password: ')
#     data[name] = {
#         'email': email,
#         'password': password
#     }
# for name in data:
#     print(f"{name} -> {data[name]['email']} {data[name]['password']}")



# data = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }

# word = input('Word: ').upper() #Hello
# for letter in word:
#     for key in data:
#         if letter in data[key]:
#             count = data[key].index(letter) + 1
#             print(key * count, end=' ')


# data = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }

# word = input('Word: ').upper()
# summ = 0
# for letter in word:
#     for key in data:
#         if letter in data[key]:
#             summ += key
# print(summ)



# elements = {}
# elements = set()
# print(type(elements))

# elements = {5, 4, 2}
# print(elements)
# print(type(elements))


# x = {1, 2, 3, 4, 5, 6}
# y = {7, 8, 9}

# x.pop()
# print(x)
# print(2 in x)
# x.add(6)
# x.add(6)
# x.discard(6)
# x.remove(4)
# print(x.issuperset(y))
# print(y.issubset(x))
# print(x.intersection(y))
# print(y.isdisjoint(x))
# print(x.isdisjoint(y))
# print(x.difference(y))
# print(y.difference(x))
# x.update(y)
# y.update(x)
# print(x)
# print(y)
# print(x)
# list_ = [1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5]
# uniques = set(list_)
# print(uniques)


# def mult_table():
#     for i in range(1, 11):
#         for j in range(1, 11):
#             print(i * j, end='\t')
#         print()

# for i in range(10):
#     mult_table()


# def inchvor():
#     print(10)


# print(inchvor())


# def inchvor():
#     return 10

# x = inchvor()
# print(x * 5)
# print(10 * 5)


# def mult_table():
#     for i in range(1, 11):
#         for j in range(1 ,11):
#             print(i * j, end=' ')
#         print()
# mult_table()



# def armat(tiv=0):
#     return tiv ** 0.5

# print(armat())



# def astichan(tiv, astichan, animast_tiv):
#     return tiv ** astichan
# x = 3
# y = 2
# z = astichan(astichan=x, tiv=y, animast_tiv=10)
# print(z)



# def liqy_arg(*args):
#     print(args)

# liqy_arg(1, 1, 1, 2, 3, 4, 5, 6, 7, 8)


# def liqy_arg(*args, **kwargs):
#     print(args)
#     print(kwargs)

# liqy_arg(1, 1, 1, 2, 3, 4, 5, 6, 7, 8, arsen=13, harut=11)


# def mult_return(x1, x2):
#     add = x1 + x2
#     diff = x1 - x2
#     return add, diff
# y, z = mult_return(10, 6)


# import inchvor
# print(inchvor.armat(25))


# def f1(a):
#     a = a * 2
#     def f2(a, b):
#         return a + b
#     return f2(a, a + 2)

# print(f1(4))


# x = 5
# def y():
#     global x
#     x += 2
#     print(x)

# print(x)
# y()


# def y():
#     x = 5
# y()
# print(x)

# x = lambda a, b: a + b
# print(x(5, 6))


# def is_prime(tiv: int) -> bool:
#     pass

# list_ = [14, 5, 3, 4, 1, 109, 247]
# def filter(elements: list) -> list:
#     filtered_list = []
#     for i in elements:
#         if is_prime(i):
#             filtered_list.append(i)

#     return filtered_list


# def info(name, /, age, company='Microsoft'):
#     print(name, age, company)

# info('arsen', 14)


# def y(a, b):
#     return a + b
# x = y(4, 5)
# print(x)
