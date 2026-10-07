# notebooks = ['Mac', 'Lenovo', 'Samsung']
# print('Mac' in notebooks)


# password = input('Password: ')
# if len(password) >= 8:
#     count_d = 0
#     count_s = 0
#     for i in password:
#         if i.isdigit():
#             count_d += 1
#         elif not i.isalnum():
#             count_s += 1
#     if count_s >= 2 and count_d >= 2:
#         print('Strong Password')
#     else:
#         print('Weak Password')
# else:
#     print('Weak Password')


# password = input("password: ")
# special_chars = ('!', '@', '#', '$', '%', '&', '*')
# lenght_valid = len(password) >= 8

# count_d = 0
# for i in password:
#    if i.isdigit():
#       count_d += 1

# count_s = 0
# for i in password:
#    if i in special_chars:
#       count_s += 1

# if lenght_valid and count_d >= 2 and count_s >= 2:
#    print ("strong")
# else:
#    print("Weak")


# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# elements = link.split('=')
# print(elements[1])

# digits = input('Digits: ')
# elements = digits.split(' ')
# elements = [i for i in elements if int(i) % 2 == 0]
# final = ''.join(elements)
# print(final)

# list_ = [2, 4, 6, 8, 10, 3, 1, 5,12, 14]
# for i in list_[::-1]:
#     if i % 2 == 0:
#         list_.remove(i)
# print(list_)

# import random
# yntroxner = ['Arsen', 'Vahe', 'Arman', 'Albert', 'Arayik', 'Anahit', 'Meri', 'Harut']
# yntrvoxner = ['Arsen', 'Vahe', 'Arman', 'Albert', 'Arayik', 'Anahit', 'Meri', 'Harut']
# status = False
# while True:
#     yntrox = random.choice(yntroxner)
#     yntrvox = random.choice(yntrvoxner)

#     while yntrox == yntrvox:
#         if len(yntrvoxner) == 1:
#             status = True
#             break
#         yntrvox = random.choice(yntrvoxner)

#     if status:
#         yntroxner = ['Arsen', 'Vahe', 'Arman', 'Albert', 'Arayik', 'Anahit', 'Meri', 'Harut']
#         yntrvoxner = ['Arsen', 'Vahe', 'Arman', 'Albert', 'Arayik', 'Anahit', 'Meri', 'Harut']
#         status = False
#     else:
#         print(f'{yntrox} -> {yntrvox}')
#         yntroxner.remove(yntrox)
#         yntrvoxner.remove(yntrvox)

#     if yntrvoxner == []:
#         break


# lst=['anahit', 'aaaaaaaaaaa', 'pyhon', 'bbbbbbbbbbbbbbbbbbbbbb']
# lst.sort(key=len, reverse=True)
# print(lst[0])



# list_ = [5, 1, 2, 4, 6]
#[1, 5, 2, 4, 6]
#[1, 2, 5, 4, 6]
#[1, 2, 4, 5, 6]
#[1, 2, 4, 5, 6]

# for i in range(len(list_)):
#     status = True
#     for j in range(len(list_) - 1):
#         print(list_)
#         if list_[j] > list_[j + 1]:
#             list_[j], list_[j + 1] = list_[j + 1], list_[j]
#             status = False
#     if status:
#         break
# print(list_)



# list_ = [5, 1, 2, 4, 6, 2]

# for i in list_:
#     if list_.count(i) > 1:
#         print(i)
#         break

# list_.sort() #n * log2n

# for i in range(len(list_) - 1):  #n
#     if list_[i] == list_[i + 1]:
#         print(list_[i])
