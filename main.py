from B2 import *
from collections import defaultdict
from colorama import Fore
import pandas as pd
import numpy as np

def get_info(language_level, num_exam, students):
        dict_results = {
             'Nombre' : [],
             'Reading': [],
             'Listening': [],
             'Writting': [],
             'Speaking': [],
             'English_use': [],
             'Overall': []             
        }

        text = "Escribe los aciertos y el total\n" + "Escribe el primer numero separado por una / y luego el segundo"                
        underline = '========'
        
        for students in range(0,students):
            print(Fore.WHITE + "Nombre del alumno")
            name = str(input())
            dict_results['Nombre'].append(name)
            instance = B2(name,num_exam)
            for iterator in range(0,num_exam):            
                averageTest = []
                #Reading
                print(Fore.RED + 'Reading')
                print(underline)
                print(text)
                aux = str(input())
                reading = instance.filter(aux)
                result = instance.percent_category(int(reading[0]),int(reading[1]))
                #print(result)
                averageTest.append(result)
                dict_results['Reading'].append(str(aux))
                #dict_results['Reading'].append(str(reading) + ' = ' + str(result))
                #Listening
                print(Fore.YELLOW + 'Listening')
                print(underline)
                print(text)
                aux = str(input())                
                listening = instance.filter(aux)
                result = instance.percent_category(listening[0],listening[1])
                averageTest.append(result)
                dict_results['Listening'].append(str(aux))
                #dict_results['Listening'].append(str(listening) + ' = ' + str(result))
                #Writting
                print(Fore.BLUE + 'Writting')
                print(underline)
                print(text)
                aux = str(input())
                writting = instance.filter(aux)
                result = instance.percent_category(writting[0],writting[1])
                averageTest.append(result)
                dict_results['Writting'].append(str(aux))
                #dict_results['Writting'].append(str(writting) + ' = ' + str(result))
                #Speaking
                print(Fore.GREEN + 'Speaking')
                print(underline)
                print(text)
                aux = str(input())
                speaking = instance.filter(aux)
                result = instance.percent_category(speaking[0],speaking[1])
                averageTest.append(result)
                dict_results['Speaking'].append(aux)
                #dict_results['Speaking'].append(str(speaking) + ' = ' + str(result))
                if language_level == "B2":
                    #English use
                    print(Fore.WHITE + 'English use')
                    print(underline)
                    print(text)
                    aux = str(input())
                    english_use = instance.filter(aux)
                    result = instance.percent_category(english_use[0],english_use[1])
                    averageTest.append(result)
                    dict_results['English_use'].append(aux)
                    #dict_results['English_use'].append(str(english_use) + ' = ' + str(result))
                else: #It is a B1 exam
                    dict_results['English_use'].append(str('X'))
                #calculate average and insert in Overall array
                dict_results['Overall'].append(np.mean((averageTest)))
                iterator += 1
        #print(dict_results)
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
    
    #dict_notes = get_info(language_level,num_exam,students)
    #dict_evaluaciones = pd.DataFrame(dict_notes)
    print(get_info(language_level,num_exam,students))
    #print(dict_evaluaciones)   

