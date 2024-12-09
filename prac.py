n = int(input())
laptops = []

for i in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

laptops.sort()
alex_happy = True

for j in range(1,n):
    if laptops[j][1] > laptops[j-1][1]:
        alex_happy = False

if alex_happy:
    print("Happy Alex")
else:
    print("Poor Alex")