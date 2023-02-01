from calculator import Calculate as C
class main():

    def main_calculation():
        print("Calculate here...")
        inputed_data = input()

        user_input = C(inputed_data)
        
        answer = user_input.calculations()
        if len(answer) > 1:
            for i in range(len(answer)-1):
                final_answer = answer[i] * answer[i+1]
            return final_answer
        else:
            return answer[0]
    print(main_calculation())

    
   
if __name__ == "__main__":
    main()