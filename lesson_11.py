#Meri
# import random
# import readchar

# n = int(input('n: '))

# monkey_emojy = '🙉'
# monkey_row = random.randint(1,n)
# monkey_column = random.randint(1,n)

# banana_em = '🍌'
# banana_row = random.randint(1,n)
# banana_column = random.randint(1,n)

# bomb_emojy = '💣'
# bomb_row = random.randint(1,n)
# bomb_column = random.randint(1,n)

# heart = ' ❤️ '

# zombi = '🧟'
# zombie_row = random.randint(1,n)
# zombie_column = random.randint(1,n)

# astx = ' ⭐ '

# miavorner = 0
# kyanqer = 5

# while True:
#     print()
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i == monkey_row and j == monkey_column :
#                 print(monkey_emojy, end = '\t')
#             elif i == banana_row and j == banana_column :
#                 print(banana_em, end = '\t')
#             elif miavorner >= 3 and i == bomb_row and j == bomb_column:
#                 print(bomb_emojy, end = '\t')
#             elif miavorner >= 5 and i == zombie_row and j == zombie_column:
#                 print(zombi, end = '\t')
#             else:
#                 print('*', end = '\t')
#         print()

#     print(kyanqer * heart)
#     print(miavorner*astx)
#     print('W|A|S|D')

#     if kyanqer == 0:
#         print('GAME OVER 💀')
#         break
#     elif miavorner == 10:
#         print('YOU WON 🏆')
#         print(f'YOU HAVE {miavorner} coins')
#         break

#     step = readchar.readkey().lower()
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
#             monkey_row += 1

#     if miavorner >= 5:
#         zombie_row = random.randint(1,n)
#         zombie_column = random.randint(1,n)

#     if monkey_row == banana_row and monkey_column == banana_column :
#         miavorner += 1
#         banana_row = random.randint(1,n)
#         banana_column = random.randint(1,n)

#     if monkey_row == bomb_row and monkey_column == bomb_column and miavorner >= 3:
#         kyanqer -= 1
#         bomb_row = random.randint(1,n)
#         bomb_column = random.randint(1,n)

#     if monkey_row == zombie_row and monkey_column == zombie_column and miavorner >= 5:
#         kyanqer -= 1



#Arman
# import random
# import readchar
# # import readchar.readkey().lower()input('N: '))
# hp = '❤️ '
# hp_amount = 5
# score = 0

# n = int(input('N: '))

# fish_emoji = '🐟'
# fish_row = random.randint(1, n)
# fish_column = random.randint(1, n)

# worm_emoji = '🪱'
# worm_row = random.randint(1, n)
# worm_column = random.randint(1, n)

# kart_emoji = '🎣'
# kart_row = random.randint(1, n)
# kart_column = random.randint(1, n)

# while (kart_row == fish_row and kart_column == fish_column) or \
#       (kart_row == worm_row and kart_column == worm_column):

#     kart_row = random.randint(1, n)
#     kart_column = random.randint(1, n)

# shark_emoji = '🦈'
# shark_row = random.randint(1, n)
# shark_column = random.randint(1, n)

# while (shark_row == fish_row and shark_column == fish_column) or \
#       (shark_row == worm_row and shark_column == worm_column) or \
#       (shark_row == kart_row and shark_column == kart_column):

#     shark_row = random.randint(1, n)
#     shark_column = random.randint(1, n)

# row = 1
# col = 1

# while True:
#     print()

#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == worm_row and j == worm_column:
#                 print(worm_emoji, end='\t')
#             elif i == fish_row and j == fish_column:
#                 print(fish_emoji, end='\t')
#             elif score >= 3 and i == kart_row and j == kart_column:
#                 print(kart_emoji, end='\t')
#             elif score >= 10 and i == shark_row and j == shark_column:
#                 print(shark_emoji, end='\t')
#             else:
#                 print('*', end='\t')
#         print()

#     print('W|S|A|D')
#     print(hp_amount * hp, end='  ')
#     print('score =', score)

#     step = readchar.readkey().lower()
#     if step == 'q':
#         break
#     elif step == 'a':
#         if fish_column == 1:
#             fish_column = n
#         else:
#             fish_column -= 1
#     elif step == 's':
#         if fish_row == n:
#             fish_row = 1
#         else:
#             fish_row += 1
#     elif step == 'd':
#         if fish_column == n:
#             fish_column = 1
#         else:
#             fish_column += 1
#     elif step == 'w':
#         if fish_row == 1:
#             fish_row = n
#         else:
#             fish_row -= 1
#     if score >= 10:
#         shark_row += row
#         shark_column += col
#         if shark_row == n or shark_row == 1:
#             row *= -1
#         if shark_column == n or shark_column == 1:
#             col *= -1
#     if fish_column == worm_column and fish_row == worm_row:
#         score += 1
#         worm_row = random.randint(1, n)
#         worm_column = random.randint(1, n)

