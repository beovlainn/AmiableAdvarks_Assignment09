# file name: databaseEvan.py
# Student Name: Evan Bolin
# email:  bolinen@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:   
# Brief Description of what this module does: 

# Citations: N/A

def get_manufacturer_name(cursor, manufacturer_id):
    """
    Retrieves the manufacturer name from the tManufacturer table based on the manufacturer ID.
    @Returns: The name of the manufacturer as a string, or None if not found.
    """
    cursor.execute(f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}")
    return cursor.fetchone()[0]

def get_brand_name(cursor, brand_id):
    """
    Retrieves the brand name from the tBrand table based on the brand ID.
    @Returns: The name of the brand as a string, or None if not found.
    """
    cursor.execute(f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}")
    return cursor.fetchone()[0]

def get_total_sold(cursor, product_id):
    """
    Calculates the total quantity of a product sold (TransactionTypeID = 1) from the tTransactionDetail and tTransaction tables.
    @Returns: The total quantity of the product sold as an integer, or 0 if no sales are found.
    """
    cursor.execute(f"""
    SELECT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail
    INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
    WHERE dbo.tTransaction.TransactionTypeID = 1 AND dbo.tTransactionDetail.ProductID = {product_id}
    """)
    result = cursor.fetchone()
    return result[0] if result else 0