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

# def infoCountry(country, capital='unknown'):
#     print("The capital of",country,"is",capital)
# infoCountry("India")

# def infoCountry(country, capital='unknown'): #default value : 'unknown'
#     print("The capital of",country,"is",capital)
# infoCountry("India",  "new delhi")

# def maximum(l): # l = [1,2,3,4,5,6,7,1,2,3,4,5]
#     maxi = l[0] # maxi = 7    1, 2, 3,
#     for i in range(1,len(l)): # range(1,12) => (1-11)
#         if l[i] > maxi: # 2>1?, 3>2? 1>7?
#             maxi = l[i]

#     return maxi

# maxi = maximum([1,2,3,4,5,6,7,1,2,3,4,5]) # 7

# print("Maximum:",maxi)


# l = [1,2,3,4,5,6,7,1,2,3,4,5]
# for i in range(1,len(l)):
#     print(l[i])


# l = [1,2,3,4,5,6,7,1,2,3,4,5]
# print(l[ : : -2])















# # A
# def find_connected_components(n, adj):
#     visited = [False] * (n + 1)
#     components = []

#     def dfs(node):
#         stack = [node]
#         component = []
#         while stack:
#             v = stack.pop()
#             if not visited[v]:
#                 visited[v] = True
#                 component.append(v)
#                 for neighbor in adj[v]:
#                     if not visited[neighbor]:
#                         stack.append(neighbor)
#         return component

#     for i in range(1, n + 1):
#         if not visited[i]:
#             component = dfs(i)
#             components.append(component)

#     return components

# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     n = int(data[0])
#     m = int(data[1])
    
#     adj = [[] for _ in range(n + 1)]
#     index = 2
#     for _ in range(m):
#         a = int(data[index])
#         b = int(data[index + 1])
#         adj[a].append(b)
#         adj[b].append(a)
#         index += 2
    
#     components = find_connected_components(n, adj)
    
#     k = len(components) - 1
#     print(k)
    
#     for i in range(1, len(components)):
#         print(components[i-1][0], components[i][0])

# if __name__ == "__main__":
#     main()


# # B
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# class List:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def addToTail(self, val):
#         """Add a number to the end of the Linked List."""
#         new_node = Node(val)
#         if not self.head:  # If the list is empty
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def Print(self):
#         """Print the elements of the Linked List in normal order."""
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()

#     def PrintReverse(self):
#         """Print the elements of the Linked List in reverse order."""
#         def collect_reverse(node):
#             if not node:
#                 return []
#             return collect_reverse(node.next) + [node.data]

#         reverse_list = collect_reverse(self.head)
#         print(" ".join(map(str, reverse_list)))


# # Input and Execution
# n = int(input())  # Number of elements
# values = list(map(int, input().split()))  # Elements of the linked list

# # Create a linked list and add values to it
# linked_list = List()
# for value in values:
#     linked_list.addToTail(value)

# # Print the list in normal and reverse order
# linked_list.Print()
# linked_list.PrintReverse()



# # # C
# # def main():
# #     n = int(input())  
# #     stack = []

# #     for _ in range(n):
# #         operation = list(map(int, input().split()))
        
# #         if operation[0] == 1:  
# #             stack.append(operation[1])
# #         else:  
# #             if stack:
# #                 print(stack.pop())

# # if __name__ == "__main__":
# #     main()

# # # D
# # def is_valid_sequence(n, operations):
# #     stack_size = 0
# #     for op in operations:
# #         if op == 1:
# #             stack_size += 1
# #         else:  
# #             if stack_size == 0:
# #                 return False
# #             stack_size -= 1
# #     return True

# # def main():
# #     T = int(input())
# #     for _ in range(T):
# #         n = int(input())
# #         operations = list(map(int, input().split()))
# #         print("Valid" if is_valid_sequence(n, operations) else "Invalid")

# # if __name__ == "__main__":
# #     main()

# # # E
# # from collections import deque

# # def main():
# #     d = deque()
# #     n = int(input())
    
# #     for _ in range(n):
# #         op = input().split()
# #         if len(op) == 2:
# #             x = int(op[1])
# #             if op[0] == 'insert':
# #                 d.appendleft(x)
# #             else:
# #                 try:
# #                     d.remove(x)
# #                 except ValueError:
# #                     pass
# #         else:
# #             if op[0] == 'deleteFirst':
# #                 d.popleft()
# #             else:
# #                 d.pop()
    
