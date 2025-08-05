def get_calc_info():

    print(f"    --- Calulator---    ")
    print(f"Note: The supported operation of this calculator is performing; addition, substraction, division "
          f"\nmultiplication, exponential and squared root of numbers.")
    opperators =input("Enter the type of operation you are performing: ")

    if opperators in ["addition" , "Addition" , "+" , "Add" , "add"]:
        print(f"--- Performing Addition of Numbers ---")
        user_inp = int(input("Enter the count of numbers you want to add(for example "
                            f"\nif I want to add 4 numbers (12,13,48,12) i will type 4)  : "))
        sum_num = 0
        while user_inp > 0:
            num = float(input(f"Enter the numbers you want to sum up(one after the other): "))
            sum_num = sum_num + num
            user_inp -= 1

            print(f"Answer : {sum_num}")
    elif opperators in ["substract","Substract" , "Substracrion", "-" , "substraction"]:
        print(f"--- Performing Substraction of Numbers ---")
        user_inp = int(input("Enter the count of numbers you want to substract(for example "
                               f"\nif I want to add 4 numbers (12,13,48,12) i will type 4)  : "))
        sub_num = float(input("Enter the number you want to substract: "))
        user_inp -= 1
        while user_inp > 0:
            num = float(input(f"Enter the next numbers: "))
            sub_num = sub_num-num
            user_inp -= 1

            print(f"Answer: {sub_num}")
    elif opperators in ["multiplication" , "Multiplication" , "*" , "multiple", "Multiple"]:
        print(f"--- Performing Multiplication of Numbers ---")
        user_inp = int(input("Enter the count of numbers you want to multiply(for example "
            f"\nif I want to add 4 numbers (12,13,48,12) i will type 4)  : "))
        mul_num = 1
        while user_inp > 0:
            num = float(input(f"Enter the numbers you want to multiple (one after the other): "))
            mul_num = mul_num * num
            user_inp -= 1

            print(f"Answer: {mul_num}")
    elif opperators in ["division" , "Division" , "/" , "divide", "Division" ]:
        print(f"--- Performing Division of Numbers ---")
        div_num1 = float(input("Enter the numerator: "))
        div_num2= float(input("enter the denominator: "))
        if div_num2 == 0:
            print(f"Division can't be performed with a zero (0) number")
        else:
            answer=div_num1/div_num2
            print(f"Answer: {answer}")
    elif opperators in ["exponential" "Exponential" , "exp", "Exponential", "Exponent", "exponent"]:
        print(f"--- Performing Exponential of Numbers ---")
        expo_num1 = float(input("Enter the base number: "))
        expo_num2 = float(input("enter the exponent: "))
        answer = expo_num1**expo_num2
        print(f"Answer: {answer}")
    elif opperators in ["square root", "squared root", "sqrt", "Sqrt", "SQRT" , "Squared root", "Square root" "root" "Root"]:
        print(f"--- Performing Squared Root of Numbers ---")
        sqrt_num1 = float(input("Enter the number to find the squared root : "))
        sqrt_num2 = float(input("Enter root : "))
        answer= sqrt_num1**(1/sqrt_num2)
        print(f"Answer: {answer}")

    else:
        print(f"Invalid operation entered")

get_calc_info()
