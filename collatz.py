#collatz checks if a number is odd (it multiplies the number by 3 then adds 1
# but if number is even it divides the number by 2
'''number = int(input("Enter your number: "))
print("Collatz Sequence: ",end = " ")
while number > 1:
    print(number, end = " ")
    if number % 2:
        number = 3 * number + 1
    else:
        number = number // 2
print(1)
trials = 0
while trials < 5:
    number = int(input("Enter your number: "))
    print("Collatz Sequence: ",end = " ")
    while number > 1:
        print(number, end = " ")
        if number % 2:
            number = 3 * number + 1
        else:
            number = number // 2
    print(1)
    trials += 1
'''
def collatz(n):
    while n > 1:
        print(n,end=' ')
        if(n % 2):
            n = 3 * n + 1
        else:
            n = n//2
    print(1,end='')
n = int(input("enter number:"))
print("sequence: ",end=' ')
collatz(n)

