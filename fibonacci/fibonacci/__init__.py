from colorama import Fore

def fibonacci(n):
    a, b = 0, 1
    results = []
    for i in range(n):
        results.append(a)
        a, b = b, a + b
    return results

COLORS = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN ]

def colorify(x):
    return COLORS[x % len(COLORS)] + str(x)

def rainbow_fibonacci(n):
    return " ".join([ colorify(x) for x in fibonacci(n) ])
