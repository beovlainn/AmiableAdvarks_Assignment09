# file name: databaseJabob.py
# Student Name: Jacob Farrell
# email:  farrelcj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:   
# Brief Description of what this module does: Connects to the given grocery store database.

# Citations: N/A

import pyodbc

def get_connection():
    """
    Establishes a connection to the GroceryStoreSimulator database.
    """
    return pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=GroceryStoreSimulator;'
        'uid=IS4010Login;'
        'pwd=P@ssword2;'
    )