#         while (worm_row == fish_row and worm_column == fish_column) or \
#               (worm_row == kart_row and worm_column == kart_column) or \
#               (worm_row == shark_row and worm_column == shark_column):
#             worm_row = random.randint(1, n)
#             worm_column = random.randint(1, n)

#     if fish_column == kart_column and fish_row == kart_row:
#         score -= 1
#         hp_amount -= 1
#         kart_row = random.randint(1, n)
#         kart_column = random.randint(1, n)

#         while (kart_row == fish_row and kart_column == fish_column) or \
#               (kart_row == worm_row and kart_column == worm_column) or \
#               (kart_row == shark_row and kart_column == shark_column):
#             kart_row = random.randint(1, n)
#             kart_column = random.randint(1, n)

#     if score >= 10 and fish_column == shark_column and fish_row == shark_row:
#         score -= 5
#         hp_amount -= 2
#         shark_row = random.randint(1, n)
#         shark_column = random.randint(1, n)

#         while (shark_row == fish_row and shark_column == fish_column) or \
#               (shark_row == worm_row and shark_column == worm_column) or \
#               (shark_row == kart_row and shark_column == kart_column):
#             shark_row = random.randint(1, n)
#             shark_column = random.randint(1, n)

#     if hp_amount == 0:
#         print()
#         print('GAME OVER')
#         break




#Harut
# import readchar
# import random

# n=int(input("n:"))
# scores=0
# hp=3

# monkey_emoji="🐵"
# monkey_row=random.randint(1,n)
# monkey_column=random.randint(1,n)

# banana_emoji="🍌"
# banana_row=random.randint(1,n)
# banana_column=random.randint(1,n)

# bomb_emoji="💣"
# bomb_row=random.randint(1,n)
# bomb_column=random.randint(1,n)

# zombie_emoji="🧟"
# zombie_row=random.randint(1,n)
# zombie_column=random.randint(1,n)

# while True:
#     print()
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==monkey_row and j==monkey_column:
#                 print(monkey_emoji,end="\t")
#             elif i==banana_row and j==banana_column:
#                 print(banana_emoji,end="\t")
#             elif scores>=3 and i==bomb_row and j==bomb_column:
#                 print(bomb_emoji,end="\t")
#             elif scores>=5 and i==zombie_row and j==zombie_column:
#                 print(zombie_emoji,end="\t")
#             else:     
#                 print("*",end="\t")
#         print()          
#     print("❤️  " * hp)
#     print("⭐" * scores)
#     print(f'{zombie_emoji} - [{zombie_row} - {zombie_column}]')
#     print(f'{monkey_emoji} - [{monkey_row} - {monkey_column}]')
#     print(f'{bomb_emoji} - [{bomb_row} - {bomb_column}]')
#     print(f'{banana_emoji} - [{banana_row} - {banana_column}]')

#     print("W|A|S|D")
#     step=readchar.readkey()
#     step=step.lower()
#     if  step=="q":
#         break
#     elif step=="a":
#         if monkey_column==1:
#            monkey_column=n 
#         else:
#             monkey_column-=1
#     elif step=="d":
#         if monkey_column==n:
#            monkey_column=1
#         else:
#            monkey_column+=1
#     elif step=="w":
#         if monkey_row==1:
#            monkey_row=n
#         else:
#            monkey_row-=1
#     elif step=="s":
#         if monkey_row==n:
#            monkey_row=1
#         else:
#            monkey_row+=1

#     if monkey_row==banana_row and monkey_column==banana_column:
#        scores+=1
#        banana_row=random.randint(1,n)
#        banana_column=random.randint(1,n)
#     elif monkey_row==bomb_row and monkey_column==bomb_column and scores>=3:
#         hp-=1
#         bomb_row=random.randint(1,n)
#         bomb_column=random.randint(1,n)
#     elif monkey_row==zombie_row and monkey_column==zombie_column and scores>=5:
#          hp-=1
#          zombie_row=random.randint(1,n)
#          zombie_column=random.randint(1,n)
#     else:
#         zombie_move = random.choice("adws") 
#         print(zombie_move)
#         if zombie_move=="a":
#             if zombie_column == 1:
#                 zombie_column = n
#             else:
#                 zombie_column -= 1
#         elif zombie_move == "d":
#             if zombie_column == n:
#                 zombie_column = 1
#             else:
#                 zombie_column += 1
#         elif zombie_move == "w":
#             if zombie_row == 1:
#                 zombie_row = n
#             else:
#                 zombie_row -= 1
#         elif zombie_move == "s":
#             if zombie_row == n:
#                 zombie_row = 1
#             else:
#                 zombie_row += 1



