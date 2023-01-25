from calculator import calculate as C

class main():

    print("Calculate here...")
    inputed_data = input()
    calculator_class = C(inputed_data)
    
    main_calculation = calculator_class.calculation()

    

    

    

    
    
    
if __name__ == "__main__":
    main()