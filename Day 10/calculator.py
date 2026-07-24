
#calculator with functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/":div,
}
#print(operations[input("Enter operation: ")](4, 8))
def calculator():
    should_accumulater= True
    num1 = float(input("Enter a number: "))
    while should_accumulater:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation: ")
        num2 = float(input("Enter a number: "))
        answer=operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} ={answer} ")

        choice = input("Do you want to continue with answer ? (y/n): ")
        if choice == "y":
            num1=answer
        else:

            should_accumulater = False
            print("\n"*20)
            calculator()

calculator()