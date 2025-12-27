'''
CHALLENGE: Storage Logistics Calculation

You have been hired to develop a system that determines the number of pallets needed 
to store the daily production of boxes. Each pallet has a fixed capacity of boxes, 
and the goal is to calculate the total number of pallets required to accommodate 
the entire daily production.

Input:
    1. The total number of boxes produced (integer).
    2. The capacity of boxes a single pallet can hold (integer).

Output:
    The program must return a string representing the total number of pallets needed, 
    without spaces or special characters.
'''

import math

def calculate_required_pallets(total_boxes: int, pallet_capacity: int) -> int:
    
    if pallet_capacity <= 0:
        raise ValueError("Pallet capacity must be greater than zero.")
        
    return math.ceil(total_boxes / pallet_capacity)

if __name__ == "__main__":
    try:
        total_boxes_input = int(input().strip())
        pallet_capacity_input = int(input().strip())
        
        result = calculate_required_pallets(total_boxes_input, pallet_capacity_input)
        
        print(result)
        
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    
    