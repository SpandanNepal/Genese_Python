#Exercise 1
width =17
height = 12.0
delimiter = '.'

print("Exercise 1 Solution")
print("1. value of width/2 is " + str(width/2) + " and type is:")
print(type(width/2))
print("2. value of width/2.0 is " +str(width/2.0) + " and type is:")
print(type(width/2.0))
print("3. value of height/3 is " + str(height/3) + "and type is:")
print(type(height/3))
print("4. value of 1+2*5 is" + str(1 + 2 * 5) + "and type is:")
print(type(1+2*5))
print("5. value of delimiter*5 is" + str(delimiter*5) + "and type is:")
print(type(delimiter*5))
print("\n")

#Exercise 2
print("Exercise 2 Solution")
farenheit_temp = int(input("enter temperature in farenheit:"))
print(str(farenheit_temp)+ " Farenheit in degrees is " + str((farenheit_temp - 32) * (5/9)))
print("\n")

#Exercise 3
print("Exercise 3 Solution")
seconds_input = int(input("enter time in seconds:"))
print(str(int(seconds_input/60)) + " minutes and " + str(int(seconds_input%60)) + " seconds")
print("\n")

#Exercise 4
print("Exercise 4 Solution")
lst = [9,6,7,4,5,3,1,2,10,8]
print("Orginal List:" + str(lst))
print("length of list "+str(len(lst)))
print("element in first position:" + str(lst[0]))
print("element in fourth position:" + str(lst[3]))
print("\n")

#Exercise 5
print("Exercise 5 Solution")
lst = [9,6,7,4,5,3,1,2,10,8]
print("Orginal List:" + str(lst))
lst.pop()
print("After popping element" + str(lst))
lst.insert(len(lst), 101)
print("After inserting element" + str(lst))
lst.remove(101)
print("After removing element" + str(lst))