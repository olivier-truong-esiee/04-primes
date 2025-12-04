# main.py
"""
Nombres premiers
"""

def isprime(p: int) -> bool:
    """
    isprime(p : int) -> bool
    Args:
        p: int

    Returns:
        bool
    
    >>> isprime(7)
    True
    >>> isprime(10)
    False
    """

    premier = True
    borne_max = int(p**0.5) + 1
    for i in range(2, borne_max):
        if p % i == 0:
            premier = False
            break
    return premier




def main():
    """
    Appel principal
    """
    for n in range(100):
        if isprime(n):
            print(n, end=', ')

    print()

if __name__ == '__main__':
    main()