# #     print(*d)

# # if __name__ == "__main__":
# #     main()


# # # F
# # import sys
# # from collections import deque

# # def main():
# #     input = sys.stdin.readline
# #     reverse = False
# #     q = deque()
    
# #     # Operation mapping
# #     ops = {
# #         "toFront": 1,
# #         "front": 2,
# #         "back": 3,
# #         "reverse": 4,
# #         "push_back": 5
# #     }
    
# #     for _ in range(int(input())):
# #         cmd = input().split()
# #         op = ops[cmd[0]]
        
# #         if op == 1:  # toFront
# #             q.append(int(cmd[1])) if reverse else q.appendleft(int(cmd[1]))
# #         elif op == 2:  # front
# #             if not q:
# #                 sys.stdout.write("No job for Ada?\n")
# #             else:
# #                 sys.stdout.write(f"{q.pop() if reverse else q.popleft()}\n")
# #         elif op == 3:  # back
# #             if not q:
# #                 sys.stdout.write("No job for Ada?\n")
# #             else:
# #                 sys.stdout.write(f"{q.popleft() if reverse else q.pop()}\n")
# #         elif op == 4:  # reverse
# #             reverse = not reverse
# #         else:  # push_back
# #             q.appendleft(int(cmd[1])) if reverse else q.append(int(cmd[1]))

# # if __name__ == "__main__":
# #     main()


# # # H
# # from collections import deque

# # def process_test_cases():
# #     t = int(input())  # Number of test cases
    
# #     for case in range(1, t + 1):
# #         n, m = map(int, input().split())  
# #         queue = deque()
        
# #         print(f"Case {case}:")
        
# #         for _ in range(m):
# #             command = input().strip().split()
            
# #             if command[0] == "pushLeft":
# #                 x = int(command[1])
# #                 if len(queue) < n:
# #                     queue.appendleft(x)
# #                     print(f"Pushed in left: {x}")
# #                 else:
# #                     print("The queue is full")
            
# #             elif command[0] == "pushRight":
# #                 x = int(command[1])
# #                 if len(queue) < n:
# #                     queue.append(x)
# #                     print(f"Pushed in right: {x}")
# #                 else:
# #                     print("The queue is full")
            
# #             elif command[0] == "popLeft":
# #                 if queue:
# #                     print(f"Popped from left: {queue.popleft()}")
# #                 else:
# #                     print("The queue is empty")
            
# #             elif command[0] == "popRight":
# #                 if queue:
# #                     print(f"Popped from right: {queue.pop()}")
# #                 else:
# #                     print("The queue is empty")

# # if __name__ == "__main__":
# #     process_test_cases()







class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else: self._insert(self.root, key)
            

    def _insert(self, parent, key):
        if key < parent.value:
            if parent.left is None:
                parent.left = Node(key)
            else : self._insert(self.root.left, key)
        else: 
            if parent.right is None:
                parent.right = Node(key)
            else: self._insert(self.root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        elif key < node.value:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
        
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value, end=" ")
            self.in_order(root.right)
        
    # def is_divisible(self, root, res):
    #     if root:
    #         if self.search(root.value*res):
    #             return root
    #         self.is_divisible(root.left, res)
    #         # if self.search(root.value*res):
    #         #     return root
    #         self.is_divisible(root.right, res)
    #     # else:
    #     #     print("False")

    def is_divisible(self, root, res):
        if root:
            # Check if the current node's value multiplied by `res` exists in the tree
            if self.search(root.value * res):
                return True
            # Recur for left and right subtrees
            if self.is_divisible(root.left, res):
                return True
            if self.is_divisible(root.right, res):
                return True
        return False  # Return False if no match is found



bt_1 = BinaryTree()
bt_1.insert(20)
bt_1.insert(4)
bt_1.insert(1)
bt_1.insert(9)
bt_1.insert(21)
# bt_1.insert(None)
bt_1.insert(30)
# if bt_1.is_divisible(bt_1.root, 5):
#     print("True")
# else: print("False")
print(bt_1.is_divisible(bt_1.root, 5))
print(bt_1.is_divisible(bt_1.root, 8))