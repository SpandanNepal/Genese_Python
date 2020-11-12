def list_sum():
    lst = [3, 4, 5, 1, 2, 8, 7, 6, 5, 6, 7]  # OR lst = input("Enter a list")
    total = 0

    for item in lst:
        total += item

    print("list" + str(lst))
    print('sum = ' + str(total))
    print()


def common_list_elements():
    a = [1, 1, 3, 7, 9, 9]  # OR a = input("Enter list a")
    b = [2, 1, 6, 9, 2, 1, 3, 5]  # OR b = input("Enter list b")

    common = list(set(a).intersection(set(b)))
    print(a)
    print(b)
    print("common elements between two lists are:")
    print(common)
    print()


def len_string():
    inp_str = input("Enter a String:")
    counter = 0

    for i in inp_str:
        counter += 1

    print("Length of " + inp_str + " is: " + str(counter))
    print()


def main():
    list_sum()
    common_list_elements()
    len_string()


if __name__ == '__main__':
    main()
