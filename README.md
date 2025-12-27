# School-System-cli📖

A command-line based school management system built with Python.
This project is designed to simulate a simple school system, focusing on student data management and subject score processing using JSON files.

## Features
- Add and manage student data (name, NISN, gender, class, etc.)
- Store student data by grade and class
- Select subjects from a predefined list
- Input daily scores, midterm (PTS), and final exam (PAS)
- Automatically calculate final subject scores
- Save and load data using JSON files as a simple database
- Menu-based interaction through the terminal (CLI)

## Project Structure
- `Main.py`  
  The main entry point of the application and menu controller.

- `Datamanager/`  
  Handles data processing and file management.
  - `DataEditor.py` → student data and score storage
  - `Graders.py` → score calculation and subject selection logic

- `Datacenter/`  
  Stores JSON data files.
  - `Students.json`
  - `StudentsScore.json`

## How to Run
1. Make sure Python is installed
2. Clone this repository
3. Run the program:
   ```bash
   python Main.py
Follow the instructions shown in the terminal
Purpose
This project was created to:
Practice Python fundamentals (functions, classes, and file handling)
Learn how to manage structured data using JSON
Build a CLI-based application with real use cases
Improve logical thinking and project organization
Notes
This project is still under development. Future improvements may include:
Input validation
Editing and deleting student data
Average score and ranking calculation
Better CLI navigation and UX
Author
Naufal Azhar
Salin kode

---

### Kenapa README ini **aman buat GitHub**
- Nggak overclaim
- Fokus ke **apa yang ada sekarang**
- Bahasa developer pelajar asli
- Cocok buat repo publik & portfolio awal

Kalau lu mau next:
- versi **lebih profesional (buat beasiswa / CV)**
- atau README **lebih singkat tapi tajam**

tinggal bilang, bro. Repo lu arahnya udah bener 🔥