#Albert
# import readchar
# import random
# n = int(int(input('N :')))
# scores =0
# hp = 3
# monkey_emoji= '🐒'
# monkey_row = random.randint(1, n)
# monkey_column = random.randint(1,n)
# banan_emoji = '🍌'
# banan_row = random.randint(1, n)
# banan_column=random.randint (1,n)
# bobm_emoji = '💣'
# bomb_row = random.randint(1, n)
# bomb_column = random.randint(1, n)
# zombi_emoji = '🧟'
# zombi_row = random.randint(1,n)
# zombi_column= random.randint(1,n)
# heart_emoji = '❤️'
# heart_row = random.randint(1,n)
# heart_column= random.randint(1,n)

# while True:
#     print()
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i ==monkey_row and j == monkey_column:
#                 print(monkey_emoji,  end= '\t')
#             elif i ==banan_row and j ==banan_column:
#                 print(banan_emoji, end='\t')
#             elif scores >=3 and i ==bomb_row and j==bomb_column:
#                 print(bobm_emoji, end= '\t')
#             elif scores>=5 and i ==zombi_row and j ==zombi_column:
#                 print(zombi_emoji, end='\t')
#             elif scores>=5 and i==heart_row and j==heart_column:
#                 print(heart_emoji, end='\t')
#             else:
#                 print('*', end= '\t')        
#         print()
#     print(' ❤️ ' * hp)
#     print('⭐' * scores)

#     print('W|A|S|D')
#     step = readchar.readkey()
#     step=step.lower()
#     if step =='q':
#         break
#     elif step=='a':
#         if monkey_column==1:
#             monkey_column=n
#         else:
#             monkey_column-=1
#     elif step =='d':
#         if monkey_column==n:
#             monkey_column=1
#         else:
#             monkey_column+=1
#     elif step =='w':
#         if monkey_column==1:
#             monkey_row = n
#         else:
#             monkey_row-=1
#     elif step =='s':
#         if monkey_row ==n:
#             monkey_row=1
#         else:
#             monkey_row+=1

#     if monkey_row == banan_row and monkey_column == banan_column:
#         scores+=1
#         banan_row = random.randint(1,n)
#         banan_column= random.randint(1, n)
#     elif monkey_row== bomb_row and monkey_column== bomb_column and scores>=3:
#         hp -=1
#         bomb_row = random.randint(1,n)
#         bomb_column= random.randint(1, n)
#     elif monkey_row==zombi_row and zombi_column== monkey_column and scores >=5:
#         hp -=2
#         zombi_row = random.randint(1,n)
#         zombi_column= random.randint(1, n)
#     elif scores >=5 and monkey_row==heart_row and monkey_column==heart_column:
#         hp+=1
#         heart_row = random.randint(1,n)
#         heart_column= random.randint(1, n)

#     if hp == 0:
#         print('Game Over')
#         break

#     zombi_step = random.choice('awsd')
#     zombi_step = zombi_step.lower()
#     if zombi_step=='a':
#         if zombi_column==1:
#             zombi_column=n
#         else:
#             zombi_column-=1
#     elif zombi_step =='d':
#         if zombi_column==n:
#             zombi_column=1
#         else:
#             zombi_column+=1
#     elif zombi_step =='w':
#         if zombi_column==1:
#             zombi_row = n
#         else:
#             zombi_row-=1
#     elif zombi_step =='s':
#         if zombi_row ==n:
#             zombi_row=1
#         else:
#             zombi_row+=1


#Anahit
# import readchar
# import random

# n=int(input("enter n: "))

# monkey_emoji="🐵"
# monkey_row=random.randint(1,n)
# monkey_column=random.randint(1,n)

# banana_emoji="🍌"
# banana_row=random.randint(1,n)
# banana_column=random.randint(1,n)

# miavorner=0
# kyanqer=3

# bomb_emoji='💣'
# bomb_row=random.randint(1,n)
# bomb_column=random.randint(1,n)

# granny_emoji="👵"
# granny_row=random.randint(1,n)
# granny_column=random.randint(1,n)

# while True:
#     print("\n")
#     print(" ⭐ " * miavorner)
#     print(" ❤️ " * kyanqer)
#     print()

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==monkey_row and j==monkey_column:
#                 print(monkey_emoji, end="\t")

#             elif i==banana_row and j==banana_column:
#                 print(banana_emoji, end='\t')

#             elif  miavorner>=3 and i==bomb_row and j==bomb_column:
#                 print(bomb_emoji, end="\t")

#             elif miavorner>=5 and i==granny_row and j==granny_column:
#                 print(granny_emoji, end="\t")
    
#             else:
#                 print('*', end='\t')
#         print()
        
#     print("W/S/A/D")
#     step_1=readchar.readkey()
#     if step_1=="w":
#         if monkey_row==1:
#             monkey_row=n
#         else:
#             monkey_row-=1

#     elif step_1=='s':

