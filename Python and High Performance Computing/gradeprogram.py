import sys

def main():
    grades = [float(grade) for grade in sys.argv[1:]]
    
    mean_grade = sum(grades) / len(grades)
    
    result = "Pass" if mean_grade >= 5 else "Fail"
    
    print(f"{mean_grade:.2f} {result}")

if __name__ == "__main__":
    main()