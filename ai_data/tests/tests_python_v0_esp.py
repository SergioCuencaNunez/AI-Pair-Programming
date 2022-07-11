def test0(solution):
    exec(solution, globals())
    assert incr_lista([]) == []
    assert incr_lista([3, 2, 1]) == [4, 3, 2]
    assert incr_lista([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]

def test1(solution):
    exec(solution, globals())
    assert es_primo(6) == False   
    assert es_primo(101) == True    
    assert es_primo(11) == True   
    assert es_primo(13441) == True    
    assert es_primo(61) == True   
    assert es_primo(4) == False   
    assert es_primo(1) == False    
    assert es_primo(5) == True    
    assert es_primo(11) == True    
    assert es_primo(17) == True    
    assert es_primo(5 * 17) == False   
    assert es_primo(11 * 7) == False   
    assert es_primo(13441 * 19) == False

def test2(solution):
    exec(solution, globals())
    assert anadir_elementos([1,-2,-3,41,57,76,87,88,99], 3) == -4
    assert anadir_elementos([111,121,3,4000,5,6], 2) == 0
    assert anadir_elementos([11,21,3,90,5,6,7,8,9], 4) == 125
    assert anadir_elementos([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert anadir_elementos([1], 1) == 1

def test3(solution):
    exec(solution, globals())
    assert solucion([5, 8, 7, 1]) == 12
    assert solucion([3, 3, 3, 3, 3]) == 9
    assert solucion([30, 13, 24, 321]) == 0
    assert solucion([5, 9]) == 5
    assert solucion([2, 4, 8]) == 0
    assert solucion([30, 13, 23, 32]) == 23
    assert solucion([3, 13, 2, 9]) == 3

def test4(solution):
    exec(solution, globals())
    assert digitos(5) == 5
    assert digitos(54) == 5
    assert digitos(120) ==1
    assert digitos(5014) == 5
    assert digitos(98765) == 315
    assert digitos(5576543) == 2625