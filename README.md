# TeacherTool

TeacherTool is a lightweight backend service built with FastAPI that automates a manual grading workflow used in language exam correction.

The goal of the project was to reduce repetitive manual work involved in calculating exam scores and generating structured reports in DOCX format.

## Problem

Exam grading was previously handled manually, including score calculation across multiple assessment areas and generation of structured Word reports.


## Solution
I built a simple REST API using FastAPI to centralize the grading logic and automate report generation.

The system allows structured input of exam data and produces a formatted DOCX file with the results.

## Design decisions

Given the small scope of the project, I intentionally kept the architecture simple:

* single-service backend (no microservices)
* REST API exposed over HTTP for remote usage
* server-side execution to centralize business logic and avoid client-side dependencies
* containerized deployment using Docker to ensure a consistent and reproducible runtime environment
* template-based DOCX generation for simplicity and maintainability

The focus was on reducing complexity rather than building a highly scalable system.

## Tech stack
* FastAPI
* Pydantic
* Python
* Jinja2
* python-docx

## Outcome

The process was reduced from several manual steps per exam group to a single API call that generates the final DOCX report.

## Requirements

Make sure you have **Python 3.x** installed. You can install the project's dependencies using the `requirements.txt` file or the provided `.sh` installation script.

Additionally, you need to have a `test.docx` file with a pre-created table structure. This file will be used to populate and export student results. The table should have the following structure (or similar):

- Column 1: Student Full Name
- Column 2: Reading
- Column 3: Use of English
- Column 4: Writing
- Column 5: Listening
- Column 6: Speaking
- Column 7: Overall

The application runs on a server and is consumed remotely through a REST API.

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

