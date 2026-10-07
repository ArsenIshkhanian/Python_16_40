# import time

# n = int(input('N: ')) # 10

# for i in range(n, 0, -1):
#     time.sleep(1)
#     status = input('Heriqa te che(ayo/voch)? ')
#     if status == 'ayo':
#         print(f'Patrasta uteliqy! mikorvalnokayin der kar {i - 1} vayrkyan')
#         break


#x**3 + 2 * x**2 - 4 * x + 1

# start = int(input('Start: '))
# end = int(input('End: '))
# step = int(input('Step: '))

# for i in range(end, start - 1, step):
#     y = i**3 + 2 * i ** 2 - 4 * i + 1
#     print(f"{i} -> {y}")


# chap = int(input("Mutqagreq namaki koxmi erkarutyuny: "))
# count=0
# for i in range(chap):
#     if chap > 12:
#         count+=2
        # chap/=2
    # else:
    #     print(f"Crary petq e calel {count} angam")
    #     break



# grant=int(input("enter grant: "))
# expenses=int(input("enter expenses: "))
# sum=0
# for i in range(2,12):
#     sum+=(expenses-grant)
#     expenses *= 1.03
# print(sum)


# n = int(input('N: '))
# number = 1
# for i in range(1, n):
#     number += (-1**i) * (1 / 2**i)


# x = int(input("Mutqagreq x: "))

# ham = 1
# hayt = 1

# for i in range(1, 8):
#     ham *= x - (2 ** i - 1)
#     hayt *= x - (2 ** i)

# print(ham / hayt)



# boys = int(input('Boys: '))
# girls = int(input('Girls: '))

# if boys > 2 * girls or girls > 2 * boys:
#     print('Dzev chka')
# elif boys == girls:
#     print(4 * 'GB')
# elif boys > girls:
#     skzbic = (boys - girls)*"BGB"
#     print(f"{skzbic}{(girls - skzbic.count('G')) * 'BG'}")
# else:
#     skzbic = (girls - boys)* "GBG"
#     print(f"{skzbic}{(boys - skzbic.count('B')) * 'GB'}")


# for i in 'python':
#     print(i)

# for i in range(len('python')):
#     print(i)



# x = 5

# while x < 10:
#     print(x)
#     x += 1


# x = 1

# while x < 100:
#     print(x)
#     if x % 7 == 0:
#         # print(x)
#         break
#     x += 1


# x = int(input('X: '))
# summ = 0
# while x != 0:
#     x = int(input('X: '))
#     summ += x

# print(summ)


# while True:
#     name = input('Enter your name: ')
#     age = int(input('Enter you age: '))
#     if age:
#         break


# age = int(input('Age: ')) # 0

# while not age:
#     age = int(input('Enter you age: '))
#     print(age)
#     print(5 + 4)




# name = input('name: ')
# age = int(input('age: '))

# while name == '' or age <= 0:
#     print('Invalid values')
#     name = input('name: ')
#     age = int(input('age: '))


# import random

# print(random.choice('OP'))

# o_count = 0
# p_count = 0
# sequence = ''
# while o_count < 3 and p_count < 3:
#     x = random.choice('OP')
#     sequence += x
#     if x == 'O':
#         o_count += 1
#         p_count = 0
#     else:
#         p_count += 1
#         o_count = 0 

# print(sequence)