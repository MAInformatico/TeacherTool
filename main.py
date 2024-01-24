from B2 import *
from collections import defaultdict

def default_value():
    return "No existe ese alumno o nota"


if __name__ == "__main__":    
    print("¿Cuantos alumnos tienes?")
    students = int(input())
    print("¿Se presentan a B1 o B2?")
    languageLevel = str(input())
    if languageLevel != "B1" or languageLevel != "B2":
        while(languageLevel != "B1" or languageLevel != "B2"):
            print("¿Se presentan a B1 o B2?")
            languageLevel = input()
    else:
        group  = defaultdict(default_value)



