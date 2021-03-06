"""Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции."""


def calc():
    def_operation = ['+', '-', '/', '*']
    operator = input("Введите значение операции: '+', '-', '/', '*' или укажите 0 для выхода")
    if operator == 0:
         print("Работа завершена")

    else:
        if operator in def_operation:
             try:
                value_1 = float(input ('Введите первое число: '))
                value_2 = float(input('Введите второе число: '))
                if operator == '+':
                    print(value_1 + value_2)
                elif operator == '-':
                    print(value_1 - value_2)
                elif operator == '*':
                    print( value_1 * value_2)
                elif operator == '/':
                    print(value_1 / value_2)
             except ValueError:
                print('Указаны неверные значения')
             except ZeroDivisionError:
                print ('На ноль делить не хорошо')
        else:
            print('Нет операции, попробуйте снова')
    calc()

calc()