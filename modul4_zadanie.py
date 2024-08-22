def palindrom(x):
    """
        Funkcja sprawdza czy dany wyraz jest palindromem
    """
    return "True" if x == x[::-1] else "False"

print(palindrom("potop"))