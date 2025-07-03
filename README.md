# TeacherTool

**TeacherTool** is a web tool developed with **FastAPI** that helps **language teachers** calculate the grades for Cambridge exams that certify language proficiency levels (B1, B2, etc.). This application simplifies the grading process and enables educators to manage exam results quickly and efficiently.

## Features

- **Automatic grade calculation**: Calculates grades for Cambridge exams for different language proficiency levels.
- **RESTful API**: The app exposes an API that can be used by other tools or integrations.
- **Easy installation**: Includes a script to quickly set up the project in your local environment.
- **Export results to DOCX**: Students' exam results can be automatically exported to a `.docx` file for easy printing or record-keeping.


## Technologies

- **FastAPI**: A modern and fast web framework for Python.
- **Python 3.x**: The primary programming language.
- **Jinja2**: Templating engine used for rendering views.
- **python-docx**: Library to generate `.docx` files.

## Requirements

Make sure you have **Python 3.x** installed. You can install the project's dependencies using the `requirements.txt` file or the provided `.sh` installation script.

Additionally, you need to have a `test.docx` file with a pre-created table structure. This file will be used to populate and export student results. The table should have the following structure (or similar):

- Column 1: Student Full Name
- Column 2: Reading
- Column 3: Use of English
- Column 4: Writing
- Column 5: Listening
- Column 6: Speaking
- Column 7: Overrall

**Recommended platforms**: It is recommended to run this project on **Linux** or **Windows** for the best compatibility. 


## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/MAInformatico/TeacherTool.git
cd TeacherTool
```
### Step 2: Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the project
You can run the project locally using the .sh installation script (if you're on a Unix environment) or directly with Uvicorn:

Using the .sh script:
```bash
./execute.sh
```

