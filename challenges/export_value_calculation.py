'''
CHALLENGE: Export Value Calculation - DIO

A paper packaging producer and exporter needs to calculate the final value of its shipments. 
Each shipment has a weight in tons and a price per ton in dollars. 
Additionally, depending on the customer type, the company offers discounts:

    - New client ("Novo cliente"): No discount
    - Loyal client ("Cliente fidelizado"): 5% discount
    - Premium client ("Cliente premium"): 10% discount

The program must calculate the total shipment value considering the weight, 
price per ton, and applicable discount, returning the final amount to be paid by the customer.

Input:
    1. A decimal number representing the cargo weight in tons.
    2. A decimal number representing the price per ton in dollars.
    3. A string representing the customer type.

Output:
    The program must return the final export value (in dollars), 
    with the discount applied, formatted to two decimal places.
'''


def calculate_final_price(weight, price_per_ton, customer_type):
    
    total_value = weight * price_per_ton

    # Determine the discount based on customer type
    discount = 0.0

    if customer_type == "New client":
        discount = 0.0
    elif customer_type == "Loyal client":
        discount = 0.05
    elif customer_type == "Premium client":
        discount = 0.10

    # Apply discount
    return total_value * (1 - discount)


if __name__ == "__main__":
    weight = float(input("Enter the cargo weight (in tons): "))
    price_per_ton = float(input("Enter the price per ton: "))
    customer_type = input("Enter the customer type (New client, Loyal client, Premium client): ")

    final_price = calculate_final_price(weight, price_per_ton, customer_type)

    print(f"{final_price:.2f}")
