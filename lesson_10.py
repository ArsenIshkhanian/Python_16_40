# n = int(input('N: '))
# max_sum = 0
# max_num = 0
# for i in range(n):
#     number = int(input('Enter the number: '))
#     number_copy = number
#     summ = 0
#     while number >= 10:
#         summ += number % 10
#         number //= 10
#     summ += number
#     print(f'{number_copy} -> {summ}')
#     if summ > max_sum:
#         max_sum = summ
#         max_num = number_copy

# print(f'MAX is {max_num} -> {max_sum}')



# n = int(input('N: '))

# for i in range(1, n + 1):
#     for j in range(1, n + i):
#         if j >= n + 1 - i:
#             print('#', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# number = 1
# n = int(input('N: '))
# for i in range(1, n + 1):
#     for j in range(1, n + i):
#         if j >= n + 1 - i:
#             if (i + j) % 2 == 0: 
#                 print(number, end='  ')
#                 number += 2
#             else:
#                 print('  ', end='  ')
#         else:
#             print('  ', end='  ')
#     print()


#version - 1
# n = int(input("N: "))
# number = n
# for i in range(1, n+1):
#     for j in range(1, i + 1):
#         print(number, end=' ')
#         number -= 1

#     for k in range(2*(n - i)):
#         print('*', end=' ')

#     for t in range(i):
#         number += 1
#         print(number, end=' ')
#     print()


#version - 2
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, 2 * n + 1):
#         if j <= i:
#             print(n + 1 - j, end=' ')
#         elif j > 2 * n - i:
#             print(j - n, end=' ')
#         else:
#             print('.', end=' ')
#     print()



# n = int(input('N: '))
# for i in range(1, n + 1):
#     number = 0
#     for j in range(1, n + i):
#         if j >= n + 1 - i:
#             if j > n:
#                 number -= 1
#                 print(number, end=' ')
#             else:
#                 number += 1
#                 print(number, end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# import msvcrt
# while True:
#     print('W|S|A|D')
#     # step = msvcrt.getch()


#     if step == 'q':
#         break

# import random
# import readchar

# n = int(input('N: '))

# scores = 0
# hp = 3

# monkey_emoji = '🐵'
# monkey_row = random.randint(1, n) 
# monkey_column = random.randint(1, n) 

# banan_emoji = '🍌'
# banan_row = random.randint(1, n) 
# banan_column = random.randint(1, n) 

# bomb_emoji = '💣'
# bomb_row = random.randint(1, n) # 5
# bomb_column = random.randint(1, n) # 6

# while True:
#     print()
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == monkey_row and j == monkey_column:
#                 print(monkey_emoji, end='\t')
#             elif i == banan_row and j == banan_column:
#                 print(banan_emoji, end='\t')
#             elif scores >= 3 and i == bomb_row and j == bomb_column:
#                 print(bomb_emoji, end='\t')
#             else:
#                 print('*', end='\t')
#         print()
#     print('❤️ ' * hp)
#     print('⭐' * scores)


#     print('W|A|S|D')
#     step = readchar.readkey() 
#     step = step.lower()
#     if step == 'q':
#         break
#     elif step == 'a':
#         if monkey_column == 1:
#             monkey_column = n
#         else:
#             monkey_column -= 1
#     elif step == 'd':
#         if monkey_column == n:
#             monkey_column = 1
#         else:
#             monkey_column += 1
#     elif step == 'w':
#         if monkey_row == 1:
#             monkey_row = n
#         else:
#             monkey_row -= 1
#     elif step == 's':
#         if monkey_row == n:
#             monkey_row = 1
#         else:
#             monwkey_row += 1

#     if monkey_row == banan_row and monkey_column == banan_column:
#         scores += 1
#         banan_row = random.randint(1, n)
#         banan_column = random.randint(1, n) 
#     elif monkey_row == bomb_row and monkey_column == bomb_column and scores >= 3:
#         hp -= 1
#         bomb_row = random.randint(1, n) 
#         bomb_column = random.randint(1, n) 