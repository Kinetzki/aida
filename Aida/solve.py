import sympy as sym
import math

x = sym.Symbol('x')
y = sym.Symbol('y')
z = sym.Symbol('z')


def derivative(equation):
    equation = equation.replace('what is ', '')
    equation = equation.replace('five', '5')
    equation = equation.replace('derivative of ', '')
    equation = equation.replace('the ', '')
    equation = equation.replace(' x x ', ' times x ')
    equation = equation.replace(' raised to ', '**')
    equation = equation.replace('to', '2')
    equation = equation.replace(' times ', ' * ')
    equation = equation.replace('one', '1')
    equation = equation.replace(' plus ', ' + ')
    equation = equation.replace(' minus ', ' - ')
    equation = equation.replace(' divided by ', ' / ')
    equation = equation.replace('squared', ' **2')
    equation = sym.sympify(equation)
    equation = str(sym.diff(equation))
    equation = equation.replace('**', ' raised to ')
    equation = equation.replace('-', 'minus')
    equation = equation.replace('*', ' times ')
    equation = equation.replace('*', ' times ')
    equation = equation.replace('minus', 'negative ')

    return equation


def square_root(equation):
    equation = equation.replace('square root of ', '')
    equation = equation.replace('one', '1')
    equation = sym.sympify(equation)
    return math.sqrt(equation)


def math_(equation):
    equation = equation.replace('what is ', '')
    equation = equation.replace('derivative of ', '')
    equation = equation.replace('five', '5')
    equation = equation.replace('the ', '')
    equation = equation.replace('one', '1')
    equation = equation.replace(' raised to ', '**')
    equation = equation.replace(' raise to ', '**')
    equation = equation.replace('to', '2')
    equation = equation.replace(' times ', ' * ')
    equation = equation.replace(' plus ', ' + ')
    equation = equation.replace(' minus ', ' - ')
    equation = equation.replace(' divided by ', ' / ')
    equation = equation.replace('squared', ' **2')
    equation = equation.replace(' x ', '')

    equation = sym.sympify(equation)

    return equation
