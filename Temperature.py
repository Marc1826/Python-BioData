# -*- coding: utf-8 -*-
"""Temperature.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FxV7n0wZdWfH2j6HaEXJ70ROJ4t1F-C8
"""

cel = float(input("Input the value of celcius: "))

fahrenheit= (1.8 * cel)+32
reaumur =  cel * 0.8
print("The equivalent of celcius to fahrenheit: {:.2f} and Reaumur: {:.2f}".format(fahrenheit,reaumur))