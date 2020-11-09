# Problem 1
lst = [3, 4, 5, 1, 2, 8, 7, 6, 5, 6, 7]
total = 0

for item in lst:
    total += item

print("Problem 1 Solution:")
print(total)
print("\n")

# Problem 2
a = [1, 1, 3, 7, 9, 9]
b = [2, 1, 6, 9, 2, 1, 3, 5]

common = list(set(a).intersection(set(b)))

print("Problem 2 Solution:")
print(common)
print("\n")

# Problem 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Problem 3 Solution:")
for item in lst:
    print("Num:" + str(item) + " Square:" + str(item**2))
print("\n")

# Problem 4
print("Problem 4 Solution:")
inp_str = input("Enter a String:")
counter = 0

for i in inp_str:
    counter += 1

print("Length of " + inp_str + " is: " + str(counter))
print("\n")

# Problem 5
print("Problem 5 Solution:")
inp_str = input("Enter a String:")

print("Upper: " + inp_str.upper())
print("Lower: " + inp_str.lower())
