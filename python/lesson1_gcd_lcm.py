#!/usr/bin/env python3
"""
GCD and LCM Calculator for Kids!
Learn about Greatest Common Divisor and Least Common Multiple
"""

def find_gcd(a, b):
    """
    Find the Greatest Common Divisor (GCD) of two numbers.
    
    English: Greatest Common Divisor (GCD)
    Chinese: 最大公约数 (zuì dà gōng yuē shù) or 最大公因数 (zuì dà gōng yīn shù)
    
    The GCD is the largest number that divides both numbers without leaving a remainder.
    
    This function uses the Euclidean Algorithm, which is much faster than finding all factors!
    
    HOW THE ALGORITHM WORKS:
    The key insight is that the GCD of two numbers is the same as the GCD of the 
    smaller number and the remainder when you divide the larger by the smaller.
    
    STEP-BY-STEP EXAMPLE (GCD of 48 and 18):
    1. First iteration:  a=48, b=18, remainder=48%18=12
       New values: a=18, b=12
    2. Second iteration: a=18, b=12, remainder=18%12=6
       New values: a=12, b=6
    3. Third iteration:  a=12, b=6,  remainder=12%6=0
       New values: a=6, b=0
    4. Loop ends because b=0
    5. Return a=6 (the GCD!)
    
    WHY THIS WORKS:
    If a number divides both a and b, it also divides the remainder (a % b).
    So any common divisor of a and b is also a common divisor of b and a % b.
    The reverse is also true, so the GCD must be the same!
    
    This is much faster than finding all factors because it just uses division
    and remainders, not prime factorization.
    """
    # Keep dividing until we can't divide anymore
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    """
    Find the Least Common Multiple (LCM) of two numbers.
    
    English: Least Common Multiple (LCM)
    Chinese: 最小公倍数 (zuì xiǎo gōng bèi shù)
    
    The LCM is the smallest number that both numbers can divide into.
    
    Example: LCM of 4 and 6
    - Multiples of 4: 4, 8, 12, 16, 20, 24, ...
    - Multiples of 6: 6, 12, 18, 24, 30, ...
    - Common multiples: 12, 24, 36, ...
    - LCM = 12 (the smallest common multiple)
    """
    # LCM = (a × b) ÷ GCD(a, b)
    return (a * b) // find_gcd(a, b)

def show_examples():
    """Show some fun examples of GCD and LCM!"""
    print("🎯 Let's learn about GCD and LCM with some examples!\n")
    
    examples = [
        (12, 18),
        (8, 12),
        (15, 25),
        (9, 16)
    ]
    
    for num1, num2 in examples:
        gcd = find_gcd(num1, num2)
        lcm = find_lcm(num1, num2)
        
        print(f"Numbers: {num1} and {num2}")
        print(f"  GCD = {gcd}")
        print(f"  LCM = {lcm}")
        print()

def interactive_calculator():
    """Let kids input their own numbers to find GCD and LCM!"""
    print("🔢 Interactive GCD and LCM Calculator!")
    print("Enter two numbers to find their GCD and LCM.")
    print("(Type 'quit' to exit)\n")
    
    while True:
        try:
            # Get first number
            num1_input = input("Enter first number: ").strip().lower()
            if num1_input == 'quit':
                print("Thanks for learning! 👋")
                break
            
            num1 = int(num1_input)
            
            # Get second number
            num2_input = input("Enter second number: ").strip().lower()
            if num2_input == 'quit':
                print("Thanks for learning! 👋")
                break
            
            num2 = int(num2_input)
            
            # Calculate and show results
            gcd = find_gcd(num1, num2)
            lcm = find_lcm(num1, num2)
            
            print(f"\n✨ Results for {num1} and {num2}:")
            print(f"   Greatest Common Divisor (GCD) = {gcd}")
            print(f"   Least Common Multiple (LCM) = {lcm}")
            
            # Show the relationship: LCM divided by each number
            multiple1 = lcm // num1
            multiple2 = lcm // num2
            print(f"   {lcm} ÷ {num1} = {multiple1} (first multiple)")
            print(f"   {lcm} ÷ {num2} = {multiple2} (second multiple)")
            print()
            
        except ValueError:
            print("❌ Please enter valid numbers!")
            print()
        except KeyboardInterrupt:
            print("\n\nThanks for learning! 👋")
            break

def main():
    """Main function to run our GCD and LCM learning program!"""
    print("=" * 50)
    print("🌟 Welcome to GCD and LCM Learning! 🌟")
    print("=" * 50)
    print()
    
    # Show examples first
    show_examples()
    
    # Then let kids try it themselves
    interactive_calculator()

if __name__ == "__main__":
    main()
