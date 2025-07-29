from addition import add_three_numbers

def test_addition():
    """Test the add_three_numbers function with various inputs"""
    
    # Test case 1: Positive numbers
    result1 = add_three_numbers(5, 10, 15)
    print(f"Test 1: 5 + 10 + 15 = {result1}")
    
    # Test case 2: Negative numbers
    result2 = add_three_numbers(-2, -3, -5)
    print(f"Test 2: -2 + (-3) + (-5) = {result2}")
    
    # Test case 3: Mixed positive and negative
    result3 = add_three_numbers(10, -5, 3)
    print(f"Test 3: 10 + (-5) + 3 = {result3}")
    
    # Test case 4: Decimal numbers
    result4 = add_three_numbers(1.5, 2.7, 3.8)
    print(f"Test 4: 1.5 + 2.7 + 3.8 = {result4}")
    
    # Test case 5: Zero values
    result5 = add_three_numbers(0, 0, 0)
    print(f"Test 5: 0 + 0 + 0 = {result5}")

if __name__ == "__main__":
    print("Testing the addition function:")
    print("=" * 30)
    test_addition()
    print("\nAll tests completed successfully!")