from B2 import *
from collections import defaultdict
from colorama import Fore
import numpy as np


def get_info(language_level, num_exam, students,averageReading,averageListening,averageSpeaking,averageWritting,averageEnglishUse):
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
            avg_reading = []
            avg_listening = []
            avg_writting = []
            avg_speaking = []
            avg_englishUse = []
            for iterator in range(0,num_exam):            
                average_test = []
                #Reading
                print(Fore.RED + 'Reading')
                print(underline)
                print(text)
                aux = str(input())
                if not aux:
                     result = 'X'
                     dict_results['Reading'].append(str(aux) + ' = ' + str(result))
                else:
                    reading = instance.filter(aux)
                    result = instance.percent_category(int(reading[0]),int(reading[1]))
                #print(result)
                    average_test.append(result)
                    avg_reading.append(result)
                    dict_results['Reading'].append(str(aux) + ' = ' + str(result))
                #dict_results['Reading'].append(str(reading) + ' = ' + str(result))
                #Listening
                print(Fore.YELLOW + 'Listening')
                print(underline)
                print(text)
                aux = str(input())                
                if not aux:
                     result = 'X'
                     dict_results['Listening'].append(str(aux) + ' = ' + str(result))
                else:
                    listening = instance.filter(aux)
                    result = instance.percent_category(listening[0],listening[1])
                    average_test.append(result)
                    avg_listening.append(result)
                #dict_results['Listening'].append(str(aux))
                    dict_results['Listening'].append(str(aux) + ' = ' + str(result))
                #dict_results['Listening'].append(str(listening) + ' = ' + str(result))
                #Writting
                print(Fore.BLUE + 'Writting')
                print(underline)
                print(text)
                aux = str(input())
                if not aux:
                     result = 'X'
                     dict_results['Writting'].append(str(aux) + ' = ' + str(result))
                else:
                    writting = instance.filter(aux)
                    result = instance.percent_category(writting[0],writting[1])
                    average_test.append(result)
                    avg_writting.append(result)
                    #dict_results['Writting'].append(str(aux))
                    dict_results['Writting'].append(str(aux) + ' = ' + str(result))
                #dict_results['Writting'].append(str(writting) + ' = ' + str(result))
                #Speaking
                print(Fore.GREEN + 'Speaking')
                print(underline)
                print(text)
                aux = str(input())
                if not aux:
                     result = 'X'
                     dict_results['Speaking'].append(str(aux) + ' = ' + str(result))
                else:
                    speaking = instance.filter(aux)
                    result = instance.percent_category(speaking[0],speaking[1])
                    average_test.append(result)
                    avg_speaking.append(result)
                #dict_results['Speaking'].append(aux)
                    dict_results['Speaking'].append(str(aux) + ' = ' + str(result))
                #dict_results['Speaking'].append(str(speaking) + ' = ' + str(result))
                if language_level == "B2":
                    #English use
                    print(Fore.WHITE + 'English use')
                    print(underline)
                    print(text)
                    aux = str(input())
                    if not aux:
                        result = 'X'
                        dict_results['Speaking'].append(str(aux) + ' = ' + str(result))
                    else:
                        english_use = instance.filter(aux)                    
                        result = instance.percent_category(english_use[0],english_use[1])
                        average_test.append(result)
                        avg_englishUse.append(result)
                    #dict_results['English_use'].append(aux)
                        dict_results['English_use'].append(str(aux) + ' = ' + str(result))
                    #dict_results['English_use'].append(str(english_use) + ' = ' + str(result))
                else: #It is a B1 exam
                    dict_results['English_use'].append(str('X'))
                #calculate average and insert in Overall array
                dict_results['Overall'].append(np.mean(average_test))                
                iterator += 1
            averageReading.append(np.mean(avg_reading))
            averageListening.append(np.mean(avg_listening))
            averageWritting.append(np.mean(avg_writting))
            averageSpeaking.append(np.mean(avg_speaking))
            averageEnglishUse.append(np.mean(avg_englishUse))
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
    

    #storing averages
    
    averageReading = []
    averageListening = []
    averageWritting = []
    averageSpeaking = []
    averageEnglishUse = []    

    #Showing info by terminal
    #========================

    
    dict_notes = get_info(language_level,num_exam,students,averageReading,averageListening,averageSpeaking,averageWritting,averageEnglishUse)    
    fichero = open('Examenes.txt', 'w')
    fichero.write("Estos son los resultados de los examenes o del examen que has insertado:\n")
    fichero.write('\n'.join("{}: {}".format(k, v) for k, v in dict_notes.items()))    
    fichero.write("\n")
    arrayStudents = dict_notes
    fichero.write("\n")
    fichero.write("Los alumnos han obtenido las siguientes medias por área:\n")
    fichero.write(str(dict_notes['Nombre']))
    fichero.write("\n")
    fichero.write("Reading:")
    fichero.write(str(averageReading))
    fichero.write("\n")
    fichero.write("Listening:")
    fichero.write(str(averageListening))
    fichero.write("\n")
    fichero.write("Writting:")
    fichero.write(str(averageWritting))
    fichero.write("\n")
    fichero.write("Speaking:")
    fichero.write(str(averageSpeaking))
    fichero.write("\n")
    if language_level != 'B1':
        fichero.write("English Use:")
        fichero.write(str(averageEnglishUse))
        fichero.write("\n")
    fichero.write("Fin de las medias por área\n")    
    fichero.close()




    """   
    print(Fore.WHITE + "Estos son los resultados de los examenes o del examen que has insertado:\n")

    print('\n'.join("{}: {}".format(k, v) for k, v in dict_notes.items()))
    print("\n")
    
    arrayStudents = dict_notes
    print("Los alumnos " + str(dict_notes['Nombre']) + "han obtenido las siguientes medias por área:\n")
    print(str(dict_notes['Nombre']))
    print("Reading:")
    print(averageReading)
    print("Listening:")
    print(averageListening)
    print("Writting:")
    print(averageWritting)
    print("Speaking:")
    print(averageSpeaking)
    if language_level != 'B1':
        print("English Use:")
        print(averageEnglishUse)
    print("Fin de las medias por área\n")    
    """