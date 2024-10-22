from calc_app import addition,subtraction
def main():
    print(" Welcome to the Calculator App")
    print("Select the below opti1on")
    user_input = int(input("""Please select below option:
                    1. Addition
                    2.Subtraction
                    """))
    a = eval(input("Please enter value 1: "))
    b = eval(input("Please enter value 2: "))

    if user_input == 1:
        print(addition(a,b))
    else:
        print(subtraction(a,b))

if __name__ == "__main__":
    main()
