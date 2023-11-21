from CalculatorApp.controllers import Calculator

calculator = Calculator()

def lambda_handler_add(event : {} = None):
    resp = calculator.add(**event)
    return resp

def lambda_handler_subtract(event : {} = None):
    resp = calculator.subtract(**event)
    return resp

def lambda_handler_multiply(event : {} = None):
    resp = calculator.multiply(**event)
    return resp
