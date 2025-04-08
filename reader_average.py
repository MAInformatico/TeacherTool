
import pandas as pd
import requests

from docx.api import Document

class ReaderAverage:
    """
    This class reads .docx files and extracts data from the first table.
    It assumes that the first row of the table contains the headers.
    The data is returned as a list of dictionaries, where each dictionary
    represents a row in the table with keys as the headers.
    """
    def __init__(self):
        # Initialize an empty list to store the data        
        self.data = []

    def read_file(self,name_file: str):
        document = Document(name_file)
        table = document.tables[0]

        # Data will be a list of rows represented as dictionaries
        # containing each row's data.    
        keys = None
        for i, row in enumerate(table.rows):
            text = (cell.text for cell in row.cells)

            # Establish the mapping based on the first row
            # headers; these will become the keys of our dictionary
            if i == 0:
                keys = tuple(text)
                continue

            # Construct a dictionary for this row, mapping
            # keys to values for this row
            row_data = dict(zip(keys, text))
            self.data.append(row_data)

    def get_student_names(self):
        """
        Returns a list of student names from the data.
        Assumes that the first column contains the student names.
        """
        # Convert the list of dictionaries to a DataFrame
        # and clean the column names by stripping whitespace
        # from the start and end of each column name
        pdf = pd.DataFrame(objeto.data)
        pdf.columns = pdf.columns.str.strip()
        # Extracting the first and last names from the "FULL NAME" column
        student_list = pdf["FULL NAME"].str.split(" ", n=1, expand=True).drop_duplicates()
        return student_list
    
    def check_student_names(self, student_name: str):
        pdf = self.get__dataframe()
        pdf.columns = pdf.columns.str.strip()
        # Extracting the first and last names from the "FULL NAME" column
        student_name = objeto.get_student_names()

        #Filtering the DataFrame to find the row with the specified student name
        print(pdf.loc[pdf['FULL NAME'] == student_name])
    
    def get__dataframe(self):
        """
        Returns the data as a DataFrame.
        """
        # Convert the list of dictionaries to a DataFrame
        # and clean the column names by stripping whitespace
        # from the start and end of each column name
        pdf = pd.DataFrame(objeto.data)
        pdf.columns = pdf.columns.str.strip()
        return pdf




