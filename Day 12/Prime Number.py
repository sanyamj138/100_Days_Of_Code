
def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter the Number you want to Check: "))

if isPrime(num):
    print('Prime Number')
else:
    print('Not Prime Number')