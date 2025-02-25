from Reporter.FileGenerator import FileGenerator

if __name__ == "__main__":

    #storing averages
    
    averageOverall = []
    averageReading = []
    averageListening = []
    averageWriting = []
    averageSpeaking = []
    averageUseEnglish = []    

    #Showing info by terminal
    #========================

    generator = FileGenerator()
    language_level, dict_notes, num_exam, students = generator.get_info(averageOverall,averageReading,averageListening,averageSpeaking,averageWriting,averageUseEnglish)        
    generator.generate_files(dict_notes, num_exam)