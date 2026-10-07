# dic = {}
# while True:
#     name = input("Enter your name: ")
#     if name == "q":
#         break
#     email = input("Enter you email: ")
#     password = input("Enter your password: ")

#     dic[name] = {
#         'email': email,
#         'password': password
#     }
# for name in dic: #
#     print(f'{name} -> {dic[name]['email']}, {dic[name]['password']}')



# def maximum(elements):
#     maximum_element = 0
#     for element in elements:
#         if element > maximum_element:
#             maximum_element = element
#     return maximum_element

# print(maximum([17, 3, 1, 3, 90, 104]))



# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n%i==0:
#             return False
#     return True

# def primes_between(start, end):
#     mylist = []
#     for element in range(start, end + 1):
#         if is_prime(element):
#             mylist.append(element)

#     return mylist


# print(primes_between(10, 30))



# def compress(text):
#     new_str = ''
#     count = 1
#     for index in range(len(text) - 1):
#         if text[index] == text[index + 1]:
#             count += 1
#         else:
#             new_str += f'{text[index]}{count}'
#             count = 1

#     new_str += f'{text[-1]}{count}'
#     return new_str

# print(compress('aaabbccccdaa'))