from  TeacherTool.B2 import B2
from colorama import Fore
import numpy as np
from docx import Document
import docxedit


def get_info(language_level, num_exam, students,average_overall,average_reading,average_listening,average_speaking,average_writing,average_use_english):
        dict_results = {
            'Nombre' : [],
            'Reading': [],
            'Listening': [],
            'Writing': [],
            'Speaking': [],
            'Use_English': [],
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
            avg_writing = []
            avg_speaking = []
            avg_use_english = []
            for _ in range(0,num_exam):            
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
                print(Fore.BLUE + 'Writing')
                print(underline)
                print(text)
                aux = str(input())
                if not aux:
                    result = 'X'
                    dict_results['Writing'].append(str(aux) + ' = ' + str(result))
                else:
                    writing = instance.filter(aux)
                    result = instance.percent_category(writing[0],writing[1])
                    average_test.append(result)
                    avg_writing.append(result)
                    #dict_results['Writing'].append(str(aux))
                    dict_results['Writing'].append(str(aux) + ' = ' + str(result))
                #dict_results['Writing'].append(str(writing) + ' = ' + str(result))
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
                if language_level[0] == "B2" and language_level[1] == 2:
                    #English use
                    print(Fore.WHITE + 'English use')
                    print(underline)
                    print(text)
                    aux = str(input())
                    if not aux:
                        result = 'X'
                        dict_results['Use_English'].append(str(aux) + ' = ' + str(result))
                    else:
                        english_use = instance.filter(aux)                    
                        result = instance.percent_category(english_use[0],english_use[1])
                        average_test.append(result)
                        avg_use_english.append(result)
                    #dict_results['English_use'].append(aux)
                        dict_results['Use_English'].append(str(aux) + ' = ' + str(result))
                    #dict_results['English_use'].append(str(english_use) + ' = ' + str(result))
                else: #It is a B1 exam
                    dict_results['Use_English'].append(str('X'))
                #calculate average and insert in Overall array
                aux = np.mean(average_test)
                dict_results['Overall'].append(aux)                
            average_overall.append(aux)
            average_reading.append(np.mean(avg_reading))
            average_listening.append(np.mean(avg_listening))
            average_writing.append(np.mean(avg_writing))
            average_speaking.append(np.mean(avg_speaking))
            if language_level[0] == "B2" and language_level[1] == 2:
                average_use_english.append(np.mean(avg_use_english))
            
        #print(dict_results)
        return dict_results


if __name__ == "__main__":
    language_level = [" "]
    print("¿Cuántos alumnos tienes?")
    students = int(input())
    print('¿Cuántos exámenes quieres evaluar?')
    num_exam = int(input())
    while(language_level[0] != "B1" and language_level[0] != "B2"):
        print("¿Se presentan a B1 o B2?")
        language_level[0] = str(input())
        print(language_level[0])
        if language_level[0] == "B2":
            print("¿Son alumnos de primer o segundo año? (escribe 1 o 2)")
            language_level.append(int(input()))

    #storing averages
    
    averageOverall = []
    averageReading = []
    averageListening = []
    averageWriting = []
    averageSpeaking = []
    averageUseEnglish = []    

    #Showing info by terminal
    #========================

    dict_notes = get_info(language_level,num_exam,students,averageOverall,averageReading,averageListening,averageSpeaking,averageWriting,averageUseEnglish)    


    document = Document('test.docx')
    docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=1, new_string='Hello')
    document.save('test.docx')

    '''
    valuetoclean = "np.float64("
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
    fichero.write(str(averageReading).replace(valuetoclean,'').replace(')',''))
    fichero.write("\n")
    fichero.write("Listening:")
    fichero.write(str(averageListening).replace(valuetoclean,'').replace(')',''))
    fichero.write("\n")
    fichero.write("Writing:")
    fichero.write(str(averageWriting).replace(valuetoclean,'').replace(')',''))
    fichero.write("\n")
    fichero.write("Speaking:")
    fichero.write(str(averageSpeaking).replace(valuetoclean,'').replace(')',''))
    fichero.write("\n")
    if language_level[0] != 'B1':
        fichero.write("English Use:")
        fichero.write(str(averageUseEnglish).replace(valuetoclean,'').replace(')',''))
        fichero.write("\n")
    fichero.write("Overall:")
    fichero.write(str(averageOverall).replace(valuetoclean,'').replace(')',''))
    fichero.write("\n")
    fichero.write("Fin de las medias por área\n")    
    fichero.close()
    '''