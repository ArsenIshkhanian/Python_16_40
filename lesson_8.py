# hours = 3
# current = 1
# summ = 0
# go_to_shop = False

# while current <= hours:
#     count = int(input('How many tasks did you solve? '))
#     summ += count
#     status = input('Answer the call or no(yes/no)? ')
#     if status == 'yes':
#         go_to_shop = True
#     current += 1

# if go_to_shop:
#     print('Kmtnes xanut anpayman!!!!!')
# print(summ)



# import math

# number = int(input('Enter the number between 0-100: '))
# steps = 1
# minimum = 0
# maximum = 100
# while minimum <= maximum:
#     guessed_number = math.ceil((maximum + minimum) / 2)
#     answer = input(f'Is your number {guessed_number} ?(less/more/yes): ').lower()
#     if answer == 'yes':
#         print(f'I guessed your number with {steps} steps')
#         break
#     elif answer == 'less':
#         maximum = guessed_number - 1
#     else:
#         minimum = guessed_number + 1

#     steps += 1


# import random
# comp_number = random.randint(1, 100)
# # print(comp_number)
# user_number = int(input('Guess the number: '))
# steps = 1
# while user_number != comp_number:
#     if user_number > comp_number:
#         print('poqra')
#     else:
#         print('metsa')
#     user_number = int(input('Guess the number: '))
#     steps += 1
# print(f'I guessed your number with {steps} steps')


# n = int(input('N: '))
# for i in range(n):
#     for j in range(n): 
#         print('*', end=' ')
#     print()


# n = int(input('N: '))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# n = int(input('N: '))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i % 2 == 0 and j % 2 == 0:
#             print('#', end=' ')
#         elif i % 2 == 1 and j % 2 == 1:
#             print('#', end=' ')
#         else:
#             print('.', end=' ')
#     print()



# n = int(input("N: "))
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if((i+j) % 2 == 0):
#             print("#", end = " ")
#         else:
#             print(".", end = " ")
#     print()


# n = int(input('N: '))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j > n + 1:
#             print('.', end=' ')
#         else:
#             print('#', end=' ')
#     print()