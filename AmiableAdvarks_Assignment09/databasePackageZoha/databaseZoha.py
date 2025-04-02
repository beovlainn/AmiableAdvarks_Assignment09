# file name: databaseZoha
# Student Name: Zoha Iqbal
# email: iqbalza@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: This assignment is supposed to create a sentence  
# Brief Description of what this module does: "This module retrieves product data from a database and selects a random product

# Citations: N/A

import random

def fetch_products(cursor):
    cursor.execute("SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID FROM tProduct")
    return cursor.fetchall()

def select_random_product(products):
    return random.choice(products)