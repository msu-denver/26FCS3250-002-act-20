'''
CS 3250 - Software Dev. Methods and Tools
Instructor: Thyago Mota
Student:
Description: Activity 20
'''

import os
import subprocess

def insecure_function(user_input):
    # Security flaw: Using user input in a shell command without sanitization
    os.system(f"echo {user_input}")

def another_insecure_function():
    # Security flaw: Hardcoded password
    password = "supersecretpassword"
    print(f"The password is: {password}")

def yet_another_insecure_function():
    # Security flaw: Using subprocess without shell=False
    subprocess.run(["ls", "-l"], shell=True)

if __name__ == "__main__":
    user_input = input("Enter something: ")
    insecure_function(user_input)
    another_insecure_function()
    yet_another_insecure_function()