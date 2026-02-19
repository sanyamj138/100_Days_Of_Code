
def isPrime(num):

    if num == 1 or num == 2:
        return True

    for i in range(1, int(num / 2)):
        if num % i == 0:
            return False
    return True

num = int(input("Enter the Number you want to Check: "))

if isPrime(num):
    print('Prime Number')
else:
    print('Not Prime Number')