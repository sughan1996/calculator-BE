from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()

setup(
    name='CalculatorApp',
    version='0.1.0',
    description='Your package description',
    author='Your Name',
    author_email='youremail@example.com',
    license='MIT',
    packages=find_packages() + ['CalculatorQuantApp'],  # Include your package and the subpackage
    install_requires=requirements,
    python_requires='>=3.6',
    package_data={'CalculatorQuantApp': ['*']}  # Include package data
)
