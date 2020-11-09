from fractions import Fraction
#Program 1
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i, end = " ")
print()

# Program 2
str_inp = input("Enter a string:")
if str_inp == str_inp[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
print()

# Program 3
str_inp = input("Enter a string:")
lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0
for i in str_inp:
    if i.islower():
        lower_count +=1
    elif i.isupper():
        upper_count +=1
    elif i.isdigit():
        digit_count +=1
    else:
        special_count +=1
print("Lower: " + str(lower_count) + "\nUpper: " + str(upper_count) + "\nDigit: " + str(digit_count) + "\nSpecial character: " + str(special_count))
print()

# Program 4
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N ):
    print(str(Fraction(1,i)) + " + ", end = "")
    sum += (1/i)
print(str(Fraction(1,N)))
print("Sum = " + str(sum))
print()

# Program 5
count = 1
for i in range(0, 5):
    for j in range(5, i, -1):
        print(" ", end = " ")
    for i in range(count):
        print("*", end=" ")
    count +=1
    print()
print()

# Program 6
dic = {}
str_inp = input("Enter a string: ")
for i in str_inp:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
print(dic)






