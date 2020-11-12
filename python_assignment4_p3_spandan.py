def prime():
    print("prime numbers from 1 to 100:")
    for i in range(1, 101):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i, end=" ")
    print('\n')


def palindrome():
    str_inp = input("Enter a string:")
    if str_inp == str_inp[::-1]:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")
    print()


def letter_occurance():
    dic = {}
    str_inp = input("Enter a string: ")
    for i in str_inp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)


def main():
    prime()
    palindrome()
    letter_occurance()


if __name__ == '__main__':
    main()
