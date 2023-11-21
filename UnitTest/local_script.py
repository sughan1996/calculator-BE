from CalculatorApp import Calculator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


if __name__ == '__main__':
    calculator = Calculator()
    logger.info(calculator.add(1,2))
    logger.info(calculator.multiply(3,5))


