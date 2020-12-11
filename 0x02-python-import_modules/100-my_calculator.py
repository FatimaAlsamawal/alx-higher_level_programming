#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv
    numb1 = int(argv[1])
    numb2 = int(argv[3])
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] is "+":
        print(add(numb1, numb2))
    elif argv[2] is "-":
        print(sub(numb1, numb2))
    elif argv[2] is "*":
        print(mul(numb1, numb2))
    elif argv[2] is "/":
        print(div(numb1, numb2))
