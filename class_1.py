def swap(list, i,j):
    list[i], list[j] = list[j], list[i]
    

my_list = [5, 2, 3, 1, 4 ]

def bubble_sort(list):
    for _ in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                swap(list, j, j+1)

    print(list)

bubble_sort(my_list)
