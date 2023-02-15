from math import sqrt

def isPrime(number):
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, int(number / 2) + 1, 1):
            if number % i == 0:
                return False

test = int(input())

for i in range(test):
    string = input()
    
    add = sum(int(i) for i in string)
    
    if isPrime(add):
        print("YES")
    else:
        print("NO")