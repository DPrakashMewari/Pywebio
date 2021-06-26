import pywebio
from pywebio.input import * 
from pywebio.output import *

def mathematicoperation():
	a = input("Enter the firstnumber",type=FLOAT) 
	b = input("Enter the secondnumber",type=FLOAT)
	c = 0 
	operation = radio("Choose one operation",options=["+","-","/","%","*"])
	operation_name = ""
	if operation == "+":
		operation_name ="Addition"
		c = a + b
	elif operation == "-":
		operation_name = "Subraction"
		c = a - b
	elif operation == "/":
		operation_name = 'Divide'
		c = a/b	
	elif operation == "*":
		operation_name = "Multiplication"
		c = a*b
	else:
		operation_name == "Modulus"
		c = a%b
	put_text("The operation select is %s and the output is %.2f"%(operation_name,c))

if __name__ == '__main__':
		mathematicoperation()	