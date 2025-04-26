# Find the five digit number which has the following property: 
# if we multiply the first two digits by the last three digits, we get the same number but in different order. 
# There is no 0 in the numbers. For example, 24651.  This can be broken down into 24 * 651 = 15624.  

def has_no_zero(number):
    """Check if a number has no zero digits."""
    return '0' not in str(number)

def is_rearrangement(original, product):
    """Check if two numbers are rearrangements of each other."""
    return sorted(str(original)) == sorted(str(product)) and original != product

# Search for the 5-digit number
for num in range(10000, 100000):
    if not has_no_zero(num):
        continue  # Skip if there's a 0

    first_two = int(str(num)[:2])
    last_three = int(str(num)[2:])
    
    product = first_two * last_three
    
    if 10000 <= product <= 99999:  # Make sure product is also 5 digits
        if is_rearrangement(num, product):
            print(f"Found! Number: {num}, First two: {first_two}, Last three: {last_three}, Product: {product}")
