from CalculatorApp.controllers import Calculator

calculator = Calculator()

def lambda_handler(event : {} = None):
    resp = calculator.add(**event)
    return resp
