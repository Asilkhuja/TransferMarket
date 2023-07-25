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
#    names = input('Enter username: ')
#    if names in users:
#        print(input('It have in users'))
#    elif names.lower() == 'список':
#        print(users)
#    else:
#        users.append(names)
#        print('Added')
#        print(users)



# my = ['1', '33','Jordan', 'Pasha']
# my2 = [i+'2' for i in my if 'o' in i]
# print(my2)


# my = [i for i in range(1,11,2)]
# print(my)



# names = ['Sasha', 'Masha', 'Gosha', 'Gora']
# names2 = [i[0] for i in names]
# print(names2)


# nums = [i for i in range(1,21)]
# nums_2 = [i for i in range(1,21) if i %2 == 0]
# print(nums, nums_2)


# usersnames = ['Asil', 'Maruf']
# again = bool(True)
# while True:
#     names = input('Add name: ')
#     if names in usersnames:
#         print('This name has already added!')
#     elif names.lower() == 'список':
#         print(usersnames)
#     else:
#         usersnames.append(names)
#         print('Added')
#         print(usersnames)
#     again = input('Continue?')
#     if again == 'yes':
#         again = True
#     else:
#         print('finished')
#         break