#         if monkey_row==n:
#             monkey_row=1
#         else:
#             monkey_row+=1

#     elif step_1=='a':

#         if monkey_column==1:
#             monkey_column=n
#         else:
#             monkey_column-=1

#     elif step_1=='d':

#         if monkey_column==n:
#              monkey_column=1
#         else:
#             monkey_column+=1

#     else: 
#         break
    
#     if banana_row==monkey_row and banana_column==monkey_column:
#         miavorner+=1
#         # print(f'\n miavorner={miavorner}')
#         banana_row=random.randint(1,n)
#         banana_column=random.randint(1,n)

#     if miavorner>=3 and monkey_row==bomb_row and monkey_column==bomb_column:
#         kyanqer-=1
#         # print(f'\n kyanqer={kyanqer}')
#         bomb_row=random.randint(1,n)
#         bomb_column=random.randint(1,n)

#     if miavorner>=5 and monkey_row==granny_row and monkey_column==granny_column:
#         kyanqer-=1
#         # print(f'\n kyanqer={kyanqer}')
#         granny_row=random.randint(1,n)
#         granny_column=random.randint(1,n)

#     if miavorner>=5:
#         granny_row=random.randint(1,n)
#         granny_column=random.randint(1,n)

#     if miavorner==10:
#         print("\n You won!! ")
#         break
    
#     if kyanqer==0:
#         print("\n You lose!! ")
#         break



#Aro

# elements = (7,)
# print(type(elements))
# elements = 7, 8, 9
# print(elements)
# info = ('Arsen', 67, ('Macbook', 14))


# list_ = []
# x = list()


# list_ = [1, 2, 3, 'Arsen', 'Vahe', ['Ar', 'Gv', 124]]
# for i in list_:
#     print(i)

# numbers = [10, 5, 6, 3, 4, 1]
# numbers.sort(reverse=True)
# print(numbers)

# text = 'Python'
# text = text.upper()
# print(text)

# numbers = ['a', 'o', 'v', 'g']
# numbers.sort(reverse=True)
# print(numbers)

# numbers = ['Arsen', 'Vahe', 'is','are', 'Arman', 'Albert', 'Arayik', 'Anahit', 'Meri', 'Harut']
# numbers.sort(key=len, reverse=True)
# print(numbers)
# print(numbers[1:])

# numbers = [20, 1, 4, 5, 3, 6]
# numbers.append(7)
# numbers.insert(1, 'OK')
# numbers.append(['a', 'b', 'k'])
# print(numbers[6][1])
# numbers.extend(['a', 'b', 'k'])
# print(numbers)
# y = ['a', 'b', 'c']
# z = numbers + y
# print(z)

# x = [1, 2, 3]
# y = x
# x.append(4)
# print(y)

# x = [1, 2, 3]
# y = x.copy()
# y = list(x)
# y = x[::]
# y = x[:]
# x.append(5)
# print(x)
# print(y)

# from copy import deepcopy
# x = [1, 2, 3, [4, [5], 6]]
# y = deepcopy(x)
# x[0] = 6
# x[3][1][0] = 6
# print(x)
# print(y)

# x = [1, 2, 3, 4]
# deleted_element = x.pop()
# print(x)
# print(deleted_element)
# x.pop()
# x.pop(0)
# x.remove(3)
# del x[1:]
# x.clear()
# x = []
# maximum_element = max(x)
# minimum_element = min(x)
# summ = sum(x)
# print(maximum_element)
# print(minimum_element)
# print(summ)


# words = ['is', 'are', 'erkar bar', 'medium', 'large']
# longest_word = max(words, key=len)
# shortest_word = min(words, key=len)
# print(longest_word)
# print(shortest_word)


# list_ = [None]
# new_list = list_ * 5
# print(new_list)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Version 1
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append(i)

# print(new_list)

#Version 2
# new_list = [i for i in list_ if i % 2 == 0]
# new_list = ['Zuyg' if i % 2 == 0 else 'Kent' for i in list_]
# print(new_list)

# list_ = [[1], [2, 3], [4, 5], [6, 7], [8, 9], [10]]
# new_list = []
# for i in list_:
#     for j in i:
#         new_list.append(j)

# print(new_list)


# new_list = [i for element in list_ for i in element]
# print(new_list)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(list_)):
#     print(i, list_[i])


# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c', 'd']
# for i, j in zip(l1, l2):
#     print(i, j)


# l1 = [1, 2, 3, 4, 5, 6 ,7 ]
# for i, e in enumerate(l1):
#     print(i,e)

# l1 = [1, 2, 3, 4, 5, 2, 2, 6 ,7 ]
# print(l1.count(2))
# print(l1.index(2))


# text = 'p y t h o n'
# words = text.split(' ')
# print(words)
# word = '++++'.join(words)
# print(word)

