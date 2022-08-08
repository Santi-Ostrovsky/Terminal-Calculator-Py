# FIX FORMATTING FUNCTION.

# Define global variables.
num1 = 0
num2 = 0
result = 'N/A'
num_format = ''
valid = True
memory = []
# Define an 'operators' list (if modified, update the 'user_help()' function).
operators = ['+', '-', '*', '/', '%', 'A', '**', '//']


# Define a 'value-formatting' function (display '.0' floats as integers).
def format_num(x):
    global num_format
    try:
        x = '{:,}'.format(x)
        if x.endswith('.0'):
            num_format = x[:-2]
    except ValueError:
        pass
    return num_format


# Define an 'Operations' class for memory-display.
class Operations:
    def __init__(self, value1, operator, value2, answer):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2
        self.answer = answer


# Define an operation's list-printing function.
def past_results():
    global memory, num1
    print('\nPrevious operations:'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    if len(memory) == 0:
        print('None')
    while len(memory) > 10:
        memory.pop(0)
    for m in memory:
        print('>', m.value1, m.operator, m.value2, '=', m.answer)
    print('\nContinue your operation'
          '\nYour first value is ───→', num1)


# Define user float-only input VALIDATION function.
def valid_num(x):
    global valid
    number = ''
    while valid:
        try:
            number = float(input(x + ': '))
            break
        except ValueError:
            print('\nInvalid input (numbers and decimal points only).')
    return number


# Define an operator VALIDATION function.
def valid_op():
    op = input('\nOperator: ').upper()
    while op not in operators or op.isspace():
        if op == 'H':
            user_help()
            op = input('\nOperator: ').upper()
        elif op == 'M':
            past_results()
            op = input('\nOperator: ').upper()
        elif op == 'R':
            print('\nYour calculation has been reseted.\n')
            calculate()
        else:
            print('\n► Invalid operator, try again.\n')
            op = input('Operator: ').upper()
    return op


# Define an "operations" function.
def operate(x):
    global num1, num2, result, memory
    while x in operators:
        try:
            if x == '+':  # ADDITION
                result = float(num1) + float(num2)
                break
            elif x == '-':  # SUBTRACTION
                result = float(num1) - float(num2)
                break
            elif x == '*':  # MULTIPLICATION
                result = float(num1) * float(num2)
                break
            elif x == '/':  # DIVISION
                result = float(num1) / float(num2)
                break
            elif x == '**':  # POWER
                result = float(num1) ** float(num2)
                break
            elif x == '//':  # ROOT
                result = float(num1) ** (1 / float(num2))
                break
            elif x == 'A':  # AVERAGE
                result = (float(num1) + float(num2)) / 2
                break
            elif x == '%':  # PERCENTAGE
                result = float(num1) * float(num2) / 100
                break
        except ArithmeticError as error:
            print('\nError:', error)
            break
    # Add the operation to the 'memory' list.
    operation = Operations(num1, x, num2, result)
    memory.append(operation)
    # Format and display result.
    print('\n──→ Result:', result, '\n'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')


# Define "calculate" function. Program LOOP.
def calculate():
    global num1, num2, valid
    while valid:
        num1 = valid_num('\nFirst value')
        operator = valid_op()
        num2 = valid_num('\nSecond value')
        operate(operator)


# Define "user_help" function.
def user_help():
    global num1
    print('\nList of possible operators and their uses:'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'
          '\n- Use [ M ] to display a list of the last 10 operations.'
          '\n- Use [ R ] to reset your calculation.'
          '\n- Use [ + ] for Addition - [Value #1] plus [Value #2].'
          '\n- Use [ - ] for Subtraction - [Value #1] minus [Value #2].'
          '\n- Use [ * ] for Multiplication - [Value #1] by [Value #2].'
          '\n- Use [ / ] for Division - [Value #1] divided by [Value #2].'
          '\n- Use [ % ] for Percentage - [Value #1] percentage of [Value #2].'
          '\n- Use [ A ] for Average - Average of [Value #1] and [Value #2].'
          '\n- Use [ ** ] for Power operation - [Value #1] raised by the power of [Value #2].'
          '\n- Use [ // ] for Root operation - [Value #1] rooted by the value of [Value #2].'
          '\n\nContinue your operation'
          '\nYour first value is ───→',  num1)


""" START OF PROGRAM EXECUTION """

# Welcome user and introduce the 'help' operator.
print('\n         ╔═══════════════════════════════╗'
      '\n         ║ Welcome to Santi\'s Calculator ║'
      '\n         ╚═══════════════════════════════╝'
      '\n\n► If you need help with available operators and their'
      '\n    uses, enter \'H\' when the operator is requested.'
      '\n\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

# Execute 'calculate' LOOP.
calculate()
