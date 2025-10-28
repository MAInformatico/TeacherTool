from Reporter.FileGenerator import FileGenerator
from Reporter.FileGenerator_child import filegenerator_child
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os


class Item(BaseModel):    
    num_exam: int
    language_level: str
    students   : int
    dict_list_values: dict



app = FastAPI()


# @app.post("/get_files")
# async def get_files(item: Item):
    # averageOverall = []
    # averageReading = []
    # averageListening = []
    # averageWriting = []
    # averageSpeaking = []
    # averageUseEnglish = []


    # dict_notes = {
    #             'Name' : [],
    #             'Reading': [],
    #             'Listening': [],
    #             'Writing': [],
    #             'Speaking': [],
    #             'Use_English': [],
    #             'Overall': []             
    #         }

    # list_values = item.dict_list_values

    # num_exam = item.num_exam
    # language_level = item.language_level
    # students = item.students        
    
    # generator = filegenerator_child(language_level, students, num_exam, list_values)

    # language_level, dict_notes, num_exam, students = generator.get_info(averageOverall,averageReading,averageListening,averageSpeaking,averageWriting,averageUseEnglish)
    # results_file = generator.generate_files(dict_notes, num_exam)
    # file_path = os.path.join(os.getcwd(), results_file)
    # download_name_file = file_path.split("/")[-1]
    # if file_path:        
    #     return FileResponse(file_path, media_type='application/octet-stream',filename=download_name_file)
    # else:
    #     return {"error" : "File not found!"}    

@app.post("/get_files")
async def get_files(item: Item):
    try:
        if not item.dict_list_values:
            raise HTTPException(status_code=400, detail="El diccionario de valores no puede estar vacío")
        
        if item.language_level not in ["B1", "B2", "C1"]:
            raise HTTPException(status_code=400, detail="Nivel de idioma no válido")

        # Inicializar listas
        averages = {
            'Overall': [],
            'Reading': [],
            'Listening': [],
            'Speaking': [],
            'Writing': [],
            'Use_English': []
        }

        dict_notes = {
            'Name': [],
            'Reading': [],
            'Listening': [],
            'Writing': [],
            'Speaking': [],
            'Use_English': [],
            'Overall': []             
        }

        print(f"Processing input data with {len(item.dict_list_values)} students")
        
        generator = filegenerator_child(
            item.language_level, 
            item.students, 
            item.num_exam, 
            item.dict_list_values
        )
        
        try:
            language_level, dict_notes, num_exam, students = generator.get_info(
                averages['Overall'],
                averages['Reading'],
                averages['Listening'],
                averages['Speaking'],
                averages['Writing'],
                averages['Use_English']
            )
            print(f"Successfully processed data for {students} students")
        except KeyError as ke:
            print(f"KeyError in get_info: {ke}")
            raise HTTPException(status_code=400, detail=f"Falta la clave requerida: {str(ke)}")
        except IndexError as ie:
            print(f"IndexError in get_info: {ie}")
            raise HTTPException(status_code=400, detail=f"Error en el formato de los datos: {str(ie)}")
        except Exception as e:
            print(f"Unexpected error in get_info: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error procesando datos: {str(e)}")

        results_file = generator.generate_files(dict_notes, num_exam)
        file_path = os.path.join(os.getcwd(), results_file)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="No se pudo generar el archivo")
            
        download_name_file = file_path.split("/")[-1]
        return FileResponse(file_path, media_type='application/octet-stream', filename=download_name_file)

    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "API is running"}