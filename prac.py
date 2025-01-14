# foods=("fried rice","fried chiken","beef","mutton","mixed vegetables")

# # for food in foods:
# #     # print(food)
# #     print(f"Our item: {food}")

# # foods[2] = "water"

# foods = ("fried rice","fried chiken","mutton","mixed vegetables", "water")
# for food in foods:
#     print(f"Our item: {food}")

# print(foods[3:5])


# infoDict = { "Bangladesh":"Dhaka",
# "India":"Delhi",
# "Pakistan": "Islamabad",
# "Srilanka":"Colombo",
# "Nepal":"Kathmandu"}

# print(infoDict)
# print(len(infoDict))
# print(infoDict["Bangladesh"])
# print(infoDict["Srilanka"])


# roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

# print(roman_numerals)
# print(roman_numerals['I'])
# print(roman_numerals['X'])

# print(roman_numerals.get("IV", "Not found"))

# # del roman_numerals['III']
# print(roman_numerals)
# if "III" in roman_numerals:
#     print(roman_numerals["Afganistan"])
# else:
#     print("Not in the dictionary")

# phone_numbers = {"Musfique": "01711111111", "Rahim": "01722222222", "Karim": "01733333333"}
# phone_numbers = {'My name': '00000000000'}

# phone_numbers["My name"] = "11111111111"

# print(phone_numbers)


# phone_book={
#     "Sajid":"01797592987",
#     "Farah":"01741537509",
#     "Dona":"01926280343",
#     "Shushmi":"01926280343"
# }


# for name,number in phone_book.items():
#     print(f"Good Morning {name}, here is your cell number {number}")




# for name in phone_book.keys():
#     print(f"How are You {name}")



# for number in phone_book.values():
#     print(f"Your Number is {number}")



# for number in set( phone_book.values()):
#     print(f"Your Number is {number}")


# lst = [1,1,2,3,4,4,5]
# print(lst)
# print(set(lst))




# list of dicts

# person_1 = {"Name": "Sajid", "Age": 23}
# person_2 = {"Name": "Umaiya", "Age": 22}
# person_3 = {"Name": "Musfique", "Age": 24}

# persons = [person_1, person_2, person_3]

# for person in persons:
#     # for name, age in person.items():
#     #     print(f"{name} : {age}")
#     for value in person.values():
#         print(value, end=" :")
#     print()

# info = {
#     "Name": ["Sajid","Anik","Umaiya"], 
#     "Age":[23,24,22]
#     }


# for value in info.values():
#     for i in value:
#         print(i)



# info = {
#     "Name": {"Sajid":"ok","Anik":"ok","Umaiya":'not ok'}, 
#     "Age":{2:3,2:4,2:2}
#     }

# for value in info.values():
#     for key, val in value.items():
#         print(key, val)



# person_1 = {"Name_1": "Sajid", "Age_1": 23}
# person_2 = {"Name": "Umaiya", "Age": 22}
# person_3 = {"Name": "Musfique", "Age": 24}

# dict = {**person_1, **person_2}
# print(dict)

# lst = [1,2,3]

# lst[2] = 4 #miutable
# print(lst)

# tpl = (1,2,3)

# tpl[2] = 4#unmiutable
# print(tpl)


# upozilla_map = {
#     "Dighinala": ['Panchari', 'Khagrachari'], 
#     "Panchari": ['Khagrachari', 'Dighinala', 'Mati Ranga'], 
#     "Khagrachari": ['Dighinala', 'Panchari', 'Mati Ranga', 'Ramgarh', 'Mohla Chari'], 
#     "Mati Ranga": ['Panchari', 'Khagrachari', 'Ramgarh'], 
#     "Ramgarh": ['Mati Ranga', 'Khagrachari', 'Mohal Chari', 'Lakshmichari', 'Manikchari'], 
#     "Mohla Chari": ['Khagrachari', 'Ramgarh', 'Lakshmichari'], 
#     "Manikchari": ['Ramgarh', 'Lakshmichari'], 
#     "Lakshmichari": ['Manikchari', 'Ramgarh', 'Mohal Chari'], 
# }

