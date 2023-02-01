import re
from operators import CalculatorSequence as CS
class Calculate:
    def __init__(self, calculator_input):
        self.calculator_input = calculator_input.strip()

    def clean_data(self):
        self.calculator_input
        validate = re.findall(r'[0-9()^/*+-]', self.calculator_input)
        unwanted_data = [x for x in self.calculator_input if x not in validate]
        if unwanted_data != []:
            return "Invalid Input"
        else:
            return self.calculator_input

    def split_input(self):
        split_data = re.split(r'([()^/*+-])', self.clean_data())
        splitted_input = [x for x in split_data if x != '']
        return splitted_input

    def brackets(self, data):
        while "(" and ")" in data:
            pos1 = data.index("(")
            pos2 = data.index(")")
            bracket_data = data[pos1+1:pos2]
            while "^" in bracket_data:
                CS.power_of(bracket_data)
            while "*" in bracket_data:
                CS.multiplication(bracket_data)
            while "/" in bracket_data:
                CS.division(bracket_data)
            while "+" in bracket_data:
                CS.addition(bracket_data)
            while "-" in bracket_data:
                CS.subtraction(bracket_data)
            data[pos1] = bracket_data[0]
            del data[pos1+1:pos2+1]    
    
    def no_brackets(self,data):
        while "^" in data:
            CS.power_of(data)
        while "*" in data:
            CS.multiplication(data)
        while "/" in data:
            CS.division(data)
        while "+" in data:
            CS.addition(data)
        while "-" in data:
            CS.subtraction(data)
        
    def calculations(self):
        data = self.split_input()

        self.brackets(data)
        self.no_brackets(data)
        return data

        
        
    
                
        