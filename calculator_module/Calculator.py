#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def addition(x,y):
    return x+y
def substraction(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y

# user = print('Enter a number for operation \n 1. Addition\n 2. Substraction\n 3. Multiplication\n 4. Division')

while True:
    num1 = int(input('Enter your first number : ' ))
    user = input(f'choose a operation \n + \n - \n * \n / \n {num1}')
    num2 = int(input('Enter your second number : ' ))
    
    if user in ('+','-','*','/'):
        if user == '+':
            print(f'{num1}+{num2} = {addition(num1,num2)}')
        elif user == '-':
            print(f'{num1}-{num2} = {substraction(num1,num2)}')
        elif user == '*':
            print(f'{num1}*{num2} = {multiplication(num1,num2)}')
        elif user == '/':
            print(f'{num1}/{num2} = {division(num1,num2)}')
            
        new_cal = input('want to continue for new calcualtions? (yes/no):')
        if new_cal == 'no':
            print('Thank you!')
            break
        elif new_cal == 'yes':
            continue
    else:
        print('invalid input')


# In[ ]:




