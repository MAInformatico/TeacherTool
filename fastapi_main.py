from Reporter.FileGenerator import FileGenerator
from Reporter.FileGenerator_child import filegenerator_child
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os


class Item(BaseModel):    
    num_exam: int
    language_level: str
    students   : int
    dict_list_values: dict



app = FastAPI()


@app.post("/get_files")
async def get_files(item: Item):
    averageOverall = []
    averageReading = []
    averageListening = []
    averageWriting = []
    averageSpeaking = []
    averageUseEnglish = []


    dict_notes = {
                'Name' : [],
                'Reading': [],
                'Listening': [],
                'Writing': [],
                'Speaking': [],
                'Use_English': [],
                'Overall': []             
            }

    list_values = item.dict_list_values

    num_exam = item.num_exam
    language_level = item.language_level
    students = item.students        
    
    generator = filegenerator_child(language_level, students, num_exam, list_values)

    language_level, dict_notes, num_exam, students = generator.get_info(averageOverall,averageReading,averageListening,averageSpeaking,averageWriting,averageUseEnglish)
    results_file = generator.generate_files(dict_notes, num_exam)
    file_path = os.path.join(os.getcwd(), results_file)
    download_name_file = file_path.split("/")[-1]
    if file_path:        
        return FileResponse(file_path, media_type='application/octet-stream',filename=download_name_file)
    else:
        return {"error" : "File not found!"}    


@app.get("/")
async def root():
    return {"message": "API is running"}