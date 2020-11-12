def farenheit_to_degrees():
    farenheit_temp = int(input("enter temperature in farenheit:"))
    print(str(farenheit_temp) + " Farenheit in degrees is " + str((farenheit_temp - 32) * (5/9)))
    print("\n")


def second_to_hour():
    seconds_input = int(input("enter time in seconds:"))
    print(str(int(seconds_input/60)) + " minutes and " + str(int(seconds_input % 60)) + " seconds")
    print()


def list_index_length():
    lst = [9, 6, 7, 4, 5, 3, 1, 2, 10, 8]  # OR lst = input("Enter a list")
    print("Orginal List:" + str(lst))
    print("length of list "+str(len(lst)))
    print("element in first position:" + str(lst[0]))
    print("element in fourth position:" + str(lst[3]))
    print()


def list_operations():
    lst = [9, 6, 7, 4, 5, 3, 1, 2, 10, 8]  # OR lst = input("Enter a list")
    print("Orginal List:" + str(lst))
    lst.pop()
    print("After popping element" + str(lst))
    lst.insert(len(lst), 101)
    print("After inserting element" + str(lst))
    lst.remove(101)
    print("After removing element" + str(lst))


def main():
    farenheit_to_degrees()
    second_to_hour()
    list_index_length()
    list_operations()


if __name__ == '__main__':
    main()
