n = int(input())
list_a = []
for i in range(n):
    list_a.append(int(input()))

set_a = set(list_a)
b = sorted(set_a)

for num in b:
    print(num)
