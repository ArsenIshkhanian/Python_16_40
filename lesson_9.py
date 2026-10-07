# n = int(input('N: '))
# for i in range(n):
#     number = int(input('number: '))
#     count = 0
#     for i in range(1,number + 1):
#         if number % i == 0:
#             count += 1
#     print(f'{number} -> {count} divisors')


# n = int(input('N: '))
# for i in range(2, n + 1):
#     summ = 0
#     for j in range(1, i):
#         if i % j == 0:
#             summ += j
#     if summ == i:
#         print(i)


# n = int(input('n: '))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n:
#             print('*', end=' ')
#         elif j == 1 or j == n:
#             print('*', end=' ')
#         elif i == j:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# n = int(input('N: '))
# for i in range(1, n):
#     print(f'{i} + {n - i} = {n}')

# n = int(input('n: '))
# print(5 - n)



# N = int(input("N: "))
# for i in range(0, N):
#     num = 1
#     for j in range(0,2*N):
#         if(j == N):
#             print(i+1, end = " ")
#         elif j >= N-i and j < N:
#             print(num,end=" ")
#             num+=1
#         elif j<=N+i and j > N:
#             num-=1
#             print(num, end = " ")
#         else:
#             print(" ", end = " ")
#     print()


# n = int(input('N: '))

# for i in range(n + 1):
#     for j in range(n + 1):
#         print(f'{i + 2*j:<4}', end='')
#     print()


# n = int(input('N: '))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()

n = int(input('N: ')) # 6
count = 0
for i in range(n):
    number = int(input('number: '))
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        count += 1
print(count)