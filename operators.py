class CalculatorSequence:
    def power_of(data):
        for i in range(len(data)):
            power_of = 0
            if data[i] == "^":
                power_of = int(data[i-1]) ** int(data[i+1])
                data[i-1] = power_of
                del data[i:i+2]
                break
        return data

    def multiplication(data):
        for i in range(len(data)):
            multiply = 0
            if data[i] == "*":
                multiply = int(data[i-1]) * int(data[i+1])
                data[i-1] = multiply
                del data[i:i+2]
                break
        return data

    def division(data):
        for i in range(len(data)):
            division = 0
            if data[i] == "/":
                if int(data[i+1]) == 0:
                    raise Exception("Zero Division Error")
                division = int(data[i-1]) / int(data[i+1])
                data[i-1] = division
                del data[i:i+2]
                break
        return data

    def addition(data):
        for i in range(len(data)):
            addition = 0
            if data[i] == "+":
                addition = int(data[i-1]) + int(data[i+1])
                data[i-1] = addition
                del data[i:i+2]
                break
        return data

    def subtraction(data):
        for i in range(len(data)):
            subtraction = 0
            if data[i] == "-":
                subtraction = int(data[i-1]) - int(data[i+1])
                data[i-1] = subtraction
                del data[i:i+2]
                break
        return data