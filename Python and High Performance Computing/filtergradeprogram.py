import sys

def main():
    grades = [int(grade) for grade in sys.argv[1:]]
    
    print(list(filter(lambda x: not x % 2, grades)))

if __name__ == "__main__":
    main()