N = int(input("Enter the number of orders: "))

totals = {
  'bag': 0,
  'corrugated cardboard': 0,
  'kraft paper': 0
}

for i in range(N):
  line = input(f"Order {i+1}/{N}: Enter the order details (customer name, packaging type, quantity in tons): ")
  try:
    customer, packaging, quantity = line.split(", ")
    quantity = float(quantity)
    
    if "bag" in packaging:
      totals['bag'] += quantity
    elif "corrugated cardboard" in packaging:
      totals['corrugated cardboard'] += quantity
    elif "kraft paper" in packaging:
      totals['kraft paper'] += quantity
    else:
      print("Invalid packaging type")
  except ValueError:
    print("Invalid input format. Please ensure you enter the details correctly.")

for type in ["bag", "corrugated cardboard", "kraft paper"]:
  value = totals[type]
  if isinstance(value, float) and value.is_integer():
    value = int(value)
  print(f"{type}: {value}")
