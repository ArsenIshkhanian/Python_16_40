#Version 1
# a = 0
# b = 1
# c = a + b

# n = int(input('N: '))
# for i in range(n):
#     print(a, end=' ')
#     a = b
#     b = c
#     c = a + b


#Version 2
# a = 0
# b = 1

# n = int(input('N: '))
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


# a = 5
# b = 3
# c = a + b # 8
# a = c - a # 3
# b = c - a # 5
# print(a, b)

# a = 5
# b = 3
# c = a * b
# a = c / a
# b = c / a
# print(a, b)

# a = 5
# b = 3
# a, b = b, a

# print(a, b)


# binary = input('Enter the binary number: ') # 1001
# print(binary)


# summ = 0 # 8
# for i in range(len(binary)): # 0, 1, 2, 3
#     summ += int(binary[i]) * 2**(len(binary) - 1 - i)

# print(summ)


# for i in range(10, 100):
#     i = str(i)
#     f = int(i[0])
#     s = int(i[1])
#     summ = f * s * 3


# x = 15
# x = str(x)


# print(int(x[0]) * int(x[1]))


# n = int(input('N: '))
# summ = n * (n + 1) / 2

# for i in range(n - 1):
#     haytni = int(input('haytni: '))
#     summ -= haytni

# print(int(summ))