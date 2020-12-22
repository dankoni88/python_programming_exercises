"""
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98
"""


def get_list_and_tuple_out_of_a_sequence(sequence):
    list_of_values = [x for x in sequence.split(',')]
    tuple_of_values = tuple(list_of_values)
    print(list_of_values)
    print(tuple_of_values)


def main():
    sequence = input("Enter a sequence of values: ")
    get_list_and_tuple_out_of_a_sequence(sequence)


if __name__ == '__main__':
    main()