# # max = 0
# # min = 100

# # for upozilla, neighbor in upozilla_map.items():
# #     neigh_num = len(neighbor)
# #     print(f"{upozilla} has {neigh_num} neighbors.")

# #     if neigh_num < min:
# #         min = neigh_num

# #     if neigh_num > max:
# #         max = neigh_num


# # print(max)
# # print(min)


# # for upozilla, neighbor in upozilla_map.items():
# #     if len(neighbor) == max:
# #         print(f"{upozilla} has maximum neibors!")
# #     if len( neighbor) == min:
# #         print (f"{upozilla} has minimum neibors!")


# strng = "ABRAKAdabra"
# strng = strng.lower()

# dct = {}

# for i in strng:
#     if i in dct.keys():
#         dct[i] += 1
#     else:
#         dct[i] = 1

# print(dct)


# print(f'{17.4897429837:.5f}')

# from decimal import Decimal
# print(f'{Decimal("10000000000000000000000000.0"):.3f}')
# print(f'{Decimal("10000000000000000000000000.0"):.3e}')


# print(f'[{27:10d}]')
# print(f'[{3.5:10f}]')
# print(f'[{"hello":10}]')

# s1 = 'happy'
# s2 = 'birthday'
# s1 += ' ' + s2
# s1 = s1+ " " + s2

# print(s1)
# symbol = '>'
# symbol *= 5
# print(symbol)



# sentence = '\t \n This is a test string. \t\t \n'
# print(sentence)
# print(sentence.strip())
# print(sentence.rstrip())
# print(sentence.lstrip())
# print('strings: a deeper look'.title())
# # print('happy birthday'.capitalize())
# print('Orange' == 'orange')
# print('Orange' != 'orange')
# print('Orange' < 'orange')
# print('Orange' <= 'orange')
# print('Orange' > 'orange')
# print('Orange' >= 'orange')

# sentence = 'to be or not to be that is the question'
# print(sentence.count('to', 12))

# sentence = 'to be or not to be that is the question'
# print(sentence.index('be'))
# sentence = 'to be or not to be that is the question'
# print('THAT' in sentence)
# print('that' in sentence)
# print('THAT' not in sentence)
# print(sentence.startswith('to'))
# print(sentence.endswith('question'))
# letters_list = ['A', 'B', 'C', 'D']
# print(','.join(letters_list))
# print('Amanda: 89, 97, 92'.partition(': '))



# def myFunc():
#     print("i am fine")

# myFunc()

# def myFunc(dress):
#     print("she is beautiful in",dress)
# myFunc("shirt")
# myFunc("jeans")

# def phone(n):
#     return(n*n)
# sq=phone(8)
# print(sq)
# print(phone(90))

# hih = 10 # local variable

# def myFunc(x, hi):
#     # hih = hih + 12 # error
#     #para += 1
#     sum = 0
#     for i in range(x):
#         sum += i
#     return f"{hi}{sum}"
# n = myFunc(6, "the number is")
# print(n)


# def my_func(x):
#     mult = 1
#     for i in range(x):
#         mult *= i
#     return mult

# m = my_func(3)
# print(m)
# def infoCountry(country, capital):
#     print("The capital of",country,"is",capital)
# infoCountry("Dhaka","Bangladesh")


# def infoCountry(country, capital):
#     print("The capital of",country,"is",capital)
# infoCountry(capital="Dhaka",country="Bangladesh")

def infoCountry(country, capital='unknown'):
    print("The capital of",country,"is",capital)
infoCountry("India")

def infoCountry(country, capital='unknown'): #default value : 'unknown'
    print("The capital of",country,"is",capital)
infoCountry("India",  "new delhi")