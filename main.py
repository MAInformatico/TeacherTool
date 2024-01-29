from B2 import *
from collections import defaultdict
import pandas as pd


if __name__ == "__main__":    
    print("¿Cuántos alumnos tienes?")
    students = int(input())
    print("¿Se presentan a B1 o B2?")    
    languageLevel = str(input())
    print('¿Cuántos exámenes quieres evaluar?')
    numExam = int(input())
    if languageLevel != "B1" or languageLevel != "B2":
        while(languageLevel != "B1" or languageLevel != "B2"):
            print("¿Se presentan a B1 o B2?")
            languageLevel = input()
    else:
        alumno = { 'Nombre' : '', 'Notas' : [] }
        for students in range(0,students-1):
            print("Nombre del alumno")
            name = str(input())
            alumno['Nombre'] = name
            print('Reading')
            print('Escribe los aciertos y el total')
            reading = filter(str(input()))
            print('Listening')
            print('Escribe los aciertos y el total')
            listening = filter(str(input()))
            print('Writting')
            print('Escribe los aciertos y el total')
            writting = filter(str(input()))
            print('Speaking \n =======')
            print('Escribe los aciertos y el total')
            speaking = filter(str(input()))

