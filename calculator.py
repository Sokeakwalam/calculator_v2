import re

class calculate:
    def __init__(self, calculator_input):
        self.calculator_input = calculator_input.rstrip()
    
    def split_input(self):
        splitted_output = re.split(r'([()^/*+-])', self.calculator_input)
        return splitted_output
          
    def calculation(self):
        data = self.split_input()
        for i in data:
            return data
        
      

        
                
                
