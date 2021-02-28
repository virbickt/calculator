# calculator
![](https://img.shields.io/badge/python-v3.7-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=blue)

The following has been made for educational purposes as part of the final project of 2.1.5: "Software Engineering and Reproducible Research" by Turing College. It is meant to serve as a toy-example of making a package that can be later installed using `pip`. Standard package structure has been adapted and initalized.  

- [Introduction](#Introduction)
  * [And a table of contents](#and-a-table-of-contents)
  * [On the right](#on-the-right)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Introduction
> A **mechanical calculator**, or calculating machine, is a mechanical device used to perform the basic operations of arithmetic automatically [...] 
> The first mechanical calculator (also known as *Pascaline*) appeared in 1642, the creation of French intellectual Blaise Pascal as "a device that will eventually perform all four arithmetic operations without relying on human intelligence."
 
350 years later, the idea of calculator is still inconceivable without the original four operations - addition, subtraction, multiplication and division. This is exemplified by the code that you will find here - an object `calculator`, which, in addition, is also able to take square root of a number.

### Installation
To install the package directly from github using `pip`, use the following:
```
pip install git+https://github.com/virbickt/calculator.git
```
Once the package has been succesfully installed, make sure to include the import statement:
```
from calculator import Calculator
```

### Addition
Addition is performed by using `calculator.add()`. It takes inputs of type float and returns the result of adding the input value to the value stored in the memory state:
```
calculator = Calculator()
calculator.add(5)
calculator.add(2)
```

### Subtraction
Substraction is performed by using `calculator.subtract()`. It takes inputs of type float and returns the result of substracting the input value from the value stored in the memory state:
```
# Assuming that the memory state equals to 7
calculator.subtract(5)
```

### Multiplication
Multiplication is performed by using `calculator.multiply()`. It takes inputs of type float and returns the result of multiplying the input value to the value stored in the memory state:
```
# Assuming that the memory state equals to 2
calculator.multiply(3)
```

### Division
Division is performed by using `calculator.divide()`. It takes inputs of type float and returns the result of multiplying the input value to the value stored in the memory state:
```
# Assuming that the memory state equals to 6
calculator.divide(3)
```

### Square root
The operation of taking square root is performed by using `calculator.sqrt()`. It takes no inputs and returns the result of taking square root of the value stored in the memory state:
```
# Assuming that the memory state equals to 4
calculator.sqrt(4)
```
`calculator.sqrt()` uses `math.sqrt` as it has been found to be quicker than the alternative such as `pow()` or `**0.5`
