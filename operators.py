class CalculatorSequence:
    def off(data):
        for i in range(len(data)-1):
            if type(data[i]) == float and type(data[i+1]) == float:
                temp = data[i] * data[i+1]
                data[i] = temp
                del data[i+1]
                break
        
        return data

    def power_of(data):
        for i in range(len(data)):
            power_of = 0
            if data[i] == "^":
                power_of = data[i-1] ** data[i+1]
                data[i-1] = power_of
                del data[i:i+2]
                break
        return data

    def multiplication(data):
        for i in range(len(data)):
            multiply = 0
            if data[i] == "*":
                multiply = data[i-1] * data[i+1]
                data[i-1] = multiply
                del data[i:i+2]
                break
        return data

    def division(data):
        for i in range(len(data)):
            division = 0
            if data[i] == "/":
                if data[i+1] == 0:
                    raise ZeroDivisionError("Zero Division Error")
                division = data[i-1] / data[i+1]
                data[i-1] = division
                del data[i:i+2]
                break
        return data

    def addition(data):
        for i in range(len(data)):
            addition = 0
            if data[i] == "+":
                if data[i+1] == "+":
                    data[i] = "+"
                    del data[i+1]
                    break
                addition = data[i-1] + data[i+1]
                data[i-1] = addition
                del data[i:i+2]
                break
        return data

    def subtraction(data):
        for i in range(len(data)):
            subtraction = 0
            if data[i] == "-":
                if data[i+1] == "-":
                    data[i] = "+"
                    del data[i+1]
                    break
                elif data[i+1] == "+":
                    data[i] = "-"
                    del data[i+1]
                    break
                elif data[i-1] == "+":
                    data[i-1] = "-"
                    del data[i:i+2]
                    break
                subtraction = data[i-1] - data[i+1]
                data[i-1] = subtraction
                del data[i:i+2]
                break

        return data