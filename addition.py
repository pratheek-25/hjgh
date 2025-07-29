def add_three_numbers(num1, num2, num3):
    """
    Function to calculate the sum of three numbers
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        num3 (float): Third number
    
    Returns:
        float: Sum of the three numbers
    """
    return num1 + num2 + num3

def main():
    """
    Main function to get user input and display the result
    """
    print("Addition of Three Numbers Calculator")
    print("=" * 35)
    
    try:
        # Get input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        # Calculate the sum
        result = add_three_numbers(num1, num2, num3)
        
        # Display the result
        print(f"\nResult: {num1} + {num2} + {num3} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers only!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()