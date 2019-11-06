import sys
import os

def print_hello():
    a = 'print_hello_string'
    b = 'print_hello_string_2'
    c = b
    print(a)
    print(b)
    return c

def new_func():
    print('hellooo')


if __name__ == "__main__":
    print_hello()
    print('else print else')

    print('Updated')

    print('Updated for other repo')