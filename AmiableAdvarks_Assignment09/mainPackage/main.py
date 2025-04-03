# main.py
# Student Name: Zoha Iqbal, Jacob Farrell, Evan Bolin
# email:  iqbalza@mail.uc.edu , farrelcj@mail.uc.edu , bolinen@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Create a grammatically correct sentnce that states the item name, manufacturer and units sold from a given grocery database. 
# Brief Description of what this module does: Calls to the other packages and prints a sentence with the product name, manufacturer, and units sold.

# Citations: N/A

from databasePackageJacob.databaseJacob import get_connection
from databasePackageZoha.databaseZoha import fetch_products, select_random_product
from databasePackageEvan.databaseEvan import get_manufacturer_name, get_brand_name, get_total_sold

def main():

    conn = get_connection()
    cursor = conn.cursor()
    
    products = fetch_products(cursor)
    selected_product = select_random_product(products)
    
    manufacturer_name = get_manufacturer_name(cursor, selected_product[3])
    brand_name = get_brand_name(cursor, selected_product[4])
    total_sold = get_total_sold(cursor, selected_product[0])

    description = selected_product[2]
    output = (
        f"The {description} by {manufacturer_name} ({brand_name}) "
        f"has sold {total_sold} units."
    )
    
    print(output)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()