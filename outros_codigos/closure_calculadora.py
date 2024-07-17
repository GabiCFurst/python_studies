def calculator(number1, number2):
    def type_calculation(operator):
        if operator == '+':
            return number1 + number2
        elif operator == '-':
            return number1 - number2
        elif operator == '*':
            return number1 * number2
        elif operator == '/':
            try:
                return number1 / number2
            except ValueError:
                return 'Is not possible divide any number by 0.'
    return type_calculation
 
 
operation1 = calculator(2, 1)
operation2 = calculator(1, 6)
operation3 = calculator(5, 1)
operation4 = calculator(1, 9)
 
print(operation1('+'))  # 2
print(operation2('-'))  # 0
print(operation3('*'))  # 1
print(operation4('/'))  # 1 