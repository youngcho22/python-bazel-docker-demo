import sys
from colorama import init, Fore, Back

init()

def main():
  print(Fore.CYAN + Back.MAGENTA + "Hello, world. ")

  return 0

if __name__ == '__main__':
  sys.exit(main()) 
