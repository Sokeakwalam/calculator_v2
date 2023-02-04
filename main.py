from calculator import Calculate as C

class main():

    def main_calculation():
        print("Calculate here...")
        inputed_data = input()
        user_input = C(inputed_data)
        answer = user_input.calculations()
        return answer     
    print(main_calculation())

    
   
if __name__ == "__main__":
    main()