import sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

def test0():
    from ai_unit_testing.code_under_test import incr_list
    assert incr_list([]) == []
    assert incr_list([3, 2, 1]) == [4, 3, 2]
    assert incr_list([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]

def test1():
    from ai_unit_testing.code_under_test import is_prime
    assert is_prime(6) == False   
    assert is_prime(101) == True    
    assert is_prime(11) == True   
    assert is_prime(13441) == True    
    assert is_prime(61) == True   
    assert is_prim(4) == False   
    assert is_prime(1) == False    
    assert is_prime(5) == True    
    assert is_prime(11) == True    
    assert is_prime(17) == True    
    assert is_prime(5 * 17) == False   
    assert is_prime(11 * 7) == False   
    assert is_prime(13441 * 19) == False

def test2():
    from ai_unit_testing.code_under_test import add_elements
    assert add_elements([1,-2,-3,41,57,76,87,88,99], 3) == -4
    assert add_elements([111,121,3,4000,5,6], 2) == 0
    assert add_elements([11,21,3,90,5,6,7,8,9], 4) == 125
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert add_elements([1], 1) == 1

def test3():
    from ai_unit_testing.code_under_test import solution
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0
    assert solution([5, 9]) == 5
    assert solution([2, 4, 8]) == 0
    assert solution([30, 13, 23, 32]) == 23
    assert solution([3, 13, 2, 9]) == 3

def test4():
    from ai_unit_testing.code_under_test import digits
    assert digits(5) == 5
    assert digits(54) == 5
    assert digits(120) ==1
    assert digits(5014) == 5
    assert digits(98765) == 315
    assert digits(5576543) == 2625