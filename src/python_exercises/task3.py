"""
With a given whole number n,
write a program to generate a dictionary that contains (i, i x i)
such that for a whole number between 1 and n (both included)
the program should print the dictionary.
"""


def square_dictionary(number):
    dictionary = {}
    for i in range(1, number + 1):  # {i : i*i for i in range(1, n+1)} dictionary comprehension
        dictionary[i] = i * i

    print(dictionary)


def main():
    number = 0
    while number <= 0:
        try:
            number = int(input("Enter a positive whole number: "))
        except ValueError:
            print("Entry must be whole and positive number, please try again.")
            number = 0
            continue
    square_dictionary(number)


if __name__ == '__main__':
    main()


