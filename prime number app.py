number = int(input("please enter a number:"))
is_prime = True

if number == 1:
    print("this number is not prime number!!")
if number == 0:
    print("this number is not prime number!!")

for i in range(2,number):
    if number % i == 0:
        is_prime == False
        break
if is_prime:
    print("this number is a prime number")
else:
    print("this number is not a prime number")



