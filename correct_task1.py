def calculate_average_order_value(orders):
    total = 0
    valid_count = 0  # Count only non-cancelled orders

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            valid_count += 1

    # Handle edge case: no valid orders or empty list
    if valid_count == 0:
        return 0.0
    
    return total / valid_count
