def roman (n):
    if type(n) != int:
        raise ValueError('Wrong type.')
    if n >= 4000:
        raise ValueError('Number too big.')
    if n <= 0:
        raise ValueError('Number too small.')
    wynik = ""
    j = n % 10
    d = int(n / 10) % 10
    s = int(n / 100) % 10
    t = int(n / 1000) % 10
    match j:
        case 1:
            wynik = "I"
        case 2:
            wynik = "II"
        case 3:
            wynik = "III"
        case 4:
            wynik = "IV"
        case 5:
            wynik = "V"
        case 6:
            wynik = "VI"
        case 7:
            wynik = "VII"
        case 8:
            wynik = "VIII"
        case 9:
            wynik = "IX"
        case _:
            wynik = wynik
    match d:
        case 1:
            wynik = "X" + wynik
        case 2:
            wynik = "XX" + wynik 
        case 3:
            wynik = "XXX" + wynik
        case 4:
            wynik = "XL" + wynik
        case 5:
            wynik = "L" + wynik
        case 6:
            wynik = "LX" + wynik
        case 7:
            wynik = "LXX" + wynik
        case 8:
            wynik = "LXXX" + wynik
        case 9:
            wynik = "XC" + wynik
        case _:
            wynik = wynik
    match s:
        case 1:
            wynik = "C" + wynik
        case 2:
            wynik = "CC" + wynik
        case 3:
            wynik = "CCC" + wynik
        case 4:
            wynik = "CD" + wynik
        case 5:
            wynik = "D" + wynik
        case 6:
            wynik = "DC" + wynik
        case 7:
            wynik = "DCC" + wynik
        case 8:
            wynik = "DCCC" + wynik
        case 9:
            wynik = "CM" + wynik
        case _:
            wynik = wynik
    match t:
        case 1:
            wynik = "M" + wynik
        case 2:
            wynik = "MM" + wynik
        case 3:
            wynik = "MMM" + wynik
        case _:
            wynik = wynik
    return wynik

