from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()

setup(
    name='CalculatorApp',
    version='0.1.0',
    description='Your package description',
    author='Your Name',
    author_email='youremail@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='=3.6',
    dependency_links=[
        'git+https://github.com/sughan1996/calculator-quantlib.git#egg=calculator-quantlib'
    ]
)
