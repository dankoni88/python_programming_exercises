"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also, include simple test function to test the class methods.
"""


class StringConverter():
    def __init__(self):
        self.string = ""

    def get_string(self) -> str:
        self.string = input("Insert a string: ")

    def print_upper_case_string(self) -> str:
        print(self.string.upper())


def main():
    converter = StringConverter()
    converter.get_string()
    converter.print_upper_case_string()


if __name__ == '__main__':
    main()
