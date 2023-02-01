import re
import operators as O

class Calculate:
    def __init__(self, calculator_input):
        self.calculator_input = calculator_input

    def split_input(self):
        split_data = re.split(r'([()^/*+-])', self.calculator_input)
        splitted_input = [x for x in split_data if x != '']
        return splitted_input

    def brackets(self, data):
        while "(" and ")" in data:
            pos1 = data.index("(")
            pos2 = data.index(")")
            bracket_data = data[pos1+1:pos2]
            while "^" in bracket_data:
                O.power_of(bracket_data)
            while "*" in bracket_data:
                O.multiplication(bracket_data)
            while "/" in bracket_data:
                O.division(bracket_data)
            while "+" in bracket_data:
                O.addition(bracket_data)
            while "-" in bracket_data:
                O.subtraction(bracket_data)
            data[pos1] = bracket_data[0]
            del data[pos1+1:pos2+1]    
    
    def no_brackets(self,data):
        while "^" in data:
            O.power_of(data)
        while "*" in data:
            O.multiplication(data)
        while "/" in data:
            O.division(data)
        while "+" in data:
            O.addition(data)
        while "-" in data:
            O.subtraction(data)
        
    def calculations(self):
        data = self.split_input()

        self.brackets(data)
        self.no_brackets(data)
        return data

        
        
    
                
        