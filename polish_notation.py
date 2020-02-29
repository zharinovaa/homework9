equation = input('Введите выражение : ')
operations = equation.split()

if len(operations) != 3:
    try:
      raise Exception('Необходимо ввести только 3 аргумента')
    except Exception as e:
        print(e)
        exit(0)

result = 'Результат не получен'

assert (operations[0] == '+') or (operations[0] == '-') or (operations[0] == '*') or (operations[0] == '/'), 'Вы ввели не тот операнд'
try:
    if operations[0] == '+':
        result = int(operations[1]) + int(operations[2])
    elif operations[0] == '-':
        result = int(operations[1]) - int(operations[2])
    elif operations[0] == '*':
        result = int(operations[1]) * int(operations[2])
    elif operations[0] == '/':
        result = int(operations[1]) / int(operations[2])
except(ZeroDivisionError):
    print('На нуль делить нельзя!')
except(TypeError):
    print('Операции применимы только к числам!')

print(result)