# x = 5
# y = 4
# print(x > y)

# x = int(input('Enter the x: '))
# y = int(input('Enter the y: '))
# if x > y:
#     print('x is max')
# elif x < y:
#     print('y is max')
# else:
#     print('x == y')


# x = int(input('Enter the x: '))
# y = int(input('Enter the y: '))

# if x > y:
#     print('mtav if')
#     if x < 10:
#         print('y < 10')
#     elif y > 10:
#         print('y >10')
#     else:
#         print('inch vor mi ban')
# elif x < y:
#     print('y is max')
# else:
#     print('x == y')



# exanak = input('Exanak: ').lower()
# if exanak == 'andzrev':
#     print('Mna tany python ara!')
# elif exanak == 'arev':
#     bassein = input('Karoxa bassein gnas ? ').lower()
#     if bassein == 'ayo':
#         tex = input('Ures uzum gnas? ').lower()
#         if tex == '20kopek':
#             print('Lav chashak unes axpers')
#         elif tex == 'jrashxarh':
#             print('De qez lav or')
#         elif tex == 'dvin':
#             print('Ari im hetevic')
#         else:
#             print('De gna')
#     else:
#         avto_lav = input('Karoxa avton lavanas? ').lower()
#         if avto_lav == 'ayo':
#             print('Tuyn axpers')
#         else:
#             print('Inch anhaves lakot durs ekar')
# else:
#     print('De taq khagnves!!')



# import random
# import time

# name = input('Enter your name: ')
# status = input('Are you ready(ayo/voch)? ').lower()
# if status == 'ayo':
#     user_score = 0
#     comp_score = 0
#     print(3)
#     time.sleep(0.7)
#     print(2)
#     time.sleep(0.7)
#     print(1)
#     time.sleep(0.7)
#     print("Let's Go")
#     comp_number = random.randint(1, 5)
#     user_number = int(input('Guess the number from 1 to 5: '))
#     if user_number == comp_number: # es 1 comp 0
#         user_score += 1
#         print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#         print(f"{name} = {user_score} / comp = {comp_score}")
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Guess the number from 1 to 5: '))
#         if user_number == comp_number: # es 2 comp 0
#             user_score += 1
#             print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#             print(f"{name} = {user_score} / comp = {comp_score}")
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Guess the number from 1 to 5: '))
#             if user_number == comp_number:# es 3 comp 0
#                 user_score += 1
#                 print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | {name} WIN!!!!')
#             else: #es 2 comp 1
#                 comp_score += 1
#                 print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | {name} WIN!!!!')
#         else: # es 1 comp 1
#             comp_score += 1
#             print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#             print(f"{name} = {user_score} / comp = {comp_score}")
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Guess the number from 1 to 5: '))
#             if user_number == comp_number: # es 2 comp 1
#                 print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | {name} WIN!!!!')
#             else: # es 1 comp 2
#                 comp_score += 1
#                 print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | Comp WIN!!!!')
#     else: # es 0 comp 1
#         comp_score += 1
#         print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#         print(f"{name} = {user_score} / comp = {comp_score}")
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Guess the number from 1 to 5: '))
#         if user_number == comp_number: # es 1 comp 1
#             user_score += 1
#             print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#             print(f"{name} = {user_score} / comp = {comp_score}")
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Guess the number from 1 to 5: '))
#             if user_number == comp_number: # es 2 comp 1
#                 user_score += 1
#                 print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | {name} WIN!!!!')
#             else: # es 1 comp 2
#                 comp_score += 1
#                 print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | Comp WIN!!!!')
#         else: # es 0 comp 2
#             comp_score += 1
#             print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#             print(f"{name} = {user_score} / comp = {comp_score}")
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Guess the number from 1 to 5: '))
#             if user_number == comp_number:  # es 1 comp 2
#                 user_score += 1
#                 print(f"{name} jan you win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | Comp WIN!!!!')
#             else: # es 0 comp 3
#                 comp_score += 1
#                 print(f"Comp win this round! {name} - {user_number} | comp - {comp_number}")
#                 print(f"{name} = {user_score} / comp = {comp_score}")
#                 print(f'End Game!!! | Comp WIN!!!!')
# else:
#     print('Du gites.')



# letter = input('Enter the letter: ')
# vowels = 'aeiou'
# if letter in vowels:
#     print('dzynavor e')
# else:
#     print('baghadzayn e')

# age = input()
# if age < 2:
#     pass
# elif age < 16:
#     pass

# age = input('age: ')

# age = eval(input('age: '))
# print(type(age))

# if 0 < age < 2:
#     print(age)

#     if age < 2

# age = 'avs'
# if not age.isdigit():
#     print(f'age-y tar e')
# print(age.isdigit())


# age = eval(input('Enter the age: '))
# salary = eval(input('Salary: '))
# print(salary)


# age = int(input('Enter the age: '))
# name = input('Name: ')

# if name:
#     print(name)
# else:
#     print('Mi ban gri')


# if age:
#     print(age)
# else:
#     print('Not valid')

# print(age.isdigit())

# if age.isdigit():
#     age = int(age)


# number_1 = input() 
# number_2 = input()

# if number_1.replace('.', '').isdigit() and number_2.replace('.', '').isdigit():
#     print('mtav stex')
#     number_1 = float(number_1)
#     number_2 = float(number_2)

# print(number_1)
# print(number_2)


