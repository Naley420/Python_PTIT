from itertools import permutations

number = input()

A = []

for i in number:
    A.append(i)
    
perm = permutations(A)

for i in list(perm):
    for x in i:
        print(x, end="")
    print()