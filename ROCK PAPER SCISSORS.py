# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:25:48 2022

@author: RAPHLAINGO
100 DAYS OF PYTHON
"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('WELCOME TO ROCK PAPER SCISSORS')
import random
user= eval(input('0 for ROCK,1 for PAPER OR 2 for SCISSORS\n'))
if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
computer= random.randint(0,2)
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
elif computer==2:
    print(scissors)
    
#results
if user==0 and computer==0:
    print('DRAW')
elif user==0 and computer==1:
    print('COMPUTER WINS')
elif user==0 and computer==2:
    print('USER WINS')
    
if user==1 and computer==0:
    print('USER WINS')
elif user==1 and computer==1:
    print('DRAW')
elif user==1 and computer==2:
    print('COMPUTER WINS')
    
if user==2 and computer==0:
    print('COMPUTER WINS')
elif user==2 and computer==1:
    print('USER WINS')
elif user==2 and computer==2:
    print('DRAW')

