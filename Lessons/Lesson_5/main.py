#a = input('Введите что-то')
#print(a.lower())
#if a.lower() == 'привет':
#   print('Приветики')



#names = ['Pavel', 'Jordan', 'Uguz', 'Asil']
#names1 = [spam + ' krutoy' for spam in names]
#print(names1)




#name = 'Pasha'
#n = [x for x in name]
#print(n)




#my_list = [1, 'a', 2, 4.5]
#my = [i + 2 for i in my_list]
#print(my)




#my = ['22', '33', 'Jordan', 'Pavel']
#my2 = [i + '2' for i in my]
#print(my2[1:3])



# nums = [ i for i in range(1,11)]
# chotniye = [nums for nums in nums if nums %2 == 0]
# nichotniye = [nums for nums in  nums if nums %2 != 0]
#
# print(chotniye, nichotniye)




# names = ['Betman', 'Sups', 'Uguz', 'Khon']
# answer = [i[0] for i in names]
# print(answer)



# numms = [1,2,3]
# my_list = [i for i in range(1,11) if i in numms]
# print(my_list)



# nums1 = [ i for i in range(1,21)]
# nums2 = [nums1 for nums1 in nums1 if nums1 %2 == 0]
# print(nums1, '    ', nums2)



# users = []
# while True:
#     names = input('Enter username: ')
#     if names in users:
#         print(input('It have in users'))
#     elif names.lower() == 'список':
#         print(users)
#     else:
#         users.append(names)
#         print('Added')
#         print(users)
#
#
#
#






a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


c = [nums for nums in a if a==b]
print(c)



















