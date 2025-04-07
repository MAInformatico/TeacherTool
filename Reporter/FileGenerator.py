from  TeacherTool.B2 import B2
from colorama import Fore
from docx import Document
import docxedit
import numpy as np
import os
import shutil

class FileGenerator():

    def __init__(self, language_level=None, students=None, num_exam=None):
        self.language_level = language_level
        self.students = students
        self.num_exam = num_exam

    def get_info(self,average_overall,average_reading,average_listening,average_speaking,average_writing,average_use_english):
            language_level, students, num_exam = self.get_initial_data()
            
            dict_results = {
                'Name' : [],
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
                print(Fore.WHITE + "Name del alumno")
                name = str(input())
                dict_results['Name'].append(name)
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
                        dict_results['Reading'].append(str(aux))
                    else:
                        reading = instance.filter(aux)
                        result = instance.percent_category(int(reading[0]),int(reading[1]))
                        average_test.append(result)
                        avg_reading.append(result)
                        dict_results['Reading'].append(str(aux))
                    #Listening
                    print(Fore.YELLOW + 'Listening')
                    print(underline)
                    print(text)
                    aux = str(input())                
                    if not aux:
                        result = 'X'
                        dict_results['Listening'].append(str(aux))
                    else:
                        listening = instance.filter(aux)
                        result = instance.percent_category(listening[0],listening[1])
                        average_test.append(result)
                        avg_listening.append(result)
                        dict_results['Listening'].append(str(aux))
                    #Writting
                    print(Fore.BLUE + 'Writing')
                    print(underline)
                    print(text)
                    aux = str(input())
                    if not aux:
                        result = 'X'
                        dict_results['Writing'].append(str(aux))
                    else:
                        writing = instance.filter(aux)
                        result = instance.percent_category(writing[0],writing[1])
                        average_test.append(result)
                        avg_writing.append(result)
                        dict_results['Writing'].append(str(aux))
                    #Speaking
                    print(Fore.GREEN + 'Speaking')
                    print(underline)
                    print(text)
                    aux = str(input())
                    if not aux:
                        result = 'X'
                        dict_results['Speaking'].append(str(aux))
                    else:
                        speaking = instance.filter(aux)
                        result = instance.percent_category(speaking[0],speaking[1])
                        average_test.append(result)
                        avg_speaking.append(result)
                        dict_results['Speaking'].append(str(aux))
                    if (language_level[0] == "B2" and language_level[1] == 2) or (language_level[0] == "C1"):
                        #English use
                        print(Fore.WHITE + 'English use')
                        print(underline)
                        print(text)
                        aux = str(input())
                        if not aux:
                            result = 'X'
                            dict_results['Use_English'].append(str(aux))
                        else:
                            english_use = instance.filter(aux)                    
                            result = instance.percent_category(english_use[0],english_use[1])
                            average_test.append(result)
                            avg_use_english.append(result)
                            dict_results['Use_English'].append(str(aux))
                    else: #It is a B1 exam
                        dict_results['Use_English'].append(str('X'))
                    #calculate average and insert in Overall array
                    aux = np.mean(average_test)
                    dict_results['Overall'].append(np.ceil(aux))                
                average_overall.append(aux)
                average_reading.append(np.mean(avg_reading))
                average_listening.append(np.mean(avg_listening))
                average_writing.append(np.mean(avg_writing))
                average_speaking.append(np.mean(avg_speaking))
                if (language_level[0] == "B2" and language_level[1] == 2) or (language_level[0] == "C1"):
                    average_use_english.append(np.mean(avg_use_english))
                
            return language_level, dict_results, num_exam, students