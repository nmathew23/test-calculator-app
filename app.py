from calc_app import addition,subtraction,multiply
def main():
    print(" Welcome to the Calculator App")
    print("Select the below opti1on")
    user_input = int(input("""Please select below option:
                    1. Addition
                    2.Subtraction
                    3. Multiplication
                    """))
    a = eval(input("Please enter value 1: "))
    b = eval(input("Please enter value 2: "))

    if user_input == 1:
        print(addition(a,b))
    elif user_input == 2:
        print(subtraction(a,b))
    else:
        print(multiply(a,b))

if __name__ == "__main__":
    main()
