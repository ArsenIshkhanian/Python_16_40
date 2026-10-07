# nums = [1, 3, 4, 6, 8, 10]
# target = int(input("Enter target number: "))
# i = 0
# j = len(nums) - 1
# while i < j:
#     summ = nums[i] + nums[j]
#     if summ < target:
#         i += 1
#     elif summ > target:
#         j -= 1
#     else:
#         print(nums[i], nums[j])
#         break
# else:
#     print('Chka tenc tiv')


# nums = [4, 8, 2, 10, 6]
# maximum_element = 0
# for element in nums:
#     if element > maximum_element:
#         maximum_element = element
# print(maximum_element)



# nums = [4, 9, 2, 8, 9, 7]
# verjin = 0 # 4, 9
# naxaverjin = 0 # 0, 4
# for i in nums:
#     if i > verjin:
#         naxaverjin = verjin
#         verjin = i
#     elif i > naxaverjin and i != verjin:
#         naxaverjin = i
# print(naxaverjin, verjin)


# nums = [10, 3, 20, 8, 15]
# min_ = abs(nums[1] - nums[0])
# for i in range(len(nums)):
#     for j in range(len(nums[i:])):
#         if abs(nums[i] - nums[j] < min_):
#             min_ = abs(nums[i] - nums[j])
# print(min_)


# nums.sort() # [3, 8, 10, 15, 20] ->n logn
# min_dif = nums[1] - nums[0]
# for i in range(1, len(nums) - 1): # n
#     if nums[i + 1] - nums[i] < min_dif:
#         min_dif = nums[i + 1] - nums[i]

# print(min_dif)




# nums = [1, 3, 3, 7, 9]
# for i in range(len(nums) - 1):
#     if nums[i + 1] < nums[i]:
#         print(False)
#         break
# else:
#     print(True)


# a = [0, 3, 4, 5, 8]
# b = [1, 2, 3, 6, 7]
# i = 0
# j = 0
# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         i += 1
#     elif a[i] > b[j]:
#         j += 1
#     else:
#         print(a[i])
#         i += 1
#         j += 1


# nums = [2, 8, 15, 21, 30]
# target = 17

# min_dif = abs(target - nums[0])
# min_dig = nums[0]

# for i in range(1, len(nums)):
#     if abs(nums[i] - target) < min_dif:
#         min_dig = nums[i]
#         min_dif = abs(nums[i] - target)

# print(min_dig)




# data = {'a': 85, 'b': 64, 'c': 96}
# data = {'arsen': 'macbook', 'Vahe': 'HP', 'c': 96}
# data = {
#     'arsen': '65',
#     'Vahe': 87,
#     'Meri': 0,
# }

# data = {
#     'arsen': {
#         'username': 'arsen_08',
#         'password': "04308Ars"
#     },
#     'vahe': {
#         'username': 'vahe_00',
#         'password': '1241'
#     },
#     'Harut': 0
# }


# data = {
#     'b': 9,
#     'a': 0,
#     'd': -2,
#     'c': 8
# }
# print(data)
# print(data.keys())
# print(data.values())
# print(data.items())

# list_ = [('b', 9), ('a', 0), ('d', -2), ('c', 8)]
# print(dict(list_))

# for i in data:
#     print(i)

# for i in data.keys():
#     print(i)

# for i in data.values():
#     print(i)

# for key in data:
#     print(key, data[key])

# for key, value in data.items():
#     print(key, value)


# data = {
#     'b': 9,
#     'a': 0,
#     'd': -2,
#     'c': 8,
# }
# x = data.copy()
# x = dict(data)
# data['w'] = 98
# print(x)

# data['w'] = 90
# data['a'] = 98
# data.setdefault('c', 98)
# data.popitem()
# data.pop('a')

# print(data)


# print(dict.fromkeys([1, 2, 3], 'a'))

# data = {
#     'b': 9,
#     'a': 0,
#     'd': -2,
#     'c': 8,
#     'k': 10
# }
# print(data['k'])
# print(data.get('k', 'CHka tenc ban'))
# data.clear()
# data = {}

# x = {
#     'arsen': 100
# }
# data.update(x)
# x.update(data)
# print(data)
# print(x)


# summ = 0
# data = {
#     'b': 9,
#     'a': 0,
#     'd': -2,
#     'c': 8,
#     'k': 10
# }
# for i in data:
#     summ += data[i]
# print(summ)


data = {
    'b': 9,
    'a': 0,
    'd': -2,
    'c': 8,
    'k': 10
}
# data['w'] = '07213648761'

# print(sorted(data.values()))
# print(sorted(data, key=data.get))
# print({key: data[key] for key in sorted(data, key=data.get)})

# for i in data:
#     print(f'{i} -> {data[i]}')