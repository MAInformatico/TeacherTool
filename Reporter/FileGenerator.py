from  TeacherTool.B2 import B2
from colorama import Fore
from docx import Document
import docxedit
import numpy as np
from datetime import datetime
import os

class FileGenerator():

    def get_initial_data(self):
        language_level = [" "]
        print("¿Cuántos alumnos tienes?")
        students = int(input())
        print('¿Cuántos exámenes quieres evaluar?')
        num_exam = int(input())
        while(language_level[0] != "B1" and language_level[0] != "B2" and language_level[0] != "C1"):
            print("¿Se presentan a B1, B2 o C1?")
            language_level[0] = str(input())
            print(language_level[0])
            if language_level[0] == "B2" or language_level[0] == "C1":
                print("¿Son alumnos de primer o segundo año? (escribe 1 o 2)")
                language_level.append(int(input()))
        
        return language_level, students, num_exam



    def get_info(self,average_overall,average_reading,average_listening,average_speaking,average_writing,average_use_english):
            language_level, students, num_exam = self.get_initial_data()
            
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



    def generate_files(self,dict_notes,num_exam):
        valuetoclean = "np.float64("        
        name_file = 'test.docx'
        if num_exam == 1 and len(dict_notes['Nombre']) == 1:
            document = Document(name_file)
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=0, new_string=str(dict_notes['Nombre']).replace('[\'','').replace('\']',''))
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=1, new_string=str(dict_notes['Reading']).replace('[\'','').replace('\']',''))
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=2, new_string=str(dict_notes['Use_English']).replace('[\'','').replace('\']',''))
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=3, new_string=str(dict_notes['Writing']).replace('[\'','').replace('\']',''))
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=4, new_string=str(dict_notes['Listening']).replace('[\'','').replace('\']',''))
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=5, new_string=str(dict_notes['Speaking']).replace('[\'','').replace('\']',''))
            docxedit.add_text_in_table(document.tables[0], row_num=1, column_num=6, new_string=str(dict_notes['Overall']).replace(valuetoclean,'').replace(')','').replace('[','').replace(']',''))
            document.save(name_file)
        elif num_exam == 1 and len(dict_notes['Nombre']) > 1:
            document = Document(name_file)
            for i in range(0,len(dict_notes['Nombre'])):            
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=0, new_string=str(dict_notes['Nombre'][i]).replace('[\'','').replace('\']',''))
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=1, new_string=str(dict_notes['Reading'][i]).replace('[\'','').replace('\']',''))
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=2, new_string=str(dict_notes['Use_English'][i]).replace('[\'','').replace('\']',''))
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=3, new_string=str(dict_notes['Writing'][i]).replace('[\'','').replace('\']',''))
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=4, new_string=str(dict_notes['Listening'][i]).replace('[\'','').replace('\']',''))
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=5, new_string=str(dict_notes['Speaking'][i]).replace('[\'','').replace('\']',''))
                docxedit.add_text_in_table(document.tables[0], row_num=i+1, column_num=6, new_string=str(dict_notes['Overall'][i]).replace(valuetoclean,'').replace(')','').replace('[','').replace(']',''))
            document.save(name_file)
            return name_file

    def change_name_file(name_file):
        file_oldname = os.path.join(str(os.getcwd()), name_file)
        file_newname_newfile = os.path.join(str(os.getcwd()), "test" + str(datetime.now()) + ".docx")
        os.rename(file_oldname, file_newname_newfile)
        print(file_newname_newfile)