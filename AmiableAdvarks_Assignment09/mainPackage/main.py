# main.py
# Student Name: {required}
# email:  {required}
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:   
# Brief Description of what this module does: 

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
        f"has sold {total_sold} items."
    )
    
    print(output)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()