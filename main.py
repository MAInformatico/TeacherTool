from B2 import *
from collections import defaultdict
import pandas as pd

def get_info(language_level, num_exam, students):
        dict_results = {
             "Nombre" : [],
             "Reading": [],
             "Listening": [],
             "Writting": [],
             "Speaking": [],
             "English_use": []
        }

        text = "Escribe los aciertos y el total\n" + "Escribe el primer numero separado por una / y luego el segundo"        
        for num_exam in range(0,num_exam):
            for students in range(0,students):
                print("Nombre del alumno")
                name = str(input())
                dict_results['Nombre'].append(name)
                '''
                print('Reading')
                print(text)
                reading = filter(str(input()))
                dict_results['Reading'].append(reading)
                print('Listening')
                print(text)                
                listening = filter(str(input()))
                dict_results['Listening'].append(listening)
                print('Writting')
                print(text)
                writting = filter(str(input()))
                dict_results['Writting'].append(writting)
                print('Speaking')
                print(text)
                speaking = filter(str(input()))
                dict_results['Speaking'].append(speaking)
                if language_level == "B2":
                    print('English use')
                    print(text)
                    english_use = filter(str(input()))
                    dict_results['English_use'].append(english_use)
                    '''
        print(dict_results)
        return dict_results


if __name__ == "__main__":
    language_level = " "
    print("¿Cuántos alumnos tienes?")
    students = int(input())
    print('¿Cuántos exámenes quieres evaluar?')
    num_exam = int(input())
    while(language_level != "B1" and language_level != "B2"):
        print("¿Se presentan a B1 o B2?")
        language_level = str(input())
        print(language_level)
    
    dict_evaluaciones = pd.DataFrame(get_info(language_level,num_exam,students))    

