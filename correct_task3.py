def average_valid_measurements(values):
    total = 0
    valid_count = 0  # Count only non-None values

    for v in values:
        if v is not None:
            try:
                total += float(v)
                valid_count += 1
            except (ValueError, TypeError):
                # Skip values that can't be converted to float
                continue

    # Handle edge case: no valid measurements
    if valid_count == 0:
        return 0.0
    
    return total / valid_count
