list = [2,5,3,0,2,3,0,3]

counter = [0] * (max(list) + 1)
# print(counter)

for i in list:
    counter[i] += 1

j = 0
for i in range(len(counter)):
    count = counter[i]
    counter[i] += j
    j += count

output_list = [0] * len(list)
for x in list:
    output_list[counter[x]] = x
    counter[x] -= 1

print(counter)
print(output_list)
