#!/usr/bin/env python3
"""
Test file for GCD and LCM functions!
Kids should implement their own find_gcd and find_lcm functions,
then run this test to see if they're correct.
"""

def test_gcd_lcm_functions():
    """
    Test function to check if the kids' GCD and LCM functions work correctly.
    
    Kids should implement their own find_gcd and find_lcm functions above this function.
    """
    
    # Test cases with known answers
    test_cases = [
        (12, 18, 6, 36),      # (num1, num2, expected_gcd, expected_lcm)
        (8, 12, 4, 24),
        (15, 25, 5, 75),
        (9, 16, 1, 144),
        (35, 77, 7, 385),
        (48, 18, 6, 144),
        (100, 75, 25, 300),
        (7, 13, 1, 91),
        (24, 36, 12, 72),
        (50, 125, 25, 250)
    ]
    
    print("🧪 Testing your GCD and LCM functions...")
    print("=" * 50)
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, (num1, num2, expected_gcd, expected_lcm) in enumerate(test_cases, 1):
        print(f"\nTest {i}: Numbers {num1} and {num2}")
        
        try:
            # Test GCD function
            your_gcd = find_gcd(num1, num2)
            gcd_correct = your_gcd == expected_gcd
            
            # Test LCM function
            your_lcm = find_lcm(num1, num2)
            lcm_correct = your_lcm == expected_lcm
            
            # Show results
            print(f"  Your GCD: {your_gcd} | Expected: {expected_gcd} | {'✅' if gcd_correct else '❌'}")
            print(f"  Your LCM: {your_lcm} | Expected: {expected_lcm} | {'✅' if lcm_correct else '❌'}")
            
            # Check if both are correct
            if gcd_correct and lcm_correct:
                passed_tests += 1
                print(f"  🎉 Test {i} PASSED!")
            else:
                print(f"  💡 Test {i} needs work. Keep trying!")
                
        except NameError:
            print("  ❌ Error: You haven't defined find_gcd and find_lcm functions yet!")
            print("  💡 Add your functions above this test function.")
        except Exception as e:
            print(f"  ❌ Error in your functions: {e}")
    
    # Final results
    print("\n" + "=" * 50)
    print(f"🏆 Final Score: {passed_tests}/{total_tests} tests passed!")
    
    if passed_tests == total_tests:
        print("🎉 CONGRATULATIONS! All tests passed!")
        print("You've successfully implemented GCD and LCM functions!")
    elif passed_tests > 0:
        print(f"👍 Good progress! {passed_tests} out of {total_tests} tests passed.")
        print("Keep working on the ones that failed!")
    else:
        print("💪 Don't give up! Review the concepts and try again.")
        print("Remember: GCD is the largest number that divides both numbers.")
        print("Remember: LCM is the smallest number both numbers can divide into.")

def run_bonus_tests():
    """
    Bonus tests for kids who want extra challenge!
    """
    print("\n🌟 BONUS CHALLENGE TESTS 🌟")
    print("=" * 30)
    
    bonus_cases = [
        (0, 5, 5, 0),         # Edge case: one number is 0
        (1, 1, 1, 1),         # Edge case: same numbers
        (17, 23, 1, 391),     # Prime numbers
        (1000, 1001, 1, 1001000),  # Large numbers
    ]
    
    for i, (num1, num2, expected_gcd, expected_lcm) in enumerate(bonus_cases, 1):
        print(f"\nBonus Test {i}: Numbers {num1} and {num2}")
        
        try:
            your_gcd = find_gcd(num1, num2)
            your_lcm = find_lcm(num1, num2)
            
            gcd_correct = your_gcd == expected_gcd
            lcm_correct = your_lcm == expected_lcm
            
            print(f"  GCD: {your_gcd} | Expected: {expected_gcd} | {'✅' if gcd_correct else '❌'}")
            print(f"  LCM: {your_lcm} | Expected: {expected_lcm} | {'✅' if lcm_correct else '❌'}")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")

# ============================================================================
# KIDS: ADD YOUR FUNCTIONS HERE!
# ============================================================================

# TODO: Write your find_gcd function here
# def find_gcd(a, b):
#     # Your code here!
#     pass

# TODO: Write your find_lcm function here  
# def find_lcm(a, b):
#     # Your code here!
#     pass

# ============================================================================
# DON'T CHANGE ANYTHING BELOW THIS LINE!
# ============================================================================

if __name__ == "__main__":
    print("🚀 Welcome to the GCD and LCM Test Suite!")
    print("This will test your implementations of find_gcd and find_lcm functions.")
    print("\n📝 Instructions:")
    print("1. Look for the TODO section above")
    print("2. Implement your find_gcd and find_lcm functions")
    print("3. Run this file to test your code!")
    print("4. Keep trying until all tests pass!")
    
    # Check if functions exist
    try:
        find_gcd(1, 1)
        find_lcm(1, 1)
        print("\n✅ Functions found! Running tests...")
        test_gcd_lcm_functions()
        run_bonus_tests()
    except NameError:
        print("\n❌ Functions not found yet!")
        print("Please implement find_gcd and find_lcm functions above the test section.")
        print("Then run this file again to test your code!